# M1.4 — Clock-driven management simulation (2026-10-10)

Added `software/management/timed.py` and six unit tests for configurable PGOOD timeout, boot grace, shutdown grace, minimum off-time, heartbeat timeout and bounded retry window. Time is injected by `advance(ms)`; no real sleeps or GPIO.

The six test scenarios were exercised locally against a **temporary stand-in** for the legacy controller, not the actual repository implementation. Therefore repository-integrated tests and GitHub CI must still be verified. Timing values are simulation examples, **not approved hardware values**.

Known gaps: coarse time-step simulation can skip intermediate deadlines; PGOOD-high is a software event, not debounced or validated hardware feedback; retries and persistent fault accounting need stronger design; security and firmware are not implemented. This code must not be used to control real hardware.

Next: verify full suite against the repository's real `reference.py`, inspect CI and resolve integration defects, then refine event scheduling before C port.
