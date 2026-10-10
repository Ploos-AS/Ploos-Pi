# M1.5 — Authorization and retry accounting fix (2026-10-10)

Fixed an authorization flaw in `TimedController.command`: unauthenticated `power_on` while OFF no longer clears retry history or the legacy counter. Added regression tests for unauthorized and authorized commands.

This is a targeted code change, **not** a verified green CI run or full timing model qualification. Known limitations remain: large `advance` increments skip intermediate timer boundaries, `pgood_low` during RUNNING does not trigger an immediate fault, no real GPIO or MCU integration, and no persistent retry journal. These must be addressed before firmware or hardware use.
