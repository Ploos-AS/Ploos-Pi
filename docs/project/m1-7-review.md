# M1.7 — Fault journal codec (2026-10-12)

Added a bounded, versioned fault-record codec, CRC32 validation, selection of latest valid slot, eight regression tests, and a hardware-independent persistence contract.

**Evidence status:** code committed; test execution and GitHub CI status not independently verified. No flash/EEPROM writes or MCU reset persistence have been demonstrated.

Next: run full test suite and repair failures, integrate fault recording with state transitions, define storage atomicity and endurance before embedded C port.
