# Ploos Pi Nano — KiCad workspace (M0.8)

**Exploratory project only. Not a functional schematic, PCB, fabrication package or prototype.**

Open `Ploos-Pi-Nano.kicad_sch` in KiCad 9. The root schematic is intentionally empty until an exact SoC and its authoritative pinout/DDR and power documentation are qualified. Do not fabricate from this directory.

## Intended schematic hierarchy (not yet drawn)
- 01-power-input
- 02-soc-clocks-boot
- 03-ddr
- 04-pmic-rails
- 05-emmc-recovery
- 06-ethernet-phy
- 07-management-mcu
- 08-debug-connectors
- 09-testpoints-mechanical

Each sheet will be added after the applicable hardware review. We explicitly avoid fake electrical connections, unverified footprints and a misleading populated schematic.

## Working design identifier
PPI-NANO-REV-A (planning identifier only).

## Release gates
1. Exact purchasable bare SoC selected and its package drawing checked.
2. RAM topology, DDR routing and PMIC sequencing reviewed.
3. PHY, storage, independent management and power-input requirements reviewed.
4. KiCad ERC/DRC and independent electrical review.
5. Fabricator stackup and assembly DFM sign-off.
6. Versioned BOM, test plan, design history and release evidence.

See [KiCad readiness](../../docs/engineering/m0-7-kicad-readiness.md) and [Nano architecture](../../docs/engineering/m0-7-nano-component-architecture.md).
