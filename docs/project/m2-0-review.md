# M2.0 — First portable C management core

Date: 2026-10-13.

Added an MCU-agnostic C11 state machine, public header, smoke test, Makefile and documentation. It supports authorized power-on/off, PGOOD, watchdog retry limit, rail fault lockout, recovery and guarded fault clearing.

**Scope:** preliminary C port only; no claim of Python/C behavioral parity or physical validation. Timing, event authentication, NVM journal, hardware drivers and production safety logic remain open. Full Python suite and GitHub CI status are not independently verified.

Next: run and verify C smoke tests in CI, build CSV-driven equivalence harness and resolve policy discrepancies before MCU selection.
