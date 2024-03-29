#include "WorkStatus_SplDcps.h"
#include "ccpp_WorkStatus_.h"

#include <v_copyIn.h>
#include <v_topic.h>
#include <os_stdlib.h>
#include <string.h>
#include <os_report.h>

v_copyin_result
__ssafy_msgs_msg_dds__WorkStatus___copyIn(
    c_base base,
    const struct ::ssafy_msgs::msg::dds_::WorkStatus_ *from,
    struct _ssafy_msgs_msg_dds__WorkStatus_ *to)
{
    v_copyin_result result = V_COPYIN_RESULT_OK;
    (void) base;

    to->is_done_ = (c_bool)from->is_done_;
    to->is_start_ = (c_bool)from->is_start_;
    return result;
}

void
__ssafy_msgs_msg_dds__WorkStatus___copyOut(
    const void *_from,
    void *_to)
{
    const struct _ssafy_msgs_msg_dds__WorkStatus_ *from = (const struct _ssafy_msgs_msg_dds__WorkStatus_ *)_from;
    struct ::ssafy_msgs::msg::dds_::WorkStatus_ *to = (struct ::ssafy_msgs::msg::dds_::WorkStatus_ *)_to;
    to->is_done_ = (::DDS::Boolean)(from->is_done_ != 0);
    to->is_start_ = (::DDS::Boolean)(from->is_start_ != 0);
}

