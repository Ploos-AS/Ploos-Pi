"""Ploos Pi management policy reference model. No hardware access."""
from dataclasses import dataclass
from enum import Enum

class State(str, Enum):
    OFF = "OFF"
    POWERING_ON = "POWERING_ON"
    RUNNING = "RUNNING"
    POWERING_OFF = "POWERING_OFF"
    CYCLING = "CYCLING"
    FAULT_LOCKOUT = "FAULT_LOCKOUT"
    RECOVERY = "RECOVERY"

@dataclass
class Controller:
    state: State = State.OFF
    main_power: bool = False
    cycles: int = 0
    max_cycles: int = 3
    last_result: str = "initialized"

    def event(self, name: str, *, authorized: bool = False,
              fault_clear: bool = False, within_retry_limit: bool = True) -> State:
        s = self.state
        if name == "rail_fault" and s in {State.POWERING_ON, State.RUNNING, State.POWERING_OFF, State.CYCLING, State.RECOVERY}:
            self.state, self.main_power, self.last_result = State.FAULT_LOCKOUT, False, "lockout_latched"
        elif s == State.OFF and name == "power_on" and authorized:
            self.state, self.main_power, self.last_result = State.POWERING_ON, True, "accepted"
        elif s == State.POWERING_ON and name == "power_on" and authorized:
            self.last_result = "idempotent"
        elif s == State.POWERING_ON and name == "pgood_timeout":
            self.state, self.main_power, self.last_result = State.FAULT_LOCKOUT, False, "fault_recorded"
        elif s == State.POWERING_ON and name == "pgood_stable":
            self.state, self.last_result = State.RUNNING, "running"
        elif s == State.RUNNING and name == "power_off" and authorized:
            self.state, self.last_result = State.POWERING_OFF, "graceful_shutdown_requested"
        elif s == State.POWERING_OFF and name in {"shutdown_complete", "shutdown_timeout"}:
            self.state, self.main_power, self.last_result = State.OFF, False, "completed"
        elif s == State.RUNNING and name in {"watchdog_timeout", "power_cycle"} and (name != "power_cycle" or authorized):
            if within_retry_limit and self.cycles < self.max_cycles:
                self.cycles += 1
                self.state, self.main_power, self.last_result = State.CYCLING, False, "cycle_count_incremented"
            else:
                self.state, self.main_power, self.last_result = State.FAULT_LOCKOUT, False, "rate_limited"
        elif s == State.CYCLING and name == "min_off_elapsed":
            if within_retry_limit and self.cycles <= self.max_cycles:
                self.state, self.main_power, self.last_result = State.POWERING_ON, True, "accepted"
            else:
                self.state, self.main_power, self.last_result = State.FAULT_LOCKOUT, False, "rate_limited"
        elif s == State.FAULT_LOCKOUT and name == "clear_fault" and authorized and fault_clear:
            self.state, self.main_power, self.cycles, self.last_result = State.OFF, False, 0, "accepted"
        elif s == State.OFF and name == "recovery" and authorized:
            self.state, self.main_power, self.last_result = State.RECOVERY, False, "recovery_straps_selected"
        elif s == State.RECOVERY and name == "recovery_complete":
            self.state, self.main_power, self.last_result = State.OFF, False, "completed"
        else:
            self.last_result = "rejected"
        assert self.main_power is False if self.state in {State.OFF, State.FAULT_LOCKOUT, State.RECOVERY, State.CYCLING} else True
        return self.state
