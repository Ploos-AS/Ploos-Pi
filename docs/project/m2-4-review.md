# M2.4 — State/event parity expansion

Added `test_c_exhaustive.py`, a bounded 1,092-case cross-language matrix covering all seven states, thirteen events, both authorization values, both fault-clear values, and three retry counts (0, 3, 4). Compares state, power, retry count and result code, and asserts rail-off invariants in OFF, CYCLING, FAULT_LOCKOUT and RECOVERY.

The test uses a temporary shared C library compiled by the host compiler, so it runs within the existing management-parity GitHub Actions workflow.

**Not yet verified:** CI passing. A local clone attempt failed because GitHub DNS could not resolve. This is a bounded model parity test, not MCU firmware validation. Timing, power-loss resilience, hardware electrical design and real authentication remain unverified.

Any failing parity case should be resolved against the documented management specification, not by weakening safety assertions.
