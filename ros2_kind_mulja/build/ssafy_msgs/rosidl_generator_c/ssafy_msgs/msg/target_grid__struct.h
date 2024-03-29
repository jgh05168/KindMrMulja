// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ssafy_msgs:msg\TargetGrid.idl
// generated code does not contain a copyright notice

#ifndef SSAFY_MSGS__MSG__TARGET_GRID__STRUCT_H_
#define SSAFY_MSGS__MSG__TARGET_GRID__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/TargetGrid in the package ssafy_msgs.
typedef struct ssafy_msgs__msg__TargetGrid
{
  double product_x;
  double product_y;
  double moving_zone_x;
  double moving_zone_y;
  double charge_x;
  double charge_y;
} ssafy_msgs__msg__TargetGrid;

// Struct for a sequence of ssafy_msgs__msg__TargetGrid.
typedef struct ssafy_msgs__msg__TargetGrid__Sequence
{
  ssafy_msgs__msg__TargetGrid * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ssafy_msgs__msg__TargetGrid__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SSAFY_MSGS__MSG__TARGET_GRID__STRUCT_H_
