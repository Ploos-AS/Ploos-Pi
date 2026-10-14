/* SPDX-License-Identifier: MIT */
#include "pp_management.h"
#include <stddef.h>
void pp_management_init(pp_management *m, uint32_t max_cycles) {
    if (m == NULL) return;
    *m = (pp_management){ .state = PP_OFF, .main_power = false,
                          .cycles = 0, .max_cycles = max_cycles };
}
bool pp_management_dispatch(pp_management *m, pp_event e, bool authorized, bool fault_clear) {
    if (m == NULL) return false;
    if (e == PP_RAIL_FAULT && m->state != PP_OFF && m->state != PP_FAULT_LOCKOUT) {
        m->state = PP_FAULT_LOCKOUT; m->main_power = false; return true;
    }
    switch (m->state) {
    case PP_OFF:
        if (e == PP_POWER_ON && authorized) {
            m->state = PP_POWERING_ON; m->main_power = true; return true;
        }
        if (e == PP_RECOVERY_START && authorized) {
            m->state = PP_RECOVERY; return true;
        }
        break;
    case PP_POWERING_ON:
        if (e == PP_POWER_ON && authorized) return true;
        if (e == PP_PGOOD_STABLE) { m->state = PP_RUNNING; return true; }
        if (e == PP_PGOOD_TIMEOUT) {
            m->state = PP_FAULT_LOCKOUT; m->main_power = false; return true;
        }
        break;
    case PP_RUNNING:
        if (e == PP_POWER_OFF && authorized) {
            m->state = PP_POWERING_OFF; return true;
        }
        if (e == PP_WATCHDOG_TIMEOUT || (e == PP_POWER_CYCLE && authorized)) {
            if (m->cycles >= m->max_cycles) {
                m->state = PP_FAULT_LOCKOUT;
            } else {
                m->cycles++; m->state = PP_CYCLING;
            }
            m->main_power = false; return true;
        }
        break;
    case PP_POWERING_OFF:
        if (e == PP_SHUTDOWN_COMPLETE || e == PP_SHUTDOWN_TIMEOUT) {
            m->state = PP_OFF; m->main_power = false; return true;
        }
        break;
    case PP_CYCLING:
        if (e == PP_MIN_OFF_ELAPSED) {
            if (m->cycles > m->max_cycles) {
                m->state = PP_FAULT_LOCKOUT;
            } else {
                m->state = PP_POWERING_ON; m->main_power = true;
            }
            return true;
        }
        break;
    case PP_FAULT_LOCKOUT:
        if (e == PP_CLEAR_FAULT && authorized && fault_clear) {
            m->state = PP_OFF; m->main_power = false; m->cycles = 0; return true;
        }
        break;
    case PP_RECOVERY:
        if (e == PP_RECOVERY_COMPLETE) {
            m->state = PP_OFF; return true;
        }
        break;
    }
    return false;
}

pp_result pp_management_dispatch_result(pp_management *m, pp_event e,
                                         bool authorized, bool fault_clear) {
    if (m == NULL) return PP_RESULT_REJECTED;
    pp_state before = m->state;
    uint32_t cycles_before = m->cycles;
    if (!pp_management_dispatch(m, e, authorized, fault_clear))
        return PP_RESULT_REJECTED;
    if (e == PP_RAIL_FAULT) return PP_RESULT_LOCKOUT_LATCHED;
    if (e == PP_POWER_ON && before == PP_POWERING_ON) return PP_RESULT_IDEMPOTENT;
    if (e == PP_PGOOD_TIMEOUT) return PP_RESULT_FAULT_RECORDED;
    if (e == PP_PGOOD_STABLE) return PP_RESULT_RUNNING;
    if (e == PP_POWER_OFF) return PP_RESULT_SHUTDOWN_REQUESTED;
    if (e == PP_SHUTDOWN_COMPLETE || e == PP_SHUTDOWN_TIMEOUT ||
        e == PP_RECOVERY_COMPLETE) return PP_RESULT_COMPLETED;
    if (e == PP_WATCHDOG_TIMEOUT || e == PP_POWER_CYCLE) {
        return m->state == PP_FAULT_LOCKOUT ? PP_RESULT_RATE_LIMITED :
               (m->cycles > cycles_before ? PP_RESULT_CYCLE_INCREMENTED : PP_RESULT_REJECTED);
    }
    if (e == PP_MIN_OFF_ELAPSED && m->state == PP_FAULT_LOCKOUT)
        return PP_RESULT_RATE_LIMITED;
    if (e == PP_RECOVERY_START) return PP_RESULT_RECOVERY_SELECTED;
    return PP_RESULT_ACCEPTED;
}
