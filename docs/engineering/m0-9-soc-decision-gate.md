# M0.9 — Nano SoC decision gate (decision record, not selection)

Date: 2026-10-09. Status: **BLOCKED — no SoC qualified for schematic capture**.

## Candidates
- TI AM6254 (exact ordering suffix pending)
- Rockchip RK3566 (exact ordering code pending)
- Allwinner H618 (exact ordering code pending)

## Minimum entry evidence (must be attached per candidate)
| Gate | Required evidence | Current disposition |
|---|---|---|
| Orderable bare SoC | Exact SKU, authorized distributor or manufacturer channel, dated quote at 10/100/1000 | HOLD for all |
| Pinout | Manufacturer-controlled full pin map, package mechanical drawing, document revision and usage rights | HOLD for all |
| DDR | Approved memory device/topology, routing constraints, reference design access | HOLD for all |
| Power | Voltage/current rails, sequencing, brownout/recovery, PMIC compatibility | HOLD for all |
| Boot | Publicly reproducible boot from eMMC and recovery, Linux kernel and bootloader status | HOLD for all |
| Networking | PHY interface, pin mux, clocks, RGMII timing, gigabit throughput plan | HOLD for all |
| Manufacturing | BGA escape, stackup, PCB/EMS capability and expected yield | HOLD for all |
| Compliance | Redistributable firmware/toolchain and source/redistribution obligations | HOLD for all |
| Economics | Landed BOM plus assembly/test cost and supply-risk alternatives | HOLD for all |

## Decision rules
1. **Do not vote by core count alone.** Prioritize documentation, sourcing, Linux maintenance and feasible board assembly.
2. An official public product page is *not* a substitute for full design files and supply confirmation.
3. A chip present on a retail development board is *not* proof of standalone SoC availability.
4. Do not copy leaked/NDA schematics or pin maps into a public repository.
5. Only after every hard gate passes: write an ADR identifying exact order code, document revisions, dissenting tradeoffs and signoff.
6. Keep the other two candidates documented as fallbacks.

## First electrical design after approval
- Verify input protection and independently powered management rail against the chosen PMIC sequence.
- Establish power-tree spreadsheet with source-based min/typ/max current, thermal estimates and margin.
- Import or create reviewed KiCad symbols/footprints from authorized documentation.
- Wire boot/recovery first, then DDR, then Ethernet; check ERC after each sheet.

See `hardware/nano/README.md` for the exploratory KiCad workspace.
