// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ssafy_msgs:msg\RequestHandControl.idl
// generated code does not contain a copyright notice

#ifndef SSAFY_MSGS__MSG__REQUEST_HAND_CONTROL__STRUCT_HPP_
#define SSAFY_MSGS__MSG__REQUEST_HAND_CONTROL__STRUCT_HPP_

#include <rosidl_generator_cpp/bounded_vector.hpp>
#include <rosidl_generator_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__ssafy_msgs__msg__RequestHandControl __attribute__((deprecated))
#else
# define DEPRECATED__ssafy_msgs__msg__RequestHandControl __declspec(deprecated)
#endif

namespace ssafy_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RequestHandControl_
{
  using Type = RequestHandControl_<ContainerAllocator>;

  explicit RequestHandControl_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->control_mode = 0;
    }
  }

  explicit RequestHandControl_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->control_mode = 0;
    }
  }

  // field types and members
  using _control_mode_type =
    uint8_t;
  _control_mode_type control_mode;

  // setters for named parameter idiom
  Type & set__control_mode(
    const uint8_t & _arg)
  {
    this->control_mode = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ssafy_msgs::msg::RequestHandControl_<ContainerAllocator> *;
  using ConstRawPtr =
    const ssafy_msgs::msg::RequestHandControl_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ssafy_msgs::msg::RequestHandControl_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ssafy_msgs::msg::RequestHandControl_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ssafy_msgs::msg::RequestHandControl_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ssafy_msgs::msg::RequestHandControl_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ssafy_msgs::msg::RequestHandControl_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ssafy_msgs::msg::RequestHandControl_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ssafy_msgs::msg::RequestHandControl_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ssafy_msgs::msg::RequestHandControl_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ssafy_msgs__msg__RequestHandControl
    std::shared_ptr<ssafy_msgs::msg::RequestHandControl_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ssafy_msgs__msg__RequestHandControl
    std::shared_ptr<ssafy_msgs::msg::RequestHandControl_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RequestHandControl_ & other) const
  {
    if (this->control_mode != other.control_mode) {
      return false;
    }
    return true;
  }
  bool operator!=(const RequestHandControl_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RequestHandControl_

// alias to use template instance with default allocator
using RequestHandControl =
  ssafy_msgs::msg::RequestHandControl_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ssafy_msgs

#endif  // SSAFY_MSGS__MSG__REQUEST_HAND_CONTROL__STRUCT_HPP_
