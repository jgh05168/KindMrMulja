// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ssafy_msgs:msg\WorkStatus.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_generator_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ssafy_msgs/msg/work_status__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ssafy_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void WorkStatus_init_function(
  void * message_memory, rosidl_generator_cpp::MessageInitialization _init)
{
  new (message_memory) ssafy_msgs::msg::WorkStatus(_init);
}

void WorkStatus_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ssafy_msgs::msg::WorkStatus *>(message_memory);
  typed_message->~WorkStatus();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember WorkStatus_message_member_array[2] = {
  {
    "is_done",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ssafy_msgs::msg::WorkStatus, is_done),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "is_start",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ssafy_msgs::msg::WorkStatus, is_start),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers WorkStatus_message_members = {
  "ssafy_msgs::msg",  // message namespace
  "WorkStatus",  // message name
  2,  // number of fields
  sizeof(ssafy_msgs::msg::WorkStatus),
  WorkStatus_message_member_array,  // message members
  WorkStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  WorkStatus_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t WorkStatus_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &WorkStatus_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace ssafy_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ssafy_msgs::msg::WorkStatus>()
{
  return &::ssafy_msgs::msg::rosidl_typesupport_introspection_cpp::WorkStatus_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ssafy_msgs, msg, WorkStatus)() {
  return &::ssafy_msgs::msg::rosidl_typesupport_introspection_cpp::WorkStatus_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
