#include "RequestHandControl_SplDcps.h"
#include "ccpp_RequestHandControl_.h"

#include <v_copyIn.h>
#include <v_topic.h>
#include <os_stdlib.h>
#include <string.h>
#include <os_report.h>

v_copyin_result
__ssafy_msgs_msg_dds__RequestHandControl___copyIn(
    c_base base,
    const struct ::ssafy_msgs::msg::dds_::RequestHandControl_ *from,
    struct _ssafy_msgs_msg_dds__RequestHandControl_ *to)
{
    v_copyin_result result = V_COPYIN_RESULT_OK;
    (void) base;

    to->control_mode_ = (c_octet)from->control_mode_;
    return result;
}

void
__ssafy_msgs_msg_dds__RequestHandControl___copyOut(
    const void *_from,
    void *_to)
{
    const struct _ssafy_msgs_msg_dds__RequestHandControl_ *from = (const struct _ssafy_msgs_msg_dds__RequestHandControl_ *)_from;
    struct ::ssafy_msgs::msg::dds_::RequestHandControl_ *to = (struct ::ssafy_msgs::msg::dds_::RequestHandControl_ *)_to;
    to->control_mode_ = (::DDS::Octet)from->control_mode_;
}

