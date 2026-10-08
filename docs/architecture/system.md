# System architecture — conceptual

```text
  Dedicated ARM64 SoC -- DDR memory
        |     |    |
     eMMC   PCIe  Ethernet MAC/PHY
        |     |    |
       boot NVMe  network
        |
  PMIC / power rails / sequencing
        |
  Independent management controller
        |-- watchdog and reset request
        |-- regulated power-enable and fault reporting
        |-- temperature/current/voltage telemetry
        |-- recovery request and serial console path
        |
  Standardized external management/power interface (TBD)
```

Each SKU will have its **own PCB**; commonality should focus on management protocol, manufacturing test conventions, connector definitions and mechanical philosophy, not an assumed single PCB for every SKU.

## Boundaries
A management microcontroller must remain useful when the ARM OS hangs. Provide secure boot/recovery pathways and avoid allowing an exposed management bus to directly compromise production nodes. Management must have authenticated remote control when network-accessible.

## Design reviews needed
SoC documentation rights, BGA footprint availability, DDR routing/length matching, layer count, impedance stack-up, PCIe budget, PHY magnetics/isolation, power transients, oscillator/jitter, thermals and RF/EMC.

## Backplane
Reserve a common node-management abstraction before choosing physical connectors. A backplane may provide power distribution, per-slot isolation and monitoring; do not claim hot-swap support without engineered connector sequencing, inrush protection and validation.

## Firmware
Prefer upstreamable U-Boot/EDK2/Linux support where feasible, with signed/verified upgrades as a later requirement to evaluate. Record all binary dependencies and redistribution rights.

## Interfaces
Provisional management API concepts: inventory, health, temperatures, power consumption, power-on/off/cycle, reset, boot source, serial console and firmware revisions. Specify authentication and fail-safe semantics before implementation.
