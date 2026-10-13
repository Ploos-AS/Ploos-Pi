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
        if (e == PP_WATCHDOG_TIMEOUT) {
            if (m->cycles >= m->max_cycles) {
                m->state = PP_FAULT_LOCKOUT;
            } else {
                m->cycles++; m->state = PP_CYCLING;
            }
            m->main_power = false; return true;
        }
        break;
    case PP_POWERING_OFF:
        if (e == PP_SHUTDOWN_COMPLETE) {
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
