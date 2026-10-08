# Engineering verification, validation and traceability

## Requirement traceability
Every requirement ID from product-family.md must map to: design location, test procedure, expected threshold, measured result, sample/board revision, operator, date and raw evidence link.

## Prototype gates
1. Power: safe rails, sequencing, startup/inrush, off-state consumption, protection and fault behavior.
2. Clocks, JTAG/UART, boot straps and emergency recovery.
3. DDR init and extended stress with temperature variation.
4. eMMC/NVMe integrity and repeated power-loss recovery.
5. Network link interoperability and sustained traffic under load.
6. Thermal soak, throttling data, fan/fanless envelopes.
7. Management watchdog, brown-out, reset and power cycle recovery.
8. 24/7 endurance, failure logging, physical serviceability.
9. Pre-compliance EMC/ESD and relevant regulatory review.
10. Factory test fixture coverage, serial traceability, production yield.

## Evidence discipline
Record instruments/calibration, test setup, board/firmware revision, scripts, raw outputs and failure modes. Failed tests remain public with follow-up actions. Benchmark reports must distinguish measured performance from targets.

## Release blockers
Unresolved safety hazards, boot instability, unknown BOM lifecycle, inaccessible test records, uncertain radio/EMC requirements, undocumented binary redistribution, missing firmware recovery and unproven manufacturing test coverage.
