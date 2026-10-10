import unittest
from timed import TimedController, Timing
from reference import State

class TimedTests(unittest.TestCase):
    def test_pgood_timeout(self):
        c = TimedController()
        c.command("power_on", authorized=True)
        self.assertEqual(c.advance(1000), State.FAULT_LOCKOUT)

    def test_boot_grace(self):
        c = TimedController()
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        self.assertEqual(c.advance(4999), State.POWERING_ON)
        self.assertEqual(c.advance(1), State.RUNNING)

    def test_shutdown_timeout(self):
        c = TimedController()
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        c.command("power_off", authorized=True)
        self.assertEqual(c.advance(10000), State.OFF)

    def test_watchdog_and_min_off(self):
        c = TimedController()
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        self.assertEqual(c.advance(3000), State.CYCLING)
        self.assertFalse(c.core.main_power)
        self.assertEqual(c.advance(500), State.POWERING_ON)

    def test_retry_window(self):
        c = TimedController(config=Timing(max_cycles=2))
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        self.assertEqual(c.command("power_cycle", authorized=True), State.CYCLING)
        c.advance(500)
        c.command("pgood_high")
        c.advance(5000)
        self.assertEqual(c.command("power_cycle", authorized=True), State.CYCLING)
        c.advance(500)
        c.command("pgood_high")
        c.advance(5000)
        self.assertEqual(c.command("power_cycle", authorized=True), State.FAULT_LOCKOUT)

    def test_invalid_time(self):
        c = TimedController()
        with self.assertRaises(ValueError):
            c.advance(-1)
        with self.assertRaises(ValueError):
            Timing(min_off_ms=0)
