# Ploos Node Management Protocol — v0 design draft

**Not implemented; no claims of interoperability or security validation.**

## Architectural boundaries
An always-on microcontroller monitors the host and remains functional while host Linux is unavailable. Remote API is served by a secure controller/gateway layer; never expose an unauthenticated MCU debug bus to an untrusted network.

## State machine
OFF -> POWERING -> BOOTING -> RUNNING -> SHUTDOWN_REQUESTED -> OFF; FAULT and RECOVERY are separate states. Every transition includes monotonic sequence ID, reason, timestamp if available and outcome.

## Draft commands
| Command | Purpose | Minimum authorization |
|---|---|---|
| inventory.get | board/SKU/revision/firmware | authenticated reader |
| health.get | rail/thermal/watchdog state | authenticated reader |
| power.on | request host power | privileged operator |
| power.shutdown | request graceful shutdown | privileged operator |
| power.cycle | controlled shutdown then power reset | privileged operator |
| recovery.enter | request recovery boot | privileged operator, audit |
| events.get | inspect reset and fault log | authenticated reader |

## Required semantics
- Commands are idempotent where possible, with request ID and explicit success/failure states.
- A power-cycle command must distinguish graceful shutdown from forced cut; forced cut requires explicit confirmation and timeout policy.
- Rate limits and minimum off/on intervals prevent destructive restart loops.
- Host watchdog heartbeat failure must not imply immediate unsafe power cycling.
- Record controller and host firmware versions in all diagnostics.
- No secrets or private keys stored in world-readable host partitions.

## Open decisions
Physical transport, authentication implementation, management MCU family, clock/time source, out-of-band Ethernet vs backplane gateway, firmware update signing and anti-rollback.
