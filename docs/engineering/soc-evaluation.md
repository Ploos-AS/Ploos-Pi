# Bare SoC selection and scoring template

**Only discrete, purchasable ARM64 SoCs qualify**. Development boards can aid comparison but are not the final platform.

## Candidate capture
For each candidate record manufacturer, exact ordering PN, lifecycle status, distributor/authorized channel, MOQ, unit costs at 10/100/1000, lead times, public/NDA docs, package, DDR types/topologies, boot ROM, bootloader, kernel patches/upstream state, ethernet MAC speeds, PCIe lane/speed, PMIC reference, power/thermal data, longevity statements, licensing restrictions and known errata.

## Gate 0: eliminate
Reject (or hold pending evidence) if purchase path unavailable, legal documentation access impossible, boot chain cannot be redistributed legally, intended network/storage configuration impossible, or supply risk unacceptably high.

## Scoring (after gate)
| Criterion | Weight |
|---|---:|
| Procurement/lifecycle/second-source feasibility | 25% |
| Boot/kernel/upstream and licensing | 25% |
| Board/DDR/layout and bring-up risk | 20% |
| Network/PCIe/memory capability | 15% |
| Power/thermal profile | 10% |
| Per-unit cost at realistic volume | 5% |

Score 1–5 with cited evidence and dated quotes; missing evidence means **unknown**, not 3/5. Re-evaluate independently for each SKU.

## Mandatory proof artifacts
Datasheet revision and legal access; BOM reference and distributor quote date; pinout/ball map; DDR app notes; known-good boot log; public kernel/boot sources or redistribution terms; interfaces matrix; layout guidance; manufacturing/assembly feasibility estimate.

No SoC selected in M0 kickoff.
