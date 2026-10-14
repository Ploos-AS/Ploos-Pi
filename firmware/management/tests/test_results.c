/* SPDX-License-Identifier: MIT */
#include "pp_management.h"
#include <assert.h>
#include <stdio.h>
int main(void) {
    pp_management m;
    pp_management_init(&m, 1);
    assert(pp_management_dispatch_result(&m, PP_POWER_ON, false, false) == PP_RESULT_REJECTED);
    assert(pp_management_dispatch_result(&m, PP_POWER_ON, true, false) == PP_RESULT_ACCEPTED);
    assert(pp_management_dispatch_result(&m, PP_POWER_ON, true, false) == PP_RESULT_IDEMPOTENT);
    assert(pp_management_dispatch_result(&m, PP_PGOOD_STABLE, false, false) == PP_RESULT_RUNNING);
    assert(pp_management_dispatch_result(&m, PP_POWER_CYCLE, false, false) == PP_RESULT_REJECTED);
    assert(pp_management_dispatch_result(&m, PP_POWER_CYCLE, true, false) == PP_RESULT_CYCLE_INCREMENTED);
    assert(m.state == PP_CYCLING && !m.main_power);
    assert(pp_management_dispatch_result(&m, PP_MIN_OFF_ELAPSED, false, false) == PP_RESULT_ACCEPTED);
    assert(pp_management_dispatch_result(&m, PP_PGOOD_STABLE, false, false) == PP_RESULT_RUNNING);
    assert(pp_management_dispatch_result(&m, PP_WATCHDOG_TIMEOUT, false, false) == PP_RESULT_RATE_LIMITED);
    assert(m.state == PP_FAULT_LOCKOUT && !m.main_power);
    assert(pp_management_dispatch_result(&m, PP_CLEAR_FAULT, true, true) == PP_RESULT_ACCEPTED);
    assert(pp_management_dispatch_result(&m, PP_POWER_ON, true, false) == PP_RESULT_ACCEPTED);
    assert(pp_management_dispatch_result(&m, PP_PGOOD_TIMEOUT, false, false) == PP_RESULT_FAULT_RECORDED);
    puts("C outcome tests: PASS");
    return 0;
}
