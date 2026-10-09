# M1 — Nano schematic review checklist

**No electrical signoff yet.** Use this checklist for each sheet and capture reviewer, date, revision, source documents and deviations.

## 01 Input and management always-on supply
- Input voltage range and transient protection sourced from actual requirements.
- Input reverse polarity, surge, ESD, overcurrent and brownout considered.
- Independent always-on rail verified under main-rail faults.
- Reset and power-enable safe defaults documented.
- Thermal and worst-case current budget calculated.

## 02 SoC, boot, clocks
- Exact SoC order code and ball map independently checked.
- Clock crystals/oscillators, reset timing and boot straps verified.
- Recovery straps and UART accessible without Linux.
- All unused pins treated per manufacturer's recommendations.

## 03 DDR
- Approved memory vendor and part number; density and bus topology.
- Reference-design layout constraints, impedance, length matching and VREF/termination.
- DDR rail sequence, training firmware and test strategy.

## 04 PMIC
- Correct sequencing for SoC, DDR, I/O, PHY and eMMC.
- Peak and transient currents with margin.
- Power-good, reset and fault logic checked across voltage domains.

## 05 eMMC and recovery
- eMMC part, voltage modes and boot support checked.
- Reflash/recovery accessible in production and field.
- Write-protect and reset behavior reviewed.

## 06 Ethernet
- PHY compatibility, strap resistors, clocks, RGMII delays, ESD and magnetics.
- RJ45 grounding/chassis strategy and EMI considerations.
- Link, throughput and error test criteria.

## 07 Management
- Independent power domain and safe fallback.
- Host UART/I2C voltage translation, isolation and no back-power.
- Watchdog, fault logging, secure update and hardware recovery.

## 08 Manufacturing and release
- Footprints/3D models sourced and licensed.
- Fabricator-approved stackup and BGA escape.
- ERC, DRC, peer review and controlled revision recorded.
- Testpoint access, factory flashing and production test fixture defined.
- No fabrication files released before all critical findings close.
