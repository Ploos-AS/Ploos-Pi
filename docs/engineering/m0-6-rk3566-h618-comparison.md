# M0.6 — RK3566 versus H618 for Nano

Research date: 2026-10-09. **Source-supported family capabilities only. No part qualified, no prices/stock verified.**

| Property | Rockchip RK3566 | Allwinner H618 |
|---|---|---|
| Manufacturer page | https://www.rock-chips.com/a/en/products/RK35_Series/2021/0113/1274.html | https://www.allwinnertech.com/index.php?a=index&c=product&id=89 |
| CPU | 4× Cortex-A55 | 4× Cortex-A53 |
| DDR | DDR3/DDR3L/DDR4/LPDDR3/LPDDR4/LPDDR4X | DDR3/DDR3L/LPDDR3/DDR4/LPDDR4 |
| Ethernet | Gigabit MAC listed in Rockchip brief datasheet | GMAC listed in manufacturer specification |
| High-speed I/O | PCIe 2.1 / SATA 3.0 / USB 3.0 combo resources in brief datasheet; lane sharing requires review | Manufacturer H618 page lists USB 2.0, SDIO and GMAC; PCIe not listed |
| Boot storage | eMMC 5.1 in Rockchip brief datasheet | Manufacturer page does not establish eMMC boot; **HOLD** |
| Software | Rockchip brief datasheet lists Linux SDK | Allwinner manufacturer page lists Android; Linux viability must be proven separately |
| Documentation | Official brief datasheet linked from Rockchip download center | Official product specification PDF published |
| Bare-chip procurement | UNKNOWN | UNKNOWN |
| Layout/DDR/PMIC design guides and legal access | UNKNOWN | UNKNOWN |
| Pricing / MOQ / lead time | UNKNOWN | UNKNOWN |
| Power / thermal under Ploos workloads | UNKNOWN | UNKNOWN |

## Primary references
- Rockchip official RK3566 page: https://www.rock-chips.com/a/en/products/RK35_Series/2021/0113/1274.html
- Rockchip official downloads index: https://www.rock-chips.com/a/en/download/index.html
- Allwinner official H618 page: https://www.allwinnertech.com/index.php?a=index&c=product&id=89
- Allwinner H618 specification PDF: https://www.allwinnertech.com/uploads/download_source/20260303162657a4.pdf

## Engineering assessment
RK3566 is **provisionally more promising** for a general-purpose headless Nano due to documented Cortex-A55, eMMC and PCIe-class connectivity. This is an *engineering hypothesis*, not a selection or price/performance conclusion.

H618's multimedia-focused feature set does not itself invalidate it for headless Linux; however, manufacturer-listed interfaces and OS support leave more questions about boot storage, upstream Linux and future expandability. Do not assert PCIe is physically absent until the full technical reference manual is reviewed.

TI AM625 remains a candidate because of its publicly available integration guidance. All three remain **HOLD** until exact orderable variants, supplier quotations and legal board-design documentation are established.

## Next gate
Request exact orderable part numbers and authorized bare-chip purchasing options for RK3566 and H618; seek DDR, PMIC, ballout, reference schematic and firmware redistribution terms. Record all supplier replies with date, quantity and confidentiality constraints. Do not populate missing figures with board retail prices.
