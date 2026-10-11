# M1.6 — Power-good failure and deadline stepping

Date: 2026-10-11.

Changes:
- `pgood_low` while RUNNING invokes the core's rail fault path, which disables logical main power and enters FAULT_LOCKOUT.
- `advance(ms)` now processes intermediate deadlines for POWERING_ON, POWERING_OFF, CYCLING and RUNNING rather than evaluating only the final timestamp.
- Added four regression tests for fault latching and time-step invariance.

**Status:** Changes committed; local/CI test execution is not verified. No physical PGOOD input or rail disconnect has been tested. Simulation parameters are illustrative.

**Unresolved:** durable fault log across MCU reset, PGOOD debounce, hardware brownout behavior, authorization integration and selected MCU. Time-step simulation still requires comprehensive fuzzing and state-machine review before use as embedded firmware.
