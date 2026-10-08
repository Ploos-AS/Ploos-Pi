# ADR-0001 — Original SBC family, no compute modules

- Status: accepted (product direction)
- Date: 2026-10-09
- Decision: Build three independent Ploos Pi ARM SBC products (Nano, Compute, Pro) around bare SoCs and directly attached components. Do not use a Raspberry Pi CM, SoM or other compute module as the product compute core.
- Rationale: Full board-level control, product differentiation, direct rack integration and consistent system management.
- Consequences: Higher NRE, DDR/high-speed layout, BGA bring-up, supply-chain and compliance burden. Longer validation and potentially higher minimum viable production volume.
- Shared assets: management specification, firmware conventions, mechanical/rack interface philosophy, test methodology and CI.
- Revisit: only by explicit product decision with documented rationale.
