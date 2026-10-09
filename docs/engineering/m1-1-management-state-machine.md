# M1.1 — Nano independent management state machine

Date: 2026-10-09. **Design proposal, not implemented firmware or tested hardware.**

## States
- `OFF`: management always-on rail active, main power disabled.
- `POWERING_ON`: assert MAIN_PWR_EN, await MAIN_PGOOD and boot grace period.
- `RUNNING`: main rails good; host may provide watchdog heartbeat.
- `POWERING_OFF`: request graceful shutdown, then disable main rails after timeout.
- `CYCLING`: remove main rails for minimum off-time, then enter POWERING_ON.
- `FAULT_LOCKOUT`: disable main rails after repeated faults; requires authorized clear.
- `RECOVERY`: request documented recovery boot straps, then sequence main power.

## Transitions
| From | Event | To | Condition/action |
|---|---|---|---|
| OFF | authorized power_on | POWERING_ON | Assert main enable |
| POWERING_ON | PGOOD stable and boot grace elapsed | RUNNING | Arm host watchdog only when enabled |
| POWERING_ON | PGOOD timeout | FAULT_LOCKOUT | Record reason, deassert enable |
| RUNNING | authorized power_off | POWERING_OFF | Request graceful host shutdown |
| POWERING_OFF | host stopped or grace timeout | OFF | Remove main power |
| RUNNING | authorized power_cycle | CYCLING | Request shutdown then remove main power |
| CYCLING | minimum off-time elapsed | POWERING_ON | Re-enable rails |
| RUNNING | watchdog expires | CYCLING | Count and rate-limit resets |
| ANY ACTIVE | rail fault / overcurrent | FAULT_LOCKOUT | Immediately disable main power where electrically safe |
| FAULT_LOCKOUT | authorized clear_fault | OFF | Clear latch only after fault input safe |
| OFF | authorized recovery | RECOVERY | Configure boot straps while main power off |
| RECOVERY | recovery session complete | OFF | Restore normal straps with main power off |

## Invariants
1. Management MCU stays powered whenever valid external input power exists.
2. Main power must be OFF in OFF and FAULT_LOCKOUT.
3. Recovery straps may change only with main power OFF, subject to SoC timing requirements.
4. No uncontrolled automatic retry after hard rail fault.
5. Host-originated requests cannot bypass lockout or authorization.
6. Commands must be idempotent or carry request IDs; unexpected repeats must not cause multiple power cycles.
7. On management MCU reset, hardware pull states keep main power in a documented safe state.
8. Management serial/network access must not imply unrestricted control without an explicit security policy.

## Timing parameters (TBD by hardware)
- `T_PGOOD_MAX_MS`
- `T_BOOT_GRACE_MS`
- `T_SHUTDOWN_GRACE_MS`
- `T_MIN_OFF_MS`
- `T_HEARTBEAT_TIMEOUT_MS`
- `MAX_CYCLES_PER_WINDOW` / `T_CYCLE_WINDOW_MS`

No numerical defaults are approved before PMIC, eMMC, DDR and host OS startup characteristics are measured.

## Failure injection tests
- Repeated `power_on` in POWERING_ON produces no additional transition.
- Fault asserted during POWERING_ON leads to FAULT_LOCKOUT.
- Host watchdog fails during RUNNING; cycling is rate limited.
- Management MCU resets during RUNNING; hardware-defined default prevents unsafe power glitch.
- Input voltage drops; host GPIO cannot back-power management or vice versa.
- Recovery request while RUNNING is rejected or safely sequenced through OFF.
- Unauthorized `clear_fault` is rejected.
- Event log retains reset reason across MCU reset when supported by chosen storage.

## Implementation note
Model transitions in a host-side reference implementation and unit tests before MCU firmware. Hardware-specific GPIO drivers and watchdog timing must be separate from policy. All interfaces are provisional pending component selection.
