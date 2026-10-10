"""M1.5 regressions: authorization must not mutate retry state."""
import unittest
from timed import TimedController
from reference import State

class AuthorizationRegressions(unittest.TestCase):
    def test_unauthorized_power_on_preserves_retry_history(self):
        c = TimedController()
        c.retry_times[:] = [1, 2]
        c.core.cycles = 2
        c.command("power_on", authorized=False)
        self.assertEqual(State.OFF, c.core.state)
        self.assertEqual([1, 2], c.retry_times)
        self.assertEqual(2, c.core.cycles)

    def test_authorized_power_on_resets_retry_history(self):
        c = TimedController()
        c.retry_times[:] = [1, 2]
        c.core.cycles = 2
        c.command("power_on", authorized=True)
        self.assertEqual(State.POWERING_ON, c.core.state)
        self.assertEqual([], c.retry_times)
        self.assertEqual(0, c.core.cycles)

    def test_unauthorized_cycle_does_not_consume_retry_budget(self):
        c = TimedController()
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        c.command("power_cycle", authorized=False)
        self.assertEqual(State.RUNNING, c.core.state)
        self.assertEqual([], c.retry_times)
