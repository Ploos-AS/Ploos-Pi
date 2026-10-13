/* SPDX-License-Identifier: MIT */
/* M2.1: 12 scenarios mirrored from docs/engineering/m1-1-management-test-vectors.csv.
 * Outcome strings are not yet part of the C API; state/power/acceptance are checked.
 */
#include "pp_management.h"
#include <assert.h>
#include <stdio.h>
typedef struct {
    const char *id;
    pp_state initial, expected;
    pp_event event;
    bool authorized, fault_clear, power_before, power_after, accepted;
    uint32_t cycles, limit;
} vector;
static const vector cases[] = {
    {"SM-001", PP_OFF, PP_POWERING_ON, PP_POWER_ON, true, false, false, true, true, 0, 3},
    {"SM-002", PP_POWERING_ON, PP_POWERING_ON, PP_POWER_ON, true, false, true, true, true, 0, 3},
    {"SM-003", PP_POWERING_ON, PP_FAULT_LOCKOUT, PP_PGOOD_TIMEOUT, false, false, true, false, true, 0, 3},
    {"SM-004", PP_RUNNING, PP_POWERING_OFF, PP_POWER_OFF, true, false, true, true, true, 0, 3},
    {"SM-005", PP_POWERING_OFF, PP_OFF, PP_SHUTDOWN_COMPLETE, false, false, true, false, true, 0, 3},
    {"SM-006", PP_RUNNING, PP_CYCLING, PP_WATCHDOG_TIMEOUT, false, false, true, false, true, 0, 3},
    {"SM-007", PP_RUNNING, PP_FAULT_LOCKOUT, PP_RAIL_FAULT, false, false, true, false, true, 0, 3},
    {"SM-008", PP_FAULT_LOCKOUT, PP_FAULT_LOCKOUT, PP_CLEAR_FAULT, false, true, false, false, false, 0, 3},
    {"SM-009", PP_FAULT_LOCKOUT, PP_OFF, PP_CLEAR_FAULT, true, true, false, false, true, 0, 3},
    {"SM-010", PP_OFF, PP_RECOVERY, PP_RECOVERY_START, true, false, false, false, true, 0, 3},
    {"SM-011", PP_RUNNING, PP_RUNNING, PP_RECOVERY_START, false, false, true, true, false, 0, 3},
    {"SM-012", PP_CYCLING, PP_FAULT_LOCKOUT, PP_MIN_OFF_ELAPSED, false, false, false, false, true, 4, 3}
};
int main(void) {
    for (size_t i = 0; i < sizeof cases / sizeof cases[0]; ++i) {
        const vector *v = &cases[i];
        pp_management m;
        pp_management_init(&m, v->limit);
        m.state = v->initial;
        m.main_power = v->power_before;
        m.cycles = v->cycles;
        bool accepted = pp_management_dispatch(&m, v->event, v->authorized, v->fault_clear);
        if (m.state != v->expected || m.main_power != v->power_after || accepted != v->accepted) {
            fprintf(stderr, "%s FAILED: state=%d power=%d accepted=%d\n",
                    v->id, (int)m.state, (int)m.main_power, (int)accepted);
            return 1;
        }
    }
    puts("12 C state/power/acceptance vectors: PASS");
    return 0;
}
