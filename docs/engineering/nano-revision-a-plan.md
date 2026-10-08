# Ploos Pi Nano — Revision A engineering plan

**Status: proposal only. No SoC selected, no schematic, no PCB, no prototype.**

## Mission
Smallest economical original ARM64 headless fleet node. Target workloads: Linux services, small CI tasks, lightweight distributed compute, telemetry and management.

## Rev A design targets (subject to SoC feasibility)
- Direct-mounted bare ARM64 SoC, RAM and non-removable boot storage.
- 1 GbE RJ45; assess integrated MAC + external PHY/magnetics.
- UART console and recovery strap/test points.
- Independent low-power management MCU with watchdog, reset/power controls, telemetry.
- Board ID and hardware revision stored in nonvolatile configuration.
- Standard node power input with reverse-polarity/overcurrent protection and documented shutdown semantics.
- eMMC as preferred boot storage; SD only as recovery/development option if practical.
- Accessible power, UART, reset and programming test points.
- No display connector, audio, wireless or camera by default.
- Optional external expansion only where it does not undermine BOM, power and size goals.

## Open decisions
Exact SoC, RAM topology/capacity, eMMC vendor, PMIC and rails, Ethernet PHY, management MCU, connector, voltage, mechanical outline, layer count, thermal solution, supply chain, unit economics.

## Design deliverables
1. Requirements traceability and block diagram.
2. Selected exact SoC part number with procurement/documentation evidence.
3. DDR/PMIC/boot/reference schematic review.
4. Stack-up and impedance specification from PCB fabricator.
5. Schematic and ERC report.
6. Layout, DRC, manufacturing and assembly data.
7. Bring-up and factory test plan with pass/fail criteria.
8. Board revision log and public prototype evidence.

## Stop conditions
No verifiable chip purchase path; missing legal DDR/ballout documentation; non-redistributable critical firmware; unachievable thermal/network/power targets; no realistic assembly and test path.
