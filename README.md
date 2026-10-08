# Ploos Pi

**Open-hardware ARM64 server boards for small compute nodes, clusters and homelabs.**

> **Status: M0 — concept and feasibility. No hardware prototype exists, no SoC is selected, and no crowdfunding campaign has been announced. Specifications below are targets, not promises.**

Ploos Pi is a family of **three independently designed single-board computers**, each using a bare ARM SoC, directly attached RAM, power circuitry, networking and storage. **No compute modules or third-party SoM carrier boards.**

| Target | Nano | Compute | Pro |
|---|---|---|---|
| Role | small always-on nodes | general compute/CI/render | high-end cluster workloads |
| CPU aspiration | 4 ARM64 cores | 8 ARM64 cores | 8–16 ARM64 cores |
| RAM aspiration | 2–4 GB | 8–16 GB | 16–32+ GB |
| Network aspiration | 1 GbE | 2.5 GbE | 10 GbE |
| Storage | eMMC | eMMC + NVMe | eMMC + NVMe |
| Remote management | mandatory | mandatory | mandatory |

These targets may change following component and manufacturing feasibility studies.

## Why build it?

Headless, efficient, fleet-manageable, serviceable ARM nodes are better suited to small datacenters than desktop-oriented SBCs. Intended use cases include Armada orchestration, AmiCompute offload, AmiRender workers, continuous integration and general Linux services.

## Read first

- [Project charter](docs/project/charter.md)
- [Architecture and non-negotiables](docs/architecture/system.md)
- [Product family requirements](docs/requirements/product-family.md)
- [M0 roadmap and acceptance gates](docs/project/roadmap.md)
- [Engineering validation plan](docs/engineering/validation.md)
- [Crowdfunding readiness and integrity](docs/crowdfunding/readiness.md)
- [Risk register](docs/project/risk-register.md)
- [Decisions (ADR)](docs/decisions/README.md)
- [Contributing](CONTRIBUTING.md)
- [Licensing](LICENSES.md)

## M0 deliverables

1. Requirements and traceable acceptance criteria for all three products.
2. Longlist and scoring template for purchasable, documentable bare ARM SoCs.
3. Initial board-level design partition and common management/backplane interface specification.
4. Prototype, bring-up, safety, thermal and production validation plans.
5. Honest, evidence-driven crowdfunding gates, BOM cost model and risk register.
6. Reviewable community governance and transparent milestone reporting.

**M0 does not include a PCB, tested firmware, verified performance, certified product or retail price.**

## Principles

- KiCad source, BOM, assembly files and manufacturing instructions when validated.
- Debian-based ARM64 support prioritized; upstream support preferred.
- UART recovery, watchdog, per-node power control, measurable power/thermal limits.
- Avoid undocumented vendor dependencies where viable; document every unavoidable closed component.
- No publication of credentials, proprietary datasheets under NDA, or unlicensed vendor binaries.
- Publish test results, failures and design revisions—not only successes.

Maintained by Ploos AS. Public information is subject to change during development.
