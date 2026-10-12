# M1.9 — Pluggable fault-journal storage (2026-10-12)

Introduced a `JournalStorage` protocol and an in-memory `MemoryStorage` implementation with injectable write failure. `LoggedController` can use an external storage object or its original `slots` list for compatibility. Journal append failures are counted and must never prevent fault lockout or rail-off transitions.

Four tests cover shared storage between simulated controller instances, injected append failure during PGOOD timeout and rail fault, and compatibility with M1.8.

**Not validated:** CI results, flash/EEPROM/FRAM durability, atomic commits, brownout resilience and actual MCU integration. A new controller sharing the same in-memory storage is a simulated restart only.

Next: run full test suite, fix any failures, define NVM commit semantics and choose MCU/storage based on endurance and brownout measurements.
