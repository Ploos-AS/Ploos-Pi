/* SPDX-License-Identifier: MIT */
#ifndef PP_MANAGEMENT_H
#define PP_MANAGEMENT_H
#include <stdbool.h>
#include <stdint.h>
typedef enum {
    PP_OFF, PP_POWERING_ON, PP_RUNNING, PP_POWERING_OFF,
    PP_CYCLING, PP_FAULT_LOCKOUT, PP_RECOVERY
} pp_state;
typedef enum {
    PP_POWER_ON, PP_PGOOD_STABLE, PP_PGOOD_TIMEOUT, PP_POWER_OFF,
    PP_SHUTDOWN_COMPLETE, PP_WATCHDOG_TIMEOUT, PP_RAIL_FAULT,
    PP_CLEAR_FAULT, PP_RECOVERY_START, PP_RECOVERY_COMPLETE,
    PP_MIN_OFF_ELAPSED, PP_SHUTDOWN_TIMEOUT, PP_POWER_CYCLE
} pp_event;
typedef struct {
    pp_state state;
    bool main_power;
    uint32_t cycles;
    uint32_t max_cycles;
} pp_management;
typedef enum {
    PP_RESULT_REJECTED, PP_RESULT_ACCEPTED, PP_RESULT_IDEMPOTENT,
    PP_RESULT_FAULT_RECORDED, PP_RESULT_RUNNING, PP_RESULT_SHUTDOWN_REQUESTED,
    PP_RESULT_COMPLETED, PP_RESULT_CYCLE_INCREMENTED, PP_RESULT_LOCKOUT_LATCHED,
    PP_RESULT_RATE_LIMITED, PP_RESULT_RECOVERY_SELECTED
} pp_result;
pp_result pp_management_dispatch_result(pp_management *m, pp_event event,
                                         bool authorized, bool fault_clear);
void pp_management_init(pp_management *m, uint32_t max_cycles);
bool pp_management_dispatch(pp_management *m, pp_event event, bool authorized, bool fault_clear);
#endif
