// generated from rosidl_typesupport_connext_cpp/resource/idl__dds_connext__type_support.cpp.em
// with input from ssafy_msgs:msg\TargetGrid.idl
// generated code does not contain a copyright notice

#include <limits>
#include <stdexcept>

#include "ssafy_msgs/msg/target_grid__rosidl_typesupport_connext_cpp.hpp"
#include "rcutils/types/uint8_array.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_connext_cpp/identifier.hpp"
#include "rosidl_typesupport_connext_cpp/message_type_support.h"
#include "rosidl_typesupport_connext_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_connext_cpp/wstring_conversion.hpp"

// forward declaration of message dependencies and their conversion functions


namespace ssafy_msgs
{

namespace msg
{

namespace typesupport_connext_cpp
{


DDS_TypeCode *
get_type_code__TargetGrid()
{
  return ssafy_msgs::msg::dds_::TargetGrid_TypeSupport::get_typecode();
}

bool
convert_ros_message_to_dds(
  const ssafy_msgs::msg::TargetGrid & ros_message,
  ssafy_msgs::msg::dds_::TargetGrid_ & dds_message)
{
  // member.name product_x
  dds_message.product_x_ =
    ros_message.product_x;

  // member.name product_y
  dds_message.product_y_ =
    ros_message.product_y;

  // member.name moving_zone_x
  dds_message.moving_zone_x_ =
    ros_message.moving_zone_x;

  // member.name moving_zone_y
  dds_message.moving_zone_y_ =
    ros_message.moving_zone_y;

  // member.name charge_x
  dds_message.charge_x_ =
    ros_message.charge_x;

  // member.name charge_y
  dds_message.charge_y_ =
    ros_message.charge_y;

  return true;
}

bool
convert_dds_message_to_ros(
  const ssafy_msgs::msg::dds_::TargetGrid_ & dds_message,
  ssafy_msgs::msg::TargetGrid & ros_message)
{
  // member.name product_x
  ros_message.product_x =
    dds_message.product_x_;

  // member.name product_y
  ros_message.product_y =
    dds_message.product_y_;

  // member.name moving_zone_x
  ros_message.moving_zone_x =
    dds_message.moving_zone_x_;

  // member.name moving_zone_y
  ros_message.moving_zone_y =
    dds_message.moving_zone_y_;

  // member.name charge_x
  ros_message.charge_x =
    dds_message.charge_x_;

  // member.name charge_y
  ros_message.charge_y =
    dds_message.charge_y_;

  return true;
}

bool
to_cdr_stream__TargetGrid(
  const void * untyped_ros_message,
  rcutils_uint8_array_t * cdr_stream)
{
  if (!cdr_stream) {
    return false;
  }
  if (!untyped_ros_message) {
    return false;
  }

  // cast the untyped to the known ros message
  const ssafy_msgs::msg::TargetGrid & ros_message =
    *(const ssafy_msgs::msg::TargetGrid *)untyped_ros_message;

  // create a respective connext dds type
  ssafy_msgs::msg::dds_::TargetGrid_ * dds_message = ssafy_msgs::msg::dds_::TargetGrid_TypeSupport::create_data();
  if (!dds_message) {
    return false;
  }

  // convert ros to dds
  if (!convert_ros_message_to_dds(ros_message, *dds_message)) {
    return false;
  }

  // call the serialize function for the first time to get the expected length of the message
  unsigned int expected_length;
  if (ssafy_msgs::msg::dds_::TargetGrid_Plugin_serialize_to_cdr_buffer(
      NULL,
      &expected_length,
      dds_message) != RTI_TRUE)
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
      dds_message) != RTI_TRUE)
  {
    return false;
  }
  if (ssafy_msgs::msg::dds_::TargetGrid_TypeSupport::delete_data(dds_message) != DDS_RETCODE_OK) {
    return false;
  }
  return true;
}

bool
to_message__TargetGrid(
  const rcutils_uint8_array_t * cdr_stream,
  void * untyped_ros_message)
{
  if (!cdr_stream) {
    return false;
  }
  if (!cdr_stream->buffer) {
    fprintf(stderr, "cdr stream doesn't contain data\n");
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

  ssafy_msgs::msg::TargetGrid & ros_message =
    *(ssafy_msgs::msg::TargetGrid *)untyped_ros_message;
  bool success = convert_dds_message_to_ros(*dds_message, ros_message);
  if (ssafy_msgs::msg::dds_::TargetGrid_TypeSupport::delete_data(dds_message) != DDS_RETCODE_OK) {
    return false;
  }
  return success;
}

static message_type_support_callbacks_t _TargetGrid__callbacks = {
  "ssafy_msgs::msg",
  "TargetGrid",
  &get_type_code__TargetGrid,
  nullptr,
  nullptr,
  &to_cdr_stream__TargetGrid,
  &to_message__TargetGrid
};

static rosidl_message_type_support_t _TargetGrid__handle = {
  rosidl_typesupport_connext_cpp::typesupport_identifier,
  &_TargetGrid__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_connext_cpp

}  // namespace msg

}  // namespace ssafy_msgs


namespace rosidl_typesupport_connext_cpp
{

template<>
ROSIDL_TYPESUPPORT_CONNEXT_CPP_EXPORT_ssafy_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<ssafy_msgs::msg::TargetGrid>()
{
  return &ssafy_msgs::msg::typesupport_connext_cpp::_TargetGrid__handle;
}

}  // namespace rosidl_typesupport_connext_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_connext_cpp,
  ssafy_msgs, msg,
  TargetGrid)()
{
  return &ssafy_msgs::msg::typesupport_connext_cpp::_TargetGrid__handle;
}

#ifdef __cplusplus
}
#endif
