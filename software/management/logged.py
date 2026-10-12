"""M1.8: in-memory fault journal integration, NOT persistent MCU storage."""
from dataclasses import dataclass, field
from timed import TimedController
from reference import State
from fault_journal import FaultRecord, encode, latest_valid

@dataclass
class LoggedController(TimedController):
    slots: list[bytes] = field(default_factory=list)
    next_sequence: int = 1

    def __post_init__(self):
        super().__post_init__()
        last = latest_valid(self.slots)
        if last is not None:
            self.next_sequence = last.sequence + 1

    def _record(self, reason: str, prior_state: State):
        if self.next_sequence >= 2**64:
            raise OverflowError("fault sequence exhausted; rollover policy required")
        record = FaultRecord(self.next_sequence, self.now_ms, reason, prior_state.value)
        self.slots.append(encode(record))
        self.next_sequence += 1

    def command(self, event: str, *, authorized: bool = False, fault_clear: bool = False):
        prior = self.core.state
        result = super().command(event, authorized=authorized, fault_clear=fault_clear)
        if event == "pgood_low" and prior == State.RUNNING and result == State.FAULT_LOCKOUT:
            self._record("rail_fault", prior)
        elif event == "rail_fault" and prior not in {State.OFF, State.FAULT_LOCKOUT} and result == State.FAULT_LOCKOUT:
            self._record("rail_fault", prior)
        elif event == "pgood_timeout" and prior == State.POWERING_ON and result == State.FAULT_LOCKOUT:
            self._record("pgood_timeout", prior)
        elif event == "shutdown_timeout" and prior == State.POWERING_OFF and result == State.OFF:
            self._record("shutdown_timeout", prior)
        return result

    def _cycle(self):
        prior = self.core.state
        result = super()._cycle()
        if prior == State.RUNNING:
            reason = "rate_limited" if result == State.FAULT_LOCKOUT else "watchdog_timeout"
            self._record(reason, prior)
        return result
