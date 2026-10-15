"""M2.4: bounded cross-language state/event equivalence and safety invariants."""
import ctypes
import pathlib
import shutil
import subprocess
import tempfile
import unittest

from reference import Controller, State
from test_c_parity import CController, EVENTS, RESULTS, STATES

ROOT = pathlib.Path(__file__).resolve().parents[2]

class ExhaustiveParityTests(unittest.TestCase):
    def test_state_event_matrix(self):
        compiler = shutil.which("cc")
        if compiler is None:
            self.fail("C compiler required for safety parity gate")
        with tempfile.TemporaryDirectory() as tmp:
            library = pathlib.Path(tmp) / "libmanagement.so"
            subprocess.run([compiler, "-std=c11", "-Wall", "-Wextra", "-Werror",
                            "-fPIC", "-shared",
                            "-I" + str(ROOT / "firmware/management/include"),
                            str(ROOT / "firmware/management/src/pp_management.c"),
                            "-o", str(library)], check=True)
            c_lib = ctypes.CDLL(str(library))
            c_lib.pp_management_dispatch_result.argtypes = [
                ctypes.POINTER(CController), ctypes.c_int, ctypes.c_bool, ctypes.c_bool]
            c_lib.pp_management_dispatch_result.restype = ctypes.c_int
            count = 0
            for state in STATES:
                for event in EVENTS:
                    for authorized in (False, True):
                        for fault_clear in (False, True):
                            for cycles in (0, 3, 4):
                                with self.subTest(state=state, event=event,
                                                  authorized=authorized, fault_clear=fault_clear,
                                                  cycles=cycles):
                                    power = state in ("POWERING_ON", "RUNNING", "POWERING_OFF")
                                    py = Controller(state=State(state), main_power=power,
                                                    cycles=cycles, max_cycles=3)
                                    c = CController(STATES.index(state), power, cycles, 3)
                                    py.event(event, authorized=authorized, fault_clear=fault_clear)
                                    result = c_lib.pp_management_dispatch_result(
                                        ctypes.byref(c), EVENTS.index(event), authorized, fault_clear)
                                    self.assertEqual((py.state.value, py.main_power, py.cycles, py.last_result),
                                                     (STATES[c.state], c.main_power, c.cycles, RESULTS[result]))
                                    if c.state in (0, 4, 5, 6):
                                        self.assertFalse(c.main_power)
                                    count += 1
            self.assertEqual(7 * 13 * 2 * 2 * 3, count)
