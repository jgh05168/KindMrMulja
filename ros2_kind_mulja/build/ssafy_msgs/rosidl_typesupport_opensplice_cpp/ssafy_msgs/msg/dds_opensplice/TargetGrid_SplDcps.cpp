#include "TargetGrid_SplDcps.h"
#include "ccpp_TargetGrid_.h"

#include <v_copyIn.h>
#include <v_topic.h>
#include <os_stdlib.h>
#include <string.h>
#include <os_report.h>

v_copyin_result
__ssafy_msgs_msg_dds__TargetGrid___copyIn(
    c_base base,
    const struct ::ssafy_msgs::msg::dds_::TargetGrid_ *from,
    struct _ssafy_msgs_msg_dds__TargetGrid_ *to)
{
    v_copyin_result result = V_COPYIN_RESULT_OK;
    (void) base;

    to->product_x_ = (c_double)from->product_x_;
    to->product_y_ = (c_double)from->product_y_;
    to->moving_zone_x_ = (c_double)from->moving_zone_x_;
    to->moving_zone_y_ = (c_double)from->moving_zone_y_;
    to->charge_x_ = (c_double)from->charge_x_;
    to->charge_y_ = (c_double)from->charge_y_;
    return result;
}

void
__ssafy_msgs_msg_dds__TargetGrid___copyOut(
    const void *_from,
    void *_to)
{
    const struct _ssafy_msgs_msg_dds__TargetGrid_ *from = (const struct _ssafy_msgs_msg_dds__TargetGrid_ *)_from;
    struct ::ssafy_msgs::msg::dds_::TargetGrid_ *to = (struct ::ssafy_msgs::msg::dds_::TargetGrid_ *)_to;
    to->product_x_ = (::DDS::Double)from->product_x_;
    to->product_y_ = (::DDS::Double)from->product_y_;
    to->moving_zone_x_ = (::DDS::Double)from->moving_zone_x_;
    to->moving_zone_y_ = (::DDS::Double)from->moving_zone_y_;
    to->charge_x_ = (::DDS::Double)from->charge_x_;
    to->charge_y_ = (::DDS::Double)from->charge_y_;
}

