"""M2.5 deterministic end-to-end fault sequences; host simulation only."""
import unittest
from logged import LoggedController
from storage import MemoryStorage
from fault_journal import decode
from reference import State
from timed import Timing

class ManagementSequenceTests(unittest.TestCase):
    def test_watchdog_restart_then_retry_lockout(self):
        c = LoggedController(config=Timing(max_cycles=1))
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        self.assertEqual(State.RUNNING, c.core.state)
        c.advance(3000)
        self.assertEqual(State.CYCLING, c.core.state)
        self.assertFalse(c.core.main_power)
        c.advance(500)
        self.assertEqual(State.POWERING_ON, c.core.state)
        c.command("pgood_high")
        c.advance(5000)
        self.assertEqual(State.RUNNING, c.core.state)
        c.advance(3000)
        self.assertEqual(State.FAULT_LOCKOUT, c.core.state)
        self.assertFalse(c.core.main_power)
        self.assertEqual(["watchdog_timeout", "rate_limited"],
                         [decode(s).reason for s in c.slots])

    def test_brownout_in_running_latches_fault(self):
        c = LoggedController()
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        c.command("pgood_low")
        self.assertEqual(State.FAULT_LOCKOUT, c.core.state)
        self.assertFalse(c.core.main_power)
        self.assertEqual("rail_fault", decode(c.slots[0]).reason)

    def test_journal_write_failure_does_not_prevent_rail_off(self):
        storage = MemoryStorage(fail_next_append=True)
        c = LoggedController(storage=storage)
        c.command("power_on", authorized=True)
        c.advance(1000)
        self.assertEqual(State.FAULT_LOCKOUT, c.core.state)
        self.assertFalse(c.core.main_power)
        self.assertEqual(1, c.journal_write_failures)

    def test_rejected_clear_fault_cannot_reenable_power(self):
        c = LoggedController()
        c.command("power_on", authorized=True)
        c.advance(1000)
        c.command("clear_fault", authorized=True, fault_clear=False)
        self.assertEqual(State.FAULT_LOCKOUT, c.core.state)
        self.assertFalse(c.core.main_power)
