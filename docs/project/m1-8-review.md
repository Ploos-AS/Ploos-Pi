# M1.8 — Fault journal connected to management simulation

Date: 2026-10-12.

Added `LoggedController`, a host-side wrapper subclass of `TimedController` that records selected state transitions as encoded fault records in an **in-memory list**. Covers PGOOD loss, PGOOD timeout, watchdog cycling, retry lockout and shutdown timeout. Six regression tests cover fault capture, duplicate suppression, unauthorized events and sequence recovery from caller-supplied slots.

**Limitations:** No physical storage, MCU reset survival, flash driver, wear leveling or atomic commit. Passing an existing list of encoded slots to a newly constructed controller simulates a restart, but is not actual persistence. No full CI test results verified. Sequence overflow raises an error; a real firmware implementation needs a rollover policy. A failed journal write is not modeled and must never prevent emergency rail shutdown.

Next: verify full test suite in CI; add explicit storage interface and fault-injection tests; review state transitions and authorization; then begin C port.
