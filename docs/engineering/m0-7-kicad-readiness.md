# M0.7 — KiCad project readiness checklist

No validated schematic or PCB exists. Do not label placeholders as manufacturing-ready.

## Proposed hierarchy
00_top; 01_power_input; 02_soc_boot_clocks; 03_ddr; 04_pmic; 05_emmc_recovery; 06_ethernet; 07_management; 08_debug_connectors; 09_mechanical_testpoints.

## Before symbol/footprint approval
- Obtain authoritative ball map and package drawing for exact orderable SoC.
- Check pin numbering and footprint land pattern against manufacturer drawing, independently.
- Record source/revision/license for each symbol, footprint and 3D model.
- Lock memory topology and length/skew constraints before layout.
- Get fabricator stackup, impedance and via-in-pad capabilities in writing.
- Perform ERC, DRC, schematic peer review, power-sequencing review and assembly DFM.
- Export versioned BOM, netlist, fabrication outputs and testpoint map only after review.

## Naming and traceability
Use `PPI-NANO-REV-A` as *working design identifier*, not a built product revision. Attach requirement IDs and review records to design commits. Maintain a revision history and ECO record.

## Gate
KiCad files may be created for exploration, but **no fabrication release** until component qualification and independent electrical review pass.
