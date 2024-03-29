// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ssafy_msgs:msg\TargetGrid.idl
// generated code does not contain a copyright notice
#include "ssafy_msgs/msg/target_grid__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ssafy_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ssafy_msgs/msg/target_grid__struct.h"
#include "ssafy_msgs/msg/target_grid__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _TargetGrid__ros_msg_type = ssafy_msgs__msg__TargetGrid;

static bool _TargetGrid__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TargetGrid__ros_msg_type * ros_message = static_cast<const _TargetGrid__ros_msg_type *>(untyped_ros_message);
  // Field name: product_x
  {
    cdr << ros_message->product_x;
  }

  // Field name: product_y
  {
    cdr << ros_message->product_y;
  }

  // Field name: moving_zone_x
  {
    cdr << ros_message->moving_zone_x;
  }

  // Field name: moving_zone_y
  {
    cdr << ros_message->moving_zone_y;
  }

  // Field name: charge_x
  {
    cdr << ros_message->charge_x;
  }

  // Field name: charge_y
  {
    cdr << ros_message->charge_y;
  }

  return true;
}

static bool _TargetGrid__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TargetGrid__ros_msg_type * ros_message = static_cast<_TargetGrid__ros_msg_type *>(untyped_ros_message);
  // Field name: product_x
  {
    cdr >> ros_message->product_x;
  }

  // Field name: product_y
  {
    cdr >> ros_message->product_y;
  }

  // Field name: moving_zone_x
  {
    cdr >> ros_message->moving_zone_x;
  }

  // Field name: moving_zone_y
  {
    cdr >> ros_message->moving_zone_y;
  }

  // Field name: charge_x
  {
    cdr >> ros_message->charge_x;
  }

  // Field name: charge_y
  {
    cdr >> ros_message->charge_y;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ssafy_msgs
size_t get_serialized_size_ssafy_msgs__msg__TargetGrid(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TargetGrid__ros_msg_type * ros_message = static_cast<const _TargetGrid__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name product_x
  {
    size_t item_size = sizeof(ros_message->product_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name product_y
  {
    size_t item_size = sizeof(ros_message->product_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name moving_zone_x
  {
    size_t item_size = sizeof(ros_message->moving_zone_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name moving_zone_y
  {
    size_t item_size = sizeof(ros_message->moving_zone_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name charge_x
  {
    size_t item_size = sizeof(ros_message->charge_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name charge_y
  {
    size_t item_size = sizeof(ros_message->charge_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TargetGrid__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ssafy_msgs__msg__TargetGrid(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ssafy_msgs
size_t max_serialized_size_ssafy_msgs__msg__TargetGrid(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: product_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: product_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: moving_zone_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: moving_zone_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: charge_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: charge_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _TargetGrid__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ssafy_msgs__msg__TargetGrid(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_TargetGrid = {
  "ssafy_msgs::msg",
  "TargetGrid",
  _TargetGrid__cdr_serialize,
  _TargetGrid__cdr_deserialize,
  _TargetGrid__get_serialized_size,
  _TargetGrid__max_serialized_size
};

static rosidl_message_type_support_t _TargetGrid__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TargetGrid,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ssafy_msgs, msg, TargetGrid)() {
  return &_TargetGrid__type_support;
}

#if defined(__cplusplus)
}
#endif
