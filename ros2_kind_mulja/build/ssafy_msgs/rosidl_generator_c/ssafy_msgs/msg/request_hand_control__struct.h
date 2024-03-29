// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ssafy_msgs:msg\RequestHandControl.idl
// generated code does not contain a copyright notice

#ifndef SSAFY_MSGS__MSG__REQUEST_HAND_CONTROL__STRUCT_H_
#define SSAFY_MSGS__MSG__REQUEST_HAND_CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/RequestHandControl in the package ssafy_msgs.
typedef struct ssafy_msgs__msg__RequestHandControl
{
  uint8_t control_mode;
} ssafy_msgs__msg__RequestHandControl;

// Struct for a sequence of ssafy_msgs__msg__RequestHandControl.
typedef struct ssafy_msgs__msg__RequestHandControl__Sequence
{
  ssafy_msgs__msg__RequestHandControl * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ssafy_msgs__msg__RequestHandControl__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SSAFY_MSGS__MSG__REQUEST_HAND_CONTROL__STRUCT_H_
