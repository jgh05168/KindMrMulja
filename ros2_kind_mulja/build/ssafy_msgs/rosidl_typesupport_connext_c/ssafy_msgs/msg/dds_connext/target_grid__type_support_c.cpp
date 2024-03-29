// generated from rosidl_typesupport_connext_c/resource/idl__dds_connext__type_support_c.cpp.em
// with input from ssafy_msgs:msg\TargetGrid.idl
// generated code does not contain a copyright notice

#include <cassert>
#include <limits>

#include "ssafy_msgs/msg/target_grid__rosidl_typesupport_connext_c.h"
#include "rcutils/types/uint8_array.h"
#include "rosidl_typesupport_connext_c/identifier.h"
#include "rosidl_typesupport_connext_c/wstring_conversion.hpp"
#include "rosidl_typesupport_connext_cpp/message_type_support.h"
#include "ssafy_msgs/msg/rosidl_typesupport_connext_c__visibility_control.h"
#include "ssafy_msgs/msg/target_grid__struct.h"
#include "ssafy_msgs/msg/target_grid__functions.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif

#include "ssafy_msgs/msg/dds_connext/TargetGrid_Support.h"
#include "ssafy_msgs/msg/dds_connext/TargetGrid_Plugin.h"

#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions
#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions

static DDS_TypeCode *
_TargetGrid__get_type_code()
{
  return ssafy_msgs::msg::dds_::TargetGrid_TypeSupport::get_typecode();
}

static bool
_TargetGrid__convert_ros_to_dds(const void * untyped_ros_message, void * untyped_dds_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  if (!untyped_dds_message) {
    fprintf(stderr, "dds message handle is null\n");
    return false;
  }
  const ssafy_msgs__msg__TargetGrid * ros_message =
    static_cast<const ssafy_msgs__msg__TargetGrid *>(untyped_ros_message);
  ssafy_msgs::msg::dds_::TargetGrid_ * dds_message =
    static_cast<ssafy_msgs::msg::dds_::TargetGrid_ *>(untyped_dds_message);
  // Member name: product_x
  {
    dds_message->product_x_ = ros_message->product_x;
  }
  // Member name: product_y
  {
    dds_message->product_y_ = ros_message->product_y;
  }
  // Member name: moving_zone_x
  {
    dds_message->moving_zone_x_ = ros_message->moving_zone_x;
  }
  // Member name: moving_zone_y
  {
    dds_message->moving_zone_y_ = ros_message->moving_zone_y;
  }
  // Member name: charge_x
  {
    dds_message->charge_x_ = ros_message->charge_x;
  }
  // Member name: charge_y
  {
    dds_message->charge_y_ = ros_message->charge_y;
  }
  return true;
}

static bool
_TargetGrid__convert_dds_to_ros(const void * untyped_dds_message, void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  if (!untyped_dds_message) {
    fprintf(stderr, "dds message handle is null\n");
    return false;
  }
  const ssafy_msgs::msg::dds_::TargetGrid_ * dds_message =
    static_cast<const ssafy_msgs::msg::dds_::TargetGrid_ *>(untyped_dds_message);
  ssafy_msgs__msg__TargetGrid * ros_message =
    static_cast<ssafy_msgs__msg__TargetGrid *>(untyped_ros_message);
  // Member name: product_x
  {
    ros_message->product_x = dds_message->product_x_;
  }
  // Member name: product_y
  {
    ros_message->product_y = dds_message->product_y_;
  }
  // Member name: moving_zone_x
  {
    ros_message->moving_zone_x = dds_message->moving_zone_x_;
  }
  // Member name: moving_zone_y
  {
    ros_message->moving_zone_y = dds_message->moving_zone_y_;
  }
  // Member name: charge_x
  {
    ros_message->charge_x = dds_message->charge_x_;
  }
  // Member name: charge_y
  {
    ros_message->charge_y = dds_message->charge_y_;
  }
  return true;
}


static bool
_TargetGrid__to_cdr_stream(
  const void * untyped_ros_message,
  rcutils_uint8_array_t * cdr_stream)
{
  if (!untyped_ros_message) {
    return false;
  }
  if (!cdr_stream) {
    return false;
  }
  const ssafy_msgs__msg__TargetGrid * ros_message =
    static_cast<const ssafy_msgs__msg__TargetGrid *>(untyped_ros_message);
  ssafy_msgs::msg::dds_::TargetGrid_ dds_message;
  if (!_TargetGrid__convert_ros_to_dds(ros_message, &dds_message)) {
    return false;
  }

  // call the serialize function for the first time to get the expected length of the message
  unsigned int expected_length;
  if (ssafy_msgs::msg::dds_::TargetGrid_Plugin_serialize_to_cdr_buffer(
      NULL, &expected_length, &dds_message) != RTI_TRUE)
  {
    fprintf(stderr, "failed to call ssafy_msgs::msg::dds_::TargetGrid_Plugin_serialize_to_cdr_buffer()\n");
    return false;
  }
  cdr_stream->buffer_length = expected_length;
  if (cdr_stream->buffer_length > (std::numeric_limits<unsigned int>::max)()) {
    fprintf(stderr, "cdr_stream->buffer_length, unexpectedly larger than max unsigned int\n");
    return false;
  }
  if (cdr_stream->buffer_capacity < cdr_stream->buffer_length) {
    cdr_stream->allocator.deallocate(cdr_stream->buffer, cdr_stream->allocator.state);
    cdr_stream->buffer = static_cast<uint8_t *>(cdr_stream->allocator.allocate(cdr_stream->buffer_length, cdr_stream->allocator.state));
  }
  // call the function again and fill the buffer this time
  unsigned int buffer_length_uint = static_cast<unsigned int>(cdr_stream->buffer_length);
  if (ssafy_msgs::msg::dds_::TargetGrid_Plugin_serialize_to_cdr_buffer(
      reinterpret_cast<char *>(cdr_stream->buffer),
      &buffer_length_uint,
      &dds_message) != RTI_TRUE)
  {
    return false;
  }

  return true;
}

static bool
_TargetGrid__to_message(
  const rcutils_uint8_array_t * cdr_stream,
  void * untyped_ros_message)
{
  if (!cdr_stream) {
    return false;
  }
  if (!untyped_ros_message) {
    return false;
  }

  ssafy_msgs::msg::dds_::TargetGrid_ * dds_message =
    ssafy_msgs::msg::dds_::TargetGrid_TypeSupport::create_data();
  if (cdr_stream->buffer_length > (std::numeric_limits<unsigned int>::max)()) {
    fprintf(stderr, "cdr_stream->buffer_length, unexpectedly larger than max unsigned int\n");
    return false;
  }
  if (ssafy_msgs::msg::dds_::TargetGrid_Plugin_deserialize_from_cdr_buffer(
      dds_message,
      reinterpret_cast<char *>(cdr_stream->buffer),
      static_cast<unsigned int>(cdr_stream->buffer_length)) != RTI_TRUE)
  {
    fprintf(stderr, "deserialize from cdr buffer failed\n");
    return false;
  }
  bool success = _TargetGrid__convert_dds_to_ros(dds_message, untyped_ros_message);
  if (ssafy_msgs::msg::dds_::TargetGrid_TypeSupport::delete_data(dds_message) != DDS_RETCODE_OK) {
    return false;
  }
  return success;
}

static message_type_support_callbacks_t _TargetGrid__callbacks = {
  "ssafy_msgs::msg",  // message_namespace
  "TargetGrid",  // message_name
  _TargetGrid__get_type_code,  // get_type_code
  _TargetGrid__convert_ros_to_dds,  // convert_ros_to_dds
  _TargetGrid__convert_dds_to_ros,  // convert_dds_to_ros
  _TargetGrid__to_cdr_stream,  // to_cdr_stream
  _TargetGrid__to_message  // to_message
};

static rosidl_message_type_support_t _TargetGrid__type_support = {
  rosidl_typesupport_connext_c__identifier,
  &_TargetGrid__callbacks,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_connext_c,
  ssafy_msgs, msg,
  TargetGrid)()
{
  return &_TargetGrid__type_support;
}

#if defined(__cplusplus)
}
#endif
