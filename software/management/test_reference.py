"""Run with: python3 -m unittest discover -s software/management -p 'test_*.py'"""
import csv
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from reference import Controller, State

ROOT = pathlib.Path(__file__).resolve().parents[2]
VECTORS = ROOT / "docs/engineering/m1-1-management-test-vectors.csv"

class VectorTests(unittest.TestCase):
    def test_specification_vectors(self):
        with VECTORS.open(newline="", encoding="utf-8") as handle:
            vectors = list(csv.DictReader(handle))
        self.assertEqual(12, len(vectors))
        for row in vectors:
            with self.subTest(vector=row["id"]):
                c = Controller(state=State(row["initial_state"]),
                               main_power=row["initial_state"] in {"POWERING_ON", "RUNNING", "POWERING_OFF"})
                if row["id"] == "SM-012":
                    c.cycles = c.max_cycles
                conditions = row["precondition"]
                c.event(row["event"],
                        authorized=conditions in {"authorized", "authorized_and_fault_clear"},
                        fault_clear=conditions == "authorized_and_fault_clear",
                        within_retry_limit=conditions != "cycle_limit_exceeded")
                self.assertEqual(row["expected_state"], c.state.value)
                self.assertEqual(row["expected_main_power"], "ON" if c.main_power else "OFF")
                self.assertEqual(row["expected_result"], c.last_result)

    def test_unprivileged_power_on_rejected(self):
        c = Controller()
        c.event("power_on")
        self.assertEqual((State.OFF, False, "rejected"), (c.state, c.main_power, c.last_result))

    def test_happy_path(self):
        c = Controller()
        c.event("power_on", authorized=True)
        c.event("pgood_stable")
        self.assertEqual(State.RUNNING, c.state)
        c.event("power_off", authorized=True)
        c.event("shutdown_complete")
        self.assertEqual((State.OFF, False), (c.state, c.main_power))

if __name__ == "__main__":
    unittest.main()
