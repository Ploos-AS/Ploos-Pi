# M0.1 — Bare-SoC candidate longlist (research hypotheses)

**Status: candidate discovery, NOT qualification.** No manufacturer has confirmed availability, documentation rights, pricing or suitability for Ploos Pi. Verify exact orderable part numbers and interfaces against the latest manufacturer documentation before scoring.

| Family to investigate | Initial SKU fit hypothesis | Why investigate | Critical questions |
|---|---|---|---|
| Allwinner H618 / H616 | Nano | Low-end quad-core ARM64 class | Authorized bare-chip sourcing, documentation, DDR layout guide, long-term supply, mainline boot |
| Rockchip RK3566 / RK3568 | Nano / Compute | ARM64 with PCIe and Ethernet options | Exact SKU I/O, DDR design, Linux support, bare SoC sourcing |
| Rockchip RK3588 / RK3588S | Compute / Pro | Eight-core high-I/O class | PCIe and 10GbE implementation (external NIC), power, cost, kernel/boot chain |
| NXP i.MX 8M Plus | Compute | Industrial lifecycle/documentation ecosystem | Sustained CPU throughput, 2.5GbE path, price/volume |
| NXP i.MX 95 family | Pro | Newer industrial application processors | Public documentation, actual lane/PHY support, price and sourcing |
| TI AM62x / AM64x | Nano / management-oriented variants | Embedded Linux and long-lifecycle focus | Compute performance, networking and memory capacity vs target |
| Amlogic A311D2 family | Compute | Multicore ARM64 ecosystem | Legal firmware availability, sourcing, DDR, kernel maintenance |

Do **not** interpret the table as verified chip capabilities, procurement options, approved vendor list or recommendation. Model-specific claims require dated primary-source citations.

## Candidate elimination gates
1. Orderable **bare SoC**, with authorized procurement channel and known MOQ.
2. Legal access to pinout, hardware integration, DDR and power sequencing documentation.
3. Linux boot-chain source/redistribution path and recovery mechanism.
4. Actual Ethernet and PCIe topology capable of meeting the proposed SKU target.
5. Commercial and technical viability at prototype and production quantities.
6. Manufacturer lifecycle information and clear product change notification path.

## Required evidence row per exact part number
- Manufacturer URL, document title/revision/date and whether accessible under NDA.
- Distributor/representative, quotation date, currency, quantity, MOQ and lead time.
- CPU topology, DDR maximum, package/ball count, PMIC and power tree.
- Ethernet MAC/PHY, PCIe lane/speed and 10GbE NIC compatibility assumptions.
- Upstream kernel/U-Boot support status with links; binary blob licensing.
- PCB stackup/DDR constraints, thermal envelope, security/recovery.
- Known blockers, confidence level, reviewer and last verified date.

**Selection rule:** An unknown on a hard gate is a HOLD, not a PASS. Do not award weighted points before hard-gate review.
