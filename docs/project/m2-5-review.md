# M2.5 — Fault-sequence regression tests

Date: 2026-10-15.

Added four deterministic host-side end-to-end tests: watchdog restart followed by retry lockout; PGOOD loss while running; journal write failure during startup timeout; and refusal to clear a fault without fault-clear confirmation.

**Verification:** Test code committed, but full test results not confirmed. Attempted to clone the repository in the execution container; GitHub DNS resolution failed. These tests exercise simulated logical power only. They do not validate real brownouts, physical watchdogs, MCU firmware, rail switching or persistent storage.

Next: inspect GitHub Actions results, fix failures, add timing edge cases and physical fault-injection plan.
