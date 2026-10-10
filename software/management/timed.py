"""Deterministic clock-driven policy wrapper; no GPIO or actual hardware timers."""
from dataclasses import dataclass, field
from reference import Controller, State

@dataclass
class Timing:
    pgood_timeout_ms: int = 1000
    boot_grace_ms: int = 5000
    shutdown_grace_ms: int = 10000
    min_off_ms: int = 500
    heartbeat_timeout_ms: int = 3000
    retry_window_ms: int = 60000
    max_cycles: int = 3

    def __post_init__(self):
        if min(vars(self).values()) <= 0:
            raise ValueError("all timing values must be positive")

@dataclass
class TimedController:
    config: Timing = field(default_factory=Timing)
    core: Controller = field(default_factory=Controller)
    now_ms: int = 0
    entered_ms: int = 0
    pgood_since_ms: int | None = None
    last_heartbeat_ms: int | None = None
    retry_times: list[int] = field(default_factory=list)

    def __post_init__(self):
        # The wrapper enforces retry windows; core's legacy lifetime counter
        # must not prematurely reject otherwise allowed retries.
        self.core.max_cycles = 2147483647

    def command(self, event: str, *, authorized: bool = False, fault_clear: bool = False):
        if event == "heartbeat":
            if self.core.state == State.RUNNING:
                self.last_heartbeat_ms = self.now_ms
            return self.core.state
        if event == "pgood_high":
            if self.core.state == State.POWERING_ON and self.pgood_since_ms is None:
                self.pgood_since_ms = self.now_ms
            return self.core.state
        if event == "pgood_low":
            self.pgood_since_ms = None
            return self.core.state
        previous = self.core.state
        if event == "power_on" and previous == State.OFF and authorized:
            self.retry_times.clear()
            self.core.cycles = 0
        if event == "power_cycle" and previous == State.RUNNING and authorized:
            return self._cycle()
        self.core.event(event, authorized=authorized, fault_clear=fault_clear)
        self._after_transition(previous)
        return self.core.state

    def _after_transition(self, previous):
        if self.core.state != previous:
            self.entered_ms = self.now_ms
            if self.core.state == State.POWERING_ON:
                self.pgood_since_ms = None
            if self.core.state == State.RUNNING:
                self.last_heartbeat_ms = self.now_ms

    def _cycle(self):
        self.retry_times = [t for t in self.retry_times if self.now_ms - t < self.config.retry_window_ms]
        previous = self.core.state
        if len(self.retry_times) >= self.config.max_cycles:
            self.core.state, self.core.main_power, self.core.last_result = State.FAULT_LOCKOUT, False, "rate_limited"
        else:
            self.retry_times.append(self.now_ms)
            self.core.event("power_cycle", authorized=True)
        self._after_transition(previous)
        return self.core.state

    def advance(self, milliseconds: int):
        if milliseconds < 0:
            raise ValueError("time cannot move backwards")
        self.now_ms += milliseconds
        state = self.core.state
        elapsed = self.now_ms - self.entered_ms
        if state == State.POWERING_ON:
            if elapsed >= self.config.pgood_timeout_ms and self.pgood_since_ms is None:
                self.command("pgood_timeout")
            elif self.pgood_since_ms is not None and elapsed >= self.config.boot_grace_ms:
                self.command("pgood_stable")
        elif state == State.POWERING_OFF and elapsed >= self.config.shutdown_grace_ms:
            self.command("shutdown_timeout")
        elif state == State.CYCLING and elapsed >= self.config.min_off_ms:
            self.command("min_off_elapsed")
        elif state == State.RUNNING and self.last_heartbeat_ms is not None and self.now_ms - self.last_heartbeat_ms >= self.config.heartbeat_timeout_ms:
            self._cycle()
        return self.core.state
