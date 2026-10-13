/* SPDX-License-Identifier: MIT */
#include "pp_management.h"
#include <assert.h>
#include <stdio.h>
int main(void) {
    pp_management m;
    pp_management_init(&m, 1);
    assert(m.state == PP_OFF && !m.main_power);
    assert(!pp_management_dispatch(&m, PP_POWER_ON, false, false));
    assert(pp_management_dispatch(&m, PP_POWER_ON, true, false));
    assert(m.state == PP_POWERING_ON && m.main_power);
    assert(pp_management_dispatch(&m, PP_PGOOD_STABLE, false, false));
    assert(m.state == PP_RUNNING);
    assert(pp_management_dispatch(&m, PP_WATCHDOG_TIMEOUT, false, false));
    assert(m.state == PP_CYCLING && !m.main_power);
    assert(pp_management_dispatch(&m, PP_MIN_OFF_ELAPSED, false, false));
    assert(m.state == PP_POWERING_ON && m.main_power);
    assert(pp_management_dispatch(&m, PP_PGOOD_STABLE, false, false));
    assert(pp_management_dispatch(&m, PP_WATCHDOG_TIMEOUT, false, false));
    assert(m.state == PP_FAULT_LOCKOUT && !m.main_power);
    assert(!pp_management_dispatch(&m, PP_CLEAR_FAULT, false, true));
    assert(!pp_management_dispatch(&m, PP_CLEAR_FAULT, true, false));
    assert(pp_management_dispatch(&m, PP_CLEAR_FAULT, true, true));
    assert(m.state == PP_OFF && !m.main_power && m.cycles == 0);
    assert(pp_management_dispatch(&m, PP_RECOVERY_START, true, false));
    assert(m.state == PP_RECOVERY && !m.main_power);
    assert(pp_management_dispatch(&m, PP_RECOVERY_COMPLETE, false, false));
    assert(m.state == PP_OFF && !m.main_power);
    puts("management C smoke test: PASS");
    return 0;
}
