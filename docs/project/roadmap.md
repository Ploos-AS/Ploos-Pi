# Roadmap and release gates

| Stage | Output | Exit criteria |
|---|---|---|
| M0 feasibility | requirements, SoC comparison, design architecture, risks, costing methodology | reviewed documents; critical unknowns tracked; go/no-go decision |
| M1 Nano schematic | SoC/DDR/PMIC design, KiCad, design review | datasheet-based design review, stack-up and bring-up plan |
| M2 Nano prototype | assembled boards, boot logs, measurements | repeatable Linux boot, storage/network, power, thermal and reset tests |
| M3 Compute design | separate schematic/PCB, faster I/O | design review, prototypes tested against requirements |
| M4 Pro design | performance/PCIe/10GbE feasibility | design review, measured prototypes |
| M5 fleet ecosystem | backplane, management, deployment | testable APIs, controlled power cycling and recovery |
| M6 production pilot | DFM/DFT, pilot builds, sourcing | test fixtures, yield records, revision-controlled BOM |
| Campaign readiness | evidence package and manufacturing plan | all crowdfunding gates pass independently |

These are sequential decision gates, **not calendar or delivery promises**.

## M0 checklist
- [ ] Confirm target operating environments and workload measurements.
- [ ] Create bare-SoC candidate longlist with public documentation and purchasing proof.
- [ ] Evaluate DDR complexity, PCB stack-up, BGA assembly/rework and impedance control.
- [ ] Prove available bootloader/kernel/firmware licensing paths.
- [ ] Draft electrical power and network management standards.
- [ ] Establish transparent per-quantity BOM and landed-cost spreadsheet.
- [ ] Approve functional test matrix, risks, and funding boundaries.
- [ ] Review release licensing and third-party IP inventory.
- [ ] Publish M0 design review minutes and go/no-go record.
