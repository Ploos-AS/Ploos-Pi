# M0.5 — Exact AM625 ordering variants and sourcing gate

Research date: 2026-10-09. **Part numbers are real manufacturer catalog entries, NOT evidence of available stock or acceptable price.**

## Manufacturer-listed examples

| Ordering code | Package | Manufacturer status | Observed availability | Reference |
|---|---|---|---|---|
| AM6254ATCGGAALW | ALW, 425-pin FCCSP | ACTIVE | TI page indicated out of stock / no price | https://www.ti.com/product/AM625/part-details/AM6254ATCGGAALW |
| AM6254ATCGHIALWR | ALW, 425-pin FCCSP | ACTIVE | TI page indicated out of stock / no price | https://www.ti.com/product/AM625/part-details/AM6254ATCGHIALWR |
| AM6254ATCGHAALW | ALW, 425-pin FCCSP | Manufacturer catalog page | Stock/price not verified | https://www.ti.com/product/AM625/part-details/AM6254ATCGHAALW |

**Important:** Ordering-code suffixes may encode temperature grade, speed, silicon revision, package or carrier. Do not interchange these without validating TI's ordering table and datasheet. ALW package is listed as 13 x 13 mm, 0.5 mm pitch on TI's AM625 page; this makes BGA escape routing/assembly review essential.

## Manufacturer-supported capabilities (family-level only)
- Up to four Cortex-A53 cores at 1.4 GHz.
- DDR4/LPDDR4 controller, 16-bit bus; documented address limits differ by memory type.
- Gigabit Ethernet ports; external PHY/magnetics and pin multiplexing need verification.
- eMMC and multiple recovery boot options.
- TI lists hardware design guidance and Linux software resources.

Sources: https://www.ti.com/product/AM625 and https://www.ti.com/lit/ds/symlink/am625.pdf

## Explicit exclusions / cautions
- AM625SIP variants integrate LPDDR4 in the chip package; these are **not compute modules**, but may not satisfy the project's preferred direct RAM component architecture. Treat as separate ADR question, not a silent substitute.
- Do not assume the internal M4F MCU can perform power cycling independently of the main SoC's power domain.
- DDR inline ECC and CPU cache ECC are not a blanket claim of full system ECC or guaranteed application-level memory protection.
- AM625 is not a verified 2.5GbE/10GbE solution and is under evaluation for **Nano**, not automatically Compute/Pro.

## Procurement questions (open)
1. Dated distributor quotes for 10, 100 and 1000 chips; currency, MOQ, lead time and PCN/EOL terms.
2. Exact order code chosen from TI's part-number legend and application temperature requirements.
3. Authorized supplier evidence and sample procurement route.
4. DDR/PMIC/PHY compatibility reviewed against selected code.
5. Full landed board-cost estimate after EMS, fabrication, testing and fulfillment.

**Gate outcome: HOLD.** Product codes and manufacturer specifications confirmed, but supply and production suitability remain unproven.
