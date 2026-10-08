# Risk register — initial

Status: open. Likelihood/impact to be reviewed at each gate.

| ID | Risk | Impact | Initial mitigation | Trigger |
|---|---|---|---|---|
| R01 | Bare SoC unobtainable or MOQ too high | High | supplier quotes, alternate candidate | no executable procurement path |
| R02 | DDR/BGA bring-up failure | High | reference design review, controlled stack-up, expert review | no stable memory training |
| R03 | Closed firmware/license conflict | High | legal IP audit and source review | no redistributable image |
| R04 | Linux support immature | High | upstream assessment and repeatable boot builds | critical private patches |
| R05 | Power/thermal miss | High | power budget and instrumented loads | throttling or unsafe temps |
| R06 | EMC/regulatory surprises | High | pre-compliance testing and specialist review | repeated failures |
| R07 | Network PHY/PCIe limitations | Medium–High | lane/topology analysis before selection | insufficient I/O |
| R08 | Low pilot yield and rework costs | High | DFM/DFT and test fixtures | yield below approved threshold |
| R09 | Logistics, VAT, tariff and returns costs | High | landed-cost model and fulfillment quotes | negative unit margin |
| R10 | Crowdfunding delay/under-delivery | High | conservative gates and independently reviewed schedule | schedule or supplier slips |
| R11 | Component obsolescence | Medium–High | lifecycle monitoring and approved alternates | EOL notice |
| R12 | Management attack surface | High | authenticated controls, isolation, threat model | unauthenticated power control |

Do not describe mitigations as completed without linked artifacts and owner signoff.
