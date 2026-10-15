"""Compile C core and compare all canonical CSV scenarios with Python reference."""
import csv
import ctypes
import pathlib
import shutil
import subprocess
import tempfile
import unittest
from reference import Controller, State

ROOT = pathlib.Path(__file__).resolve().parents[2]
VECTORS = ROOT / "docs/engineering/m1-1-management-test-vectors.csv"
EVENTS = ["power_on", "pgood_stable", "pgood_timeout", "power_off",
          "shutdown_complete", "watchdog_timeout", "rail_fault",
          "clear_fault", "recovery", "recovery_complete",
          "min_off_elapsed", "shutdown_timeout", "power_cycle"]
STATES = ["OFF", "POWERING_ON", "RUNNING", "POWERING_OFF", "CYCLING",
          "FAULT_LOCKOUT", "RECOVERY"]
RESULTS = ["rejected", "accepted", "idempotent", "fault_recorded",
           "running", "graceful_shutdown_requested", "completed",
           "cycle_count_incremented", "lockout_latched", "rate_limited",
           "recovery_straps_selected"]

class CController(ctypes.Structure):
    _fields_ = [("state", ctypes.c_int), ("main_power", ctypes.c_bool),
                ("cycles", ctypes.c_uint32), ("max_cycles", ctypes.c_uint32)]

class ParityTests(unittest.TestCase):
    def test_csv_parity(self):
        compiler = shutil.which("cc")
        if compiler is None:
            self.fail("C compiler required for parity gate")
        with tempfile.TemporaryDirectory() as tmp:
            libpath = pathlib.Path(tmp) / "libmanagement.so"
            subprocess.run([compiler, "-std=c11", "-Wall", "-Wextra", "-Werror",
                            "-fPIC", "-shared", "-I" + str(ROOT / "firmware/management/include"),
                            str(ROOT / "firmware/management/src/pp_management.c"),
                            "-o", str(libpath)], check=True)
            lib = ctypes.CDLL(str(libpath))
            lib.pp_management_dispatch_result.argtypes = [ctypes.POINTER(CController),
                ctypes.c_int, ctypes.c_bool, ctypes.c_bool]
            lib.pp_management_dispatch_result.restype = ctypes.c_int
            with VECTORS.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(12, len(rows))
            for row in rows:
                with self.subTest(case=row["id"]):
                    state = row["initial_state"]
                    power = state in {"POWERING_ON", "RUNNING", "POWERING_OFF"}
                    cycles = 4 if row["precondition"] == "cycle_limit_exceeded" else 0
                    c = CController(STATES.index(state), power, cycles, 3)
                    py = Controller(state=State(state), main_power=power,
                                    cycles=cycles, max_cycles=3)
                    condition = row["precondition"]
                    authorized = condition in {"authorized", "authorized_and_fault_clear"}
                    clear = condition == "authorized_and_fault_clear"
                    py.event(row["event"], authorized=authorized, fault_clear=clear,
                             within_retry_limit=condition != "cycle_limit_exceeded")
                    result = lib.pp_management_dispatch_result(
                        ctypes.byref(c), EVENTS.index(row["event"]), authorized, clear)
                    self.assertEqual((py.state.value, py.main_power, py.last_result),
                                     (STATES[c.state], c.main_power, RESULTS[result]))
                    self.assertEqual((row["expected_state"], row["expected_main_power"],
                                      row["expected_result"]),
                                     (STATES[c.state], "ON" if c.main_power else "OFF",
                                      RESULTS[result]))

if __name__ == "__main__":
    unittest.main()
