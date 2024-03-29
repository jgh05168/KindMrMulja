// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ssafy_msgs:msg\TargetGrid.idl
// generated code does not contain a copyright notice

#ifndef SSAFY_MSGS__MSG__TARGET_GRID__TRAITS_HPP_
#define SSAFY_MSGS__MSG__TARGET_GRID__TRAITS_HPP_

#include "ssafy_msgs/msg/target_grid__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ssafy_msgs::msg::TargetGrid>()
{
  return "ssafy_msgs::msg::TargetGrid";
}

template<>
struct has_fixed_size<ssafy_msgs::msg::TargetGrid>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<ssafy_msgs::msg::TargetGrid>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<ssafy_msgs::msg::TargetGrid>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SSAFY_MSGS__MSG__TARGET_GRID__TRAITS_HPP_
