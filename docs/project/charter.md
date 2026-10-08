# Project charter — M0

## Mission
Design and eventually produce three *original* Ploos Pi ARM64 SBCs optimized for headless data-centre, homelab, CI and compute-node deployment. Each uses a bare SoC and discrete board-level components, not a plug-in compute module.

## Users
Homelab operators, makers, open-hardware contributors, distributed-compute projects, educators and small fleet operators.

## Product scope
Nano (lowest-cost/low-power), Compute (balanced), Pro (higher-performance/high-I/O). Shared management firmware, mechanical conventions and orchestration APIs where feasible; separate PCB and SoC choices permitted.

## M0 in scope
Market/user requirements, component feasibility, functional partitioning, interface definitions, sourcing, licensing, cost models, engineering validation plans and crowdfunding prerequisites.

## M0 out of scope
Tape-out or custom silicon, finished PCB, claims of functional prototype, certified safety/EMC compliance, customer deposits or unvalidated shipping dates.

## Decision principles
Evidence before marketing; documented trade-offs; reproducible artifacts; conservative electrical and thermal margins; supply-chain resilience; transparent revisions and cost assumptions. A design is not production-ready simply because a prototype boots.

## Success / exit gate
See [roadmap](roadmap.md). No progression to PCB layout until candidate SoC documentation, power/DDR/high-speed feasibility, procurement path and boot chain are independently reviewed.

## Owners and governance
Ploos AS is project steward. Technical decisions recorded in ADRs; significant changes via PR review. Product and commercial commitments require an explicit business decision, not a GitHub issue alone.
