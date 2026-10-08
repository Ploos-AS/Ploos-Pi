# M0.7 — Nano preliminary component architecture

Status: **PROPOSED / NOT APPROVED**. This is not a schematic or bill of materials.

## Two alternative implementation tracks

| Block | Track A: TI AM625 | Track B: Rockchip RK3566 |
|---|---|---|
| SoC | Exact AM6254 orderable SKU TBD | Exact RK3566 orderable SKU TBD |
| Memory | External DDR4 or LPDDR4, topology per TI design guide | External DDR4 or LPDDR4, topology per Rockchip design guide |
| Power | TPS65219 variant selected by rail/current/sequencing review | RK817-5 reference option, subject to documentation/availability review |
| Ethernet | CPSW3G MAC, RGMII PHY, magnetics, RJ45 | GMAC and compatible PHY, pin mux/clock review |
| Boot | eMMC with recovery/UART paths | eMMC with recovery/UART paths |
| Management | Independently powered MCU, family TBD | Same functional requirement |
| Power input | Protected DC input, voltage TBD | Same requirement |

**No components are interchangeable merely because they appear in this table.** Exact PMIC variants and DDR part numbers must be derived from selected SoC reference documentation and rail budgets.

## Verified manufacturer guidance for Track A
- TI AM625 product and design document index: https://www.ti.com/product/AM625
- TI AM625 schematic guidelines and checklist: https://www.ti.com/lit/pdf/sprado3
- TI TPS65219 product and PMIC application notes: https://www.ti.com/product/TPS65219
- TI documents describe CPSW3G with two external Ethernet ports and RGMII/RMII interfaces; Nano may populate only one port. Pin multiplexing and PHY supply compatibility require schematic review.

## Track B evidence caution
Rockchip RK3566 hardware design guides describe RK817-5 reference power arrangements, but publicly mirrored documents may have redistribution restrictions. **Do not copy third-party confidential reference schematics into this repository.** Seek authorized vendor documentation and check license terms.

## Shared management MCU criteria
Independent always-on supply; programmable watchdog; I2C/UART or equivalent; adequate GPIO for power-enable, reset, fault and boot straps; firmware update/recovery; documented toolchain; long-term availability; measured standby consumption. Select exact MCU only after a pin/resource budget and management threat model.

## Electrical signoff blockers
- SoC exact ordering code, ballout and DDR timing/layout rules.
- PMIC sequencing and peak rail-current requirements.
- PHY/RGMII timing, magnetics and ESD design.
- Boot straps and recovery accessibility.
- Controlled-impedance stackup and EMS BGA capability.
- Independent management power-domain behavior.
- Sourcing and per-unit costs.

Next: source-specific schematic worksheet and manufacturing DFM review, not speculative routing.
