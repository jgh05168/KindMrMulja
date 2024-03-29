// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ssafy_msgs:msg\TargetGrid.idl
// generated code does not contain a copyright notice

#ifndef SSAFY_MSGS__MSG__TARGET_GRID__STRUCT_HPP_
#define SSAFY_MSGS__MSG__TARGET_GRID__STRUCT_HPP_

#include <rosidl_generator_cpp/bounded_vector.hpp>
#include <rosidl_generator_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__ssafy_msgs__msg__TargetGrid __attribute__((deprecated))
#else
# define DEPRECATED__ssafy_msgs__msg__TargetGrid __declspec(deprecated)
#endif

namespace ssafy_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TargetGrid_
{
  using Type = TargetGrid_<ContainerAllocator>;

  explicit TargetGrid_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->product_x = 0.0;
      this->product_y = 0.0;
      this->moving_zone_x = 0.0;
      this->moving_zone_y = 0.0;
      this->charge_x = 0.0;
      this->charge_y = 0.0;
    }
  }

  explicit TargetGrid_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->product_x = 0.0;
      this->product_y = 0.0;
      this->moving_zone_x = 0.0;
      this->moving_zone_y = 0.0;
      this->charge_x = 0.0;
      this->charge_y = 0.0;
    }
  }

  // field types and members
  using _product_x_type =
    double;
  _product_x_type product_x;
  using _product_y_type =
    double;
  _product_y_type product_y;
  using _moving_zone_x_type =
    double;
  _moving_zone_x_type moving_zone_x;
  using _moving_zone_y_type =
    double;
  _moving_zone_y_type moving_zone_y;
  using _charge_x_type =
    double;
  _charge_x_type charge_x;
  using _charge_y_type =
    double;
  _charge_y_type charge_y;

  // setters for named parameter idiom
  Type & set__product_x(
    const double & _arg)
  {
    this->product_x = _arg;
    return *this;
  }
  Type & set__product_y(
    const double & _arg)
  {
    this->product_y = _arg;
    return *this;
  }
  Type & set__moving_zone_x(
    const double & _arg)
  {
    this->moving_zone_x = _arg;
    return *this;
  }
  Type & set__moving_zone_y(
    const double & _arg)
  {
    this->moving_zone_y = _arg;
    return *this;
  }
  Type & set__charge_x(
    const double & _arg)
  {
    this->charge_x = _arg;
    return *this;
  }
  Type & set__charge_y(
    const double & _arg)
  {
    this->charge_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ssafy_msgs::msg::TargetGrid_<ContainerAllocator> *;
  using ConstRawPtr =
    const ssafy_msgs::msg::TargetGrid_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ssafy_msgs::msg::TargetGrid_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ssafy_msgs::msg::TargetGrid_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ssafy_msgs::msg::TargetGrid_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ssafy_msgs::msg::TargetGrid_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ssafy_msgs::msg::TargetGrid_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ssafy_msgs::msg::TargetGrid_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ssafy_msgs::msg::TargetGrid_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ssafy_msgs::msg::TargetGrid_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ssafy_msgs__msg__TargetGrid
    std::shared_ptr<ssafy_msgs::msg::TargetGrid_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ssafy_msgs__msg__TargetGrid
    std::shared_ptr<ssafy_msgs::msg::TargetGrid_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TargetGrid_ & other) const
  {
    if (this->product_x != other.product_x) {
      return false;
    }
    if (this->product_y != other.product_y) {
      return false;
    }
    if (this->moving_zone_x != other.moving_zone_x) {
      return false;
    }
    if (this->moving_zone_y != other.moving_zone_y) {
      return false;
    }
    if (this->charge_x != other.charge_x) {
      return false;
    }
    if (this->charge_y != other.charge_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const TargetGrid_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TargetGrid_

// alias to use template instance with default allocator
using TargetGrid =
  ssafy_msgs::msg::TargetGrid_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ssafy_msgs

#endif  // SSAFY_MSGS__MSG__TARGET_GRID__STRUCT_HPP_
