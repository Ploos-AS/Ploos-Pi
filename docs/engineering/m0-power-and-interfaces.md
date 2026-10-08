# M0.2 — Power, management and backplane draft

**Status: design proposal, not a pinout or validated electrical specification.**

## Node power domains
- Input protection: polarity/reverse-current behavior, overcurrent and transient control to be defined.
- Always-on management rail, electrically isolated as appropriate from host SoC switched rails.
- Host power tree: SoC/DDR/eMMC/PHY rails with datasheet-derived sequencing and tolerances.
- Independent telemetry (voltage, current, temperatures, reset reason) with calibrated measurement plan.

## Management states
OFF -> PRECHARGE/POWERING -> BOOTING -> RUNNING -> SHUTTING_DOWN -> OFF; FAULT/RECOVERY transitions explicitly logged. A hard power cut must not be the normal shutdown path.

## Initial API contracts (not yet implemented)
- Read inventory and firmware revision.
- Read health/rail measurements, uptime, last reset reason.
- Request graceful shutdown, reset or power cycle with access control.
- Request recovery boot, and provide an auditable serial console path.

## Safety and security
Default-deny remote power operations; signed firmware update/recovery should be evaluated. Host OS must not be able to spoof controller health without detection. Rate-limit power cycles and preserve fault history.

## Backplane unknowns
Supply voltage and current budget, connector pinout, mating cycles, keyed insertion, per-slot fuse, inrush, airflow, grounding, signal integrity and whether true hot-swap is achievable. **No hot-swap claim** until tested.

## Review outputs
1. Electrical block diagram per SKU.
2. Rail budgets and sequencer timing for selected SoCs.
3. Connector tradeoff with creepage/clearance and current ratings.
4. Fault-tree analysis and security threat model.
5. Acceptance tests for brown-out, watchdog and recovery.
