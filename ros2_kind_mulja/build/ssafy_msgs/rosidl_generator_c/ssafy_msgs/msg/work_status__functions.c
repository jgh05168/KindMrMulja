// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ssafy_msgs:msg\WorkStatus.idl
// generated code does not contain a copyright notice
#include "ssafy_msgs/msg/work_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
ssafy_msgs__msg__WorkStatus__init(ssafy_msgs__msg__WorkStatus * msg)
{
  if (!msg) {
    return false;
  }
  // is_done
  // is_start
  return true;
}

void
ssafy_msgs__msg__WorkStatus__fini(ssafy_msgs__msg__WorkStatus * msg)
{
  if (!msg) {
    return;
  }
  // is_done
  // is_start
}

ssafy_msgs__msg__WorkStatus *
ssafy_msgs__msg__WorkStatus__create()
{
  ssafy_msgs__msg__WorkStatus * msg = (ssafy_msgs__msg__WorkStatus *)malloc(sizeof(ssafy_msgs__msg__WorkStatus));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ssafy_msgs__msg__WorkStatus));
  bool success = ssafy_msgs__msg__WorkStatus__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
ssafy_msgs__msg__WorkStatus__destroy(ssafy_msgs__msg__WorkStatus * msg)
{
  if (msg) {
    ssafy_msgs__msg__WorkStatus__fini(msg);
  }
  free(msg);
}


bool
ssafy_msgs__msg__WorkStatus__Sequence__init(ssafy_msgs__msg__WorkStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  ssafy_msgs__msg__WorkStatus * data = NULL;
  if (size) {
    data = (ssafy_msgs__msg__WorkStatus *)calloc(size, sizeof(ssafy_msgs__msg__WorkStatus));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ssafy_msgs__msg__WorkStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ssafy_msgs__msg__WorkStatus__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ssafy_msgs__msg__WorkStatus__Sequence__fini(ssafy_msgs__msg__WorkStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ssafy_msgs__msg__WorkStatus__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ssafy_msgs__msg__WorkStatus__Sequence *
ssafy_msgs__msg__WorkStatus__Sequence__create(size_t size)
{
  ssafy_msgs__msg__WorkStatus__Sequence * array = (ssafy_msgs__msg__WorkStatus__Sequence *)malloc(sizeof(ssafy_msgs__msg__WorkStatus__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = ssafy_msgs__msg__WorkStatus__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
ssafy_msgs__msg__WorkStatus__Sequence__destroy(ssafy_msgs__msg__WorkStatus__Sequence * array)
{
  if (array) {
    ssafy_msgs__msg__WorkStatus__Sequence__fini(array);
  }
  free(array);
}
