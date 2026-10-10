"""Safety regressions for the logical reference model."""
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from reference import Controller, State

class SafetyTests(unittest.TestCase):
    def test_fault_during_startup(self):
        c = Controller()
        c.event("power_on", authorized=True)
        c.event("rail_fault")
        self.assertEqual((State.FAULT_LOCKOUT, False), (c.state, c.main_power))

    def test_unsafe_fault_clear_rejected(self):
        c = Controller(state=State.FAULT_LOCKOUT)
        c.event("clear_fault", authorized=True)
        self.assertEqual((State.FAULT_LOCKOUT, False, "rejected"), (c.state, c.main_power, c.last_result))

    def test_recovery_power_off(self):
        c = Controller()
        c.event("recovery", authorized=True)
        self.assertEqual((State.RECOVERY, False), (c.state, c.main_power))
        c.event("recovery_complete")
        self.assertEqual((State.OFF, False), (c.state, c.main_power))

    def test_watchdog_retry_ceiling(self):
        c = Controller(state=State.RUNNING, main_power=True, cycles=3)
        c.event("watchdog_timeout")
        self.assertEqual((State.FAULT_LOCKOUT, False, "rate_limited"), (c.state, c.main_power, c.last_result))

    def test_unauthorized_cycle(self):
        c = Controller(state=State.RUNNING, main_power=True)
        c.event("power_cycle")
        self.assertEqual((State.RUNNING, True, "rejected"), (c.state, c.main_power, c.last_result))

    def test_unknown_event(self):
        c = Controller(state=State.RUNNING, main_power=True)
        c.event("unexpected")
        self.assertEqual((State.RUNNING, True, "rejected"), (c.state, c.main_power, c.last_result))
