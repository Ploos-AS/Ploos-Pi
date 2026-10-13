# M2.1 — C state-machine vector coverage

Date: 2026-10-13.

Added a C11 table-driven test mirroring all twelve M1.1 CSV scenarios, checking expected state, logical power and command acceptance. Updated the Makefile to run both the original smoke test and the vector test.

**Important limitations:** The C test cases are copied from the CSV, not dynamically parsed; the C API does not expose the Python `expected_result` outcome strings, so this is **partial parity**, not full equivalence. SM-012 sets cycles greater than max to represent the external `cycle_limit_exceeded` precondition. Neither Python CI nor C CI has been independently verified green. Hardware timing, NVM, authorization and MCU behavior are still out of scope.

Next: verify tests, introduce explicit outcome codes and generate tests from the CSV to eliminate drift.
