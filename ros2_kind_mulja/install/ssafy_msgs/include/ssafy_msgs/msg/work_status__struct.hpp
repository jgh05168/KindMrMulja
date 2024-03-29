// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ssafy_msgs:msg\WorkStatus.idl
// generated code does not contain a copyright notice

#ifndef SSAFY_MSGS__MSG__WORK_STATUS__STRUCT_HPP_
#define SSAFY_MSGS__MSG__WORK_STATUS__STRUCT_HPP_

#include <rosidl_generator_cpp/bounded_vector.hpp>
#include <rosidl_generator_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__ssafy_msgs__msg__WorkStatus __attribute__((deprecated))
#else
# define DEPRECATED__ssafy_msgs__msg__WorkStatus __declspec(deprecated)
#endif

namespace ssafy_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WorkStatus_
{
  using Type = WorkStatus_<ContainerAllocator>;

  explicit WorkStatus_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_done = false;
      this->is_start = false;
    }
  }

  explicit WorkStatus_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_done = false;
      this->is_start = false;
    }
  }

  // field types and members
  using _is_done_type =
    bool;
  _is_done_type is_done;
  using _is_start_type =
    bool;
  _is_start_type is_start;

  // setters for named parameter idiom
  Type & set__is_done(
    const bool & _arg)
  {
    this->is_done = _arg;
    return *this;
  }
  Type & set__is_start(
    const bool & _arg)
  {
    this->is_start = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ssafy_msgs::msg::WorkStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const ssafy_msgs::msg::WorkStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ssafy_msgs::msg::WorkStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ssafy_msgs::msg::WorkStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ssafy_msgs::msg::WorkStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ssafy_msgs::msg::WorkStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ssafy_msgs::msg::WorkStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ssafy_msgs::msg::WorkStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ssafy_msgs::msg::WorkStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ssafy_msgs::msg::WorkStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ssafy_msgs__msg__WorkStatus
    std::shared_ptr<ssafy_msgs::msg::WorkStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ssafy_msgs__msg__WorkStatus
    std::shared_ptr<ssafy_msgs::msg::WorkStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WorkStatus_ & other) const
  {
    if (this->is_done != other.is_done) {
      return false;
    }
    if (this->is_start != other.is_start) {
      return false;
    }
    return true;
  }
  bool operator!=(const WorkStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WorkStatus_

// alias to use template instance with default allocator
using WorkStatus =
  ssafy_msgs::msg::WorkStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ssafy_msgs

#endif  // SSAFY_MSGS__MSG__WORK_STATUS__STRUCT_HPP_
