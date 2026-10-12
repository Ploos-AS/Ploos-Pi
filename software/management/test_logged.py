import unittest
from logged import LoggedController
from reference import State
from fault_journal import decode

class LoggedTests(unittest.TestCase):
    def running(self):
        c = LoggedController()
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        self.assertEqual(State.RUNNING, c.core.state)
        return c

    def test_pgood_fault_logged_once(self):
        c = self.running()
        c.command("pgood_low")
        c.command("pgood_low")
        self.assertEqual(["rail_fault"], [decode(x).reason for x in c.slots])
        self.assertEqual("RUNNING", decode(c.slots[0]).state)

    def test_startup_timeout_logged(self):
        c = LoggedController()
        c.command("power_on", authorized=True)
        c.advance(1000)
        self.assertEqual("pgood_timeout", decode(c.slots[0]).reason)

    def test_watchdog_logged(self):
        c = self.running()
        c.advance(3000)
        self.assertEqual("watchdog_timeout", decode(c.slots[0]).reason)

    def test_unauthorized_commands_not_logged(self):
        c = LoggedController()
        c.command("power_on")
        c.command("power_cycle")
        self.assertEqual([], c.slots)

    def test_sequence_recovered_from_slots(self):
        c = self.running()
        c.command("pgood_low")
        recovered = LoggedController(slots=list(c.slots))
        self.assertEqual(2, recovered.next_sequence)

    def test_corrupt_slot_ignored(self):
        c = LoggedController(slots=[b"corrupted"])
        self.assertEqual(1, c.next_sequence)
