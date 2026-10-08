# M0.4 — TI AM625 primary-source evidence review

Review date: 2026-10-09. **Status: PARTIAL EVIDENCE, procurement and engineering approval HOLD.**

## Manufacturer sources
- Product page: https://www.ti.com/product/AM625
- Manufacturer datasheet: https://www.ti.com/lit/ds/symlink/am625.pdf

The product page lists:
- Up to four Cortex-A53 cores at up to 1.4 GHz, plus integrated MCU functions.
- DDR4/LPDDR4 memory subsystem; validate exact density and topology for chosen part.
- Ethernet networking, MMC/eMMC boot and Linux support.
- Recommended TPS65219 PMIC family.
- Published technical reference manual, hardware design considerations, DDR board design/layout guidelines, schematic review checklist, PCB escape routing and errata.

## Evidence status by gate
| Gate | Evidence | Status |
|---|---|---|
| Public product datasheet | Manufacturer product page and linked datasheet | PARTIAL PASS: family documentation identified |
| DDR/layout guidance | Manufacturer lists DDR design/layout guide | PARTIAL PASS: document exists, exact variant review pending |
| Power design guidance | Manufacturer lists TPS65219 and PMIC guidance | PARTIAL PASS: design integration pending |
| Boot/Linux | TI product page lists Linux and boot interfaces | PARTIAL PASS: exact BSP, source licenses and board bring-up unverified |
| Ethernet | Family supports Gigabit Ethernet | PARTIAL PASS: exact pin mux/PHY topology unverified |
| Orderable part / price / MOQ | No dated quote collected | HOLD |
| Thermal/power | No Ploos board measurements | HOLD |
| EMS/BGA/stackup | No fabrication review | HOLD |
| Legal/firmware | No complete redistribution review | HOLD |

## Important limitations
- Product family capabilities are not necessarily present on every orderable SKU.
- Manufacturer documentation availability does not prove an authorized distributor will supply the selected part at an acceptable price or MOQ.
- Integrated MCU does **not** automatically replace an independently powered external management controller; assess its power domain and recovery limitations.
- The AM625 is a **Nano candidate**, not a selected Ploos Pi processor.
- No claims of ECC RAM, 2.5GbE, 10GbE, NVMe or hot swap are established by this review.

## Next evidence requests
1. Record exact TI ordering code, package and variant, with product-page link.
2. Obtain distributor pricing and stock/lead-time evidence at 10/100/1000 quantities.
3. Map DDR4/LPDDR4 devices and power rails to official hardware guidelines.
4. Identify exact Linux boot chain, mandatory firmware binaries and licenses.
5. Commission fabrication/assembly feasibility review before KiCad routing.
