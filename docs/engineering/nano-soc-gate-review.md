# M0.3 — Nano SoC hard-gate review

Status: **HOLD — no approved SoC**. This is a decision framework, not an assertion of current stock or prices.

## Comparison scope
Evaluate exact orderable variants of Rockchip RK3566, Allwinner H618/H616, and TI AM625x (as a possible industrial alternative). Do not conflate family names with specific package/pinout/feature variants. A development board is not a substitute for a purchasable bare chip.

## Mandatory gates
| Gate | Required evidence | Fail/Hold policy |
|---|---|---|
| G1 Procurement | authorized supplier quotation, MOQ, lifecycle, sample availability | HOLD without dated written evidence |
| G2 Integration docs | legally accessible ball map, reference schematics, DDR routing, power sequencing | STOP if unavailable |
| G3 Boot and Linux | boot ROM path, recovery method, maintained kernel/U-Boot and redistributable binaries | HOLD until proven |
| G4 Network | documented 1GbE MAC/PHY topology, magnetics, drivers | HOLD if not demonstrated |
| G5 Memory/storage | RAM type/topology, eMMC boot, testable layout rules | HOLD until review |
| G6 Manufacture | BGA pitch, layer/HDI requirements, EMS X-ray/rework feasibility | HOLD pending EMS review |
| G7 Power/thermal | voltage/current rails, idle/load estimate backed by references | HOLD pending budget |
| G8 Legal | licensing and export/market constraints assessed | HOLD pending review |

## Review order
1. Ask vendors for datasheet revision, hardware design guide and authorized distribution contacts.
2. Validate each gate with dated references; record public vs NDA evidence separately.
3. Reject infeasible parts before assigning weighted scores.
4. Compare candidates with Nano workloads and quantity-specific *landed* costs.
5. Publish ADR for selected part or HOLD decision with remaining unknowns.

## Important distinction
A vendor product page showing a development board or an ARM CPU family is **not** proof that an individual chip can be ordered at acceptable MOQ, nor that the hardware design guide may be redistributed.
