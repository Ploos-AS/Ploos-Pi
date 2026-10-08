# Product family requirements (proposed)

All numbers below are **aspirational, unvalidated targets**.

| ID | Requirement | Nano | Compute | Pro | Verification |
|---|---|---|---|---|---|
| SYS-001 | Original board with bare ARM64 SoC (no SoM) | must | must | must | schematic/BOM inspection |
| SYS-002 | Headless Linux operation | must | must | must | repeatable boot/system tests |
| SYS-003 | UART console and recoverable boot | must | must | must | fault injection |
| SYS-004 | Hardware watchdog | must | must | must | hang/reset test |
| SYS-005 | Dedicated controlled power/reset interface | must | must | must | management test |
| SYS-006 | Telemetry for temperature/power | must | must | must | calibrated measurements |
| SYS-007 | eMMC primary boot/storage option | goal | goal | goal | image/boot endurance |
| NET-001 | Ethernet | 1 GbE | 2.5 GbE | 10 GbE | measured throughput |
| MEM-001 | RAM capacity | 2–4 GB | 8–16 GB | 16–32+ GB | memory stress |
| CPU-001 | ARM64 cores | 4 | 8 | 8–16 | hardware inventory |
| STOR-001 | NVMe | optional | goal | goal | enumeration/IO tests |
| MECH-001 | Rack-friendly interface | must | must | must | fit/electrical tests |
| OPS-001 | 24/7 fleet use and managed recovery | goal | goal | goal | endurance/recovery tests |

## Constraints and open questions
Clock speeds, ECC, PoE, 10GbE PHY choice, PMIC, SoC availability, RAM topology, power envelopes, board dimensions, backplane connector and unit prices are **TBD**. Support for Debian/Ubuntu requires verified board support; distribution naming alone does not establish compatibility.

## Performance methodology
Publish ambient temperature, PSU, memory/storage/network conditions, kernel/bootloader revisions, sustained load duration, measured wall power and confidence intervals; no cherry-picked peak-only benchmarks.
