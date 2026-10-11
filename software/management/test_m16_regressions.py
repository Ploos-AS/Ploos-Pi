"""M1.6: rail faults and time-step invariance."""
import unittest
from timed import TimedController, Timing
from reference import State

class M16Regressions(unittest.TestCase):
    def running(self):
        c = TimedController()
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        self.assertEqual(State.RUNNING, c.core.state)
        return c

    def test_pgood_drop_latches_fault(self):
        c = self.running()
        self.assertEqual(State.FAULT_LOCKOUT, c.command("pgood_low"))
        self.assertFalse(c.core.main_power)

    def test_large_jump_crosses_watchdog_and_min_off(self):
        c = self.running()
        self.assertEqual(State.POWERING_ON, c.advance(3500))
        self.assertTrue(c.core.main_power)

    def test_chunked_and_large_advance_match(self):
        a = self.running()
        b = self.running()
        a.advance(3500)
        b.advance(3000)
        b.advance(500)
        self.assertEqual((a.core.state, a.core.main_power, a.entered_ms),
                         (b.core.state, b.core.main_power, b.entered_ms))

    def test_fault_remains_latched_during_large_jump(self):
        c = self.running()
        c.command("pgood_low")
        c.advance(600000)
        self.assertEqual(State.FAULT_LOCKOUT, c.core.state)
