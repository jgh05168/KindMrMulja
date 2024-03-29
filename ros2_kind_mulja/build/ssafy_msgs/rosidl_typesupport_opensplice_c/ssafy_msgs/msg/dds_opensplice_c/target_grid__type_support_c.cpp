// generated from rosidl_typesupport_opensplice_c/resource/idl__dds_opensplice__type_support.c.em
// generated code does not contain a copyright notice

#include <cassert>
#include <codecvt>
#include <cstring>
#include <iostream>
#include <limits>
#include <locale>
#include <sstream>

#include <CdrTypeSupport.h>
#include <u_instanceHandle.h>

// generated from rosidl_typesupport_opensplice_c/resource/msg__type_support_c.cpp.em
// generated code does not contain a copyright notice

#include "ssafy_msgs/msg/target_grid__rosidl_typesupport_opensplice_c.h"
#include "rosidl_typesupport_opensplice_c/identifier.h"
#include "ssafy_msgs/msg/rosidl_generator_c__visibility_control.h"
#include "rosidl_typesupport_opensplice_cpp/message_type_support.h"
#include "rosidl_typesupport_opensplice_cpp/u__instanceHandle.h"
#include "rmw/rmw.h"
#include "ssafy_msgs/msg/rosidl_typesupport_opensplice_c__visibility_control.h"
#include "ssafy_msgs/msg/target_grid.h"
#include "ssafy_msgs/msg/dds_opensplice/ccpp_TargetGrid_.h"

// includes and forward declarations of message dependencies and their conversion functions
#if defined(__cplusplus)
extern "C"
{
#endif

// include message dependencies

// forward declare type support functions

using __dds_msg_type_ssafy_msgs__msg__TargetGrid = ssafy_msgs::msg::dds_::TargetGrid_;
using __ros_msg_type_ssafy_msgs__msg__TargetGrid = ssafy_msgs__msg__TargetGrid;

static ssafy_msgs::msg::dds_::TargetGrid_TypeSupport _type_support_ssafy_msgs__msg__TargetGrid;

static const char *
register_type_ssafy_msgs__msg__TargetGrid(void * untyped_participant, const char * type_name)
{
  if (!untyped_participant) {
    return "untyped participant handle is null";
  }
  if (!type_name) {
    return "type name handle is null";
  }
  using DDS::DomainParticipant;
  DomainParticipant * participant = static_cast<DomainParticipant *>(untyped_participant);

  DDS::ReturnCode_t status = _type_support_ssafy_msgs__msg__TargetGrid.register_type(participant, type_name);
  switch (status) {
    case DDS::RETCODE_ERROR:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.register_type: "
             "an internal error has occurred";
    case DDS::RETCODE_BAD_PARAMETER:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.register_type: "
             "bad domain participant or type name parameter";
    case DDS::RETCODE_OUT_OF_RESOURCES:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.register_type: "
             "out of resources";
    case DDS::RETCODE_PRECONDITION_NOT_MET:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.register_type: "
             "already registered with a different TypeSupport class";
    case DDS::RETCODE_OK:
      return nullptr;
    default:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.register_type: unknown return code";
  }
}

static const char *
convert_ros_to_dds_ssafy_msgs__msg__TargetGrid(const void * untyped_ros_message, void * untyped_dds_message)
{
  if (!untyped_ros_message) {
    return "ros message handle is null";
  }
  if (!untyped_dds_message) {
    return "dds message handle is null";
  }
  const __ros_msg_type_ssafy_msgs__msg__TargetGrid * ros_message = static_cast<const __ros_msg_type_ssafy_msgs__msg__TargetGrid *>(untyped_ros_message);
  __dds_msg_type_ssafy_msgs__msg__TargetGrid * dds_message = static_cast<__dds_msg_type_ssafy_msgs__msg__TargetGrid *>(untyped_dds_message);
  // Field name: product_x
  {
    dds_message->product_x_ = ros_message->product_x;
  }

  // Field name: product_y
  {
    dds_message->product_y_ = ros_message->product_y;
  }

  // Field name: moving_zone_x
  {
    dds_message->moving_zone_x_ = ros_message->moving_zone_x;
  }

  // Field name: moving_zone_y
  {
    dds_message->moving_zone_y_ = ros_message->moving_zone_y;
  }

  // Field name: charge_x
  {
    dds_message->charge_x_ = ros_message->charge_x;
  }

  // Field name: charge_y
  {
    dds_message->charge_y_ = ros_message->charge_y;
  }

  return 0;
}

static const char *
publish_ssafy_msgs__msg__TargetGrid(void * dds_data_writer, const void * ros_message)
{
  if (!dds_data_writer) {
    return "data writer handle is null";
  }
  if (!ros_message) {
    return "ros message handle is null";
  }

  DDS::DataWriter * topic_writer = static_cast<DDS::DataWriter *>(dds_data_writer);

  __dds_msg_type_ssafy_msgs__msg__TargetGrid dds_message;
  const char * err_msg = convert_ros_to_dds_ssafy_msgs__msg__TargetGrid(ros_message, &dds_message);
  if (err_msg != 0) {
    return err_msg;
  }

  ssafy_msgs::msg::dds_::TargetGrid_DataWriter * data_writer =
    ssafy_msgs::msg::dds_::TargetGrid_DataWriter::_narrow(topic_writer);
  DDS::ReturnCode_t status = data_writer->write(dds_message, DDS::HANDLE_NIL);
  switch (status) {
    case DDS::RETCODE_ERROR:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataWriter.write: "
             "an internal error has occurred";
    case DDS::RETCODE_BAD_PARAMETER:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataWriter.write: "
             "bad handle or instance_data parameter";
    case DDS::RETCODE_ALREADY_DELETED:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataWriter.write: "
             "this ssafy_msgs::msg::dds_::TargetGrid_DataWriter has already been deleted";
    case DDS::RETCODE_OUT_OF_RESOURCES:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataWriter.write: "
             "out of resources";
    case DDS::RETCODE_NOT_ENABLED:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataWriter.write: "
             "this ssafy_msgs::msg::dds_::TargetGrid_DataWriter is not enabled";
    case DDS::RETCODE_PRECONDITION_NOT_MET:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataWriter.write: "
             "the handle has not been registered with this ssafy_msgs::msg::dds_::TargetGrid_DataWriter";
    case DDS::RETCODE_TIMEOUT:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataWriter.write: "
             "writing resulted in blocking and then exceeded the timeout set by the "
             "max_blocking_time of the ReliabilityQosPolicy";
    case DDS::RETCODE_OK:
      return nullptr;
    default:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataWriter.write: unknown return code";
  }
}

static const char *
convert_dds_to_ros_ssafy_msgs__msg__TargetGrid(const void * untyped_dds_message, void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    return "ros message handle is null";
  }
  if (!untyped_dds_message) {
    return "dds message handle is null";
  }
  const __dds_msg_type_ssafy_msgs__msg__TargetGrid * dds_message = static_cast<const __dds_msg_type_ssafy_msgs__msg__TargetGrid *>(untyped_dds_message);
  __ros_msg_type_ssafy_msgs__msg__TargetGrid * ros_message = static_cast<__ros_msg_type_ssafy_msgs__msg__TargetGrid *>(untyped_ros_message);
  // Field name: product_x
  {
    ros_message->product_x = dds_message->product_x_;
  }

  // Field name: product_y
  {
    ros_message->product_y = dds_message->product_y_;
  }

  // Field name: moving_zone_x
  {
    ros_message->moving_zone_x = dds_message->moving_zone_x_;
  }

  // Field name: moving_zone_y
  {
    ros_message->moving_zone_y = dds_message->moving_zone_y_;
  }

  // Field name: charge_x
  {
    ros_message->charge_x = dds_message->charge_x_;
  }

  // Field name: charge_y
  {
    ros_message->charge_y = dds_message->charge_y_;
  }

  return 0;
}

static const char *
take_ssafy_msgs__msg__TargetGrid(
  void * dds_data_reader,
  bool ignore_local_publications,
  void * untyped_ros_message,
  bool * taken,
  void * sending_publication_handle)
{
  if (untyped_ros_message == 0) {
    return "invalid ros message pointer";
  }

  DDS::DataReader * topic_reader = static_cast<DDS::DataReader *>(dds_data_reader);

  ssafy_msgs::msg::dds_::TargetGrid_DataReader * data_reader =
    ssafy_msgs::msg::dds_::TargetGrid_DataReader::_narrow(topic_reader);

  ssafy_msgs::msg::dds_::TargetGrid_Seq dds_messages;
  DDS::SampleInfoSeq sample_infos;
  DDS::ReturnCode_t status = data_reader->take(
    dds_messages,
    sample_infos,
    1,
    DDS::ANY_SAMPLE_STATE,
    DDS::ANY_VIEW_STATE,
    DDS::ANY_INSTANCE_STATE);

  const char * errs = nullptr;
  bool ignore_sample = false;

  switch (status) {
    case DDS::RETCODE_ERROR:
      errs = "ssafy_msgs::msg::dds_::TargetGrid_DataReader.take: "
        "an internal error has occurred";
      goto finally;
    case DDS::RETCODE_ALREADY_DELETED:
      errs = "ssafy_msgs::msg::dds_::TargetGrid_DataReader.take: "
        "this ssafy_msgs::msg::dds_::TargetGrid_DataReader has already been deleted";
      goto finally;
    case DDS::RETCODE_OUT_OF_RESOURCES:
      errs = "ssafy_msgs::msg::dds_::TargetGrid_DataReader.take: "
        "out of resources";
      goto finally;
    case DDS::RETCODE_NOT_ENABLED:
      errs = "ssafy_msgs::msg::dds_::TargetGrid_DataReader.take: "
        "this ssafy_msgs::msg::dds_::TargetGrid_DataReader is not enabled";
      goto finally;
    case DDS::RETCODE_PRECONDITION_NOT_MET:
      errs = "ssafy_msgs::msg::dds_::TargetGrid_DataReader.take: "
        "a precondition is not met, one of: "
        "max_samples > maximum and max_samples != LENGTH_UNLIMITED, or "
        "the two sequences do not have matching parameters (length, maximum, release), or "
        "maximum > 0 and release is false.";
      goto finally;
    case DDS::RETCODE_NO_DATA:
      *taken = false;
      errs = nullptr;
      goto finally;
    case DDS::RETCODE_OK:
      break;
    default:
      errs = "ssafy_msgs::msg::dds_::TargetGrid_DataReader.take: unknown return code";
      goto finally;
  }

  {
    DDS::SampleInfo & sample_info = sample_infos[0];
    if (!sample_info.valid_data) {
      // skip sample without data
      ignore_sample = true;
    } else {
      DDS::InstanceHandle_t sender_handle = sample_info.publication_handle;
      auto sender_gid = u_instanceHandleToGID(sender_handle);
      if (ignore_local_publications) {
        // compare the system id from the sender and this receiver
        // if they are equal the sample has been sent from this process and should be ignored
        DDS::InstanceHandle_t receiver_handle = topic_reader->get_instance_handle();
        auto receiver_gid = u_instanceHandleToGID(receiver_handle);
        ignore_sample = sender_gid.systemId == receiver_gid.systemId;
      }
      // This is nullptr when being used with plain rmw_take, so check first.
      if (sending_publication_handle) {
        *static_cast<DDS::InstanceHandle_t *>(sending_publication_handle) = sender_handle;
      }
    }
  }

  if (!ignore_sample) {
    errs = convert_dds_to_ros_ssafy_msgs__msg__TargetGrid(&dds_messages[0], untyped_ros_message);
    if (errs != 0) {
      goto finally;
    }
    *taken = true;
  } else {
    *taken = false;
  }

finally:
  // Ensure the loan is returned.
  status = data_reader->return_loan(dds_messages, sample_infos);
  switch (status) {
    case DDS::RETCODE_ERROR:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataReader.return_loan: "
             "an internal error has occurred";
    case DDS::RETCODE_ALREADY_DELETED:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataReader.return_loan: "
             "this ssafy_msgs::msg::dds_::TargetGrid_DataReader has already been deleted";
    case DDS::RETCODE_OUT_OF_RESOURCES:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataReader.return_loan: "
             "out of resources";
    case DDS::RETCODE_NOT_ENABLED:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataReader.return_loan: "
             "this ssafy_msgs::msg::dds_::TargetGrid_DataReader is not enabled";
    case DDS::RETCODE_PRECONDITION_NOT_MET:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataReader.return_loan: "
             "a precondition is not met, one of: "
             "the data_values and info_seq do not belong to a single related pair, or "
             "the data_values and info_seq were not obtained from this "
             "ssafy_msgs::msg::dds_::TargetGrid_DataReader";
    case DDS::RETCODE_OK:
      return nullptr;
    default:
      return "ssafy_msgs::msg::dds_::TargetGrid_DataReader.return_loan failed with "
             "unknown return code";
  }

  return errs;
}

static const char *
serialize_ssafy_msgs__msg__TargetGrid(
  const void * untyped_ros_message,
  void * untyped_serialized_data)
{
  if (!untyped_ros_message) {
    return "ros message handle is null";
  }
  if (!untyped_serialized_data) {
    return "serialized_data handle is null";
  }

  __dds_msg_type_ssafy_msgs__msg__TargetGrid dds_message;
  const char * err_msg = convert_ros_to_dds_ssafy_msgs__msg__TargetGrid(untyped_ros_message, &dds_message);
  if (err_msg != 0) {
    return err_msg;
  }

  DDS::OpenSplice::CdrTypeSupport cdr_ts(_type_support_ssafy_msgs__msg__TargetGrid);

  DDS::OpenSplice::CdrSerializedData * serdata = nullptr;

  DDS::ReturnCode_t status = cdr_ts.serialize(&dds_message, &serdata);
  switch (status) {
    case DDS::RETCODE_ERROR:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.serialize: "
             "an internal error has occurred";
    case DDS::RETCODE_BAD_PARAMETER:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.serialize: "
             "bad parameter";
    case DDS::RETCODE_ALREADY_DELETED:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.serialize: "
             "this ssafy_msgs::msg::dds_::TargetGrid_TypeSupport has already been deleted";
    case DDS::RETCODE_OUT_OF_RESOURCES:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.serialize: "
             "out of resources";
    case DDS::RETCODE_OK:
      break;
    default:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.serialize failed with "
             "unknown return code";
  }

  rmw_serialized_message_t * serialized_data =
    static_cast<rmw_serialized_message_t *>(untyped_serialized_data);

  auto data_length = serdata->get_size();

  if (serialized_data->buffer_capacity < data_length) {
    if (rmw_serialized_message_resize(serialized_data, data_length) == RMW_RET_OK) {
      serialized_data->buffer_capacity = data_length;
    } else {
      delete serdata;
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.serialize: "
             "unable to dynamically resize serialized message";
    }
  }

  serialized_data->buffer_length = data_length;
  serdata->get_data(serialized_data->buffer);

  delete serdata;

  return nullptr;
}

static const char *
deserialize_ssafy_msgs__msg__TargetGrid(
  const uint8_t * buffer,
  unsigned length,
  void * untyped_ros_message)
{
  const char * errs = nullptr;

  if (untyped_ros_message == 0) {
    return "invalid ros message pointer";
  }

  DDS::OpenSplice::CdrTypeSupport cdr_ts(_type_support_ssafy_msgs__msg__TargetGrid);

  __dds_msg_type_ssafy_msgs__msg__TargetGrid dds_message;
  DDS::ReturnCode_t status = cdr_ts.deserialize(buffer, length, &dds_message);

  switch (status) {
    case DDS::RETCODE_ERROR:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.deserialize: "
             "an internal error has occurred";
    case DDS::RETCODE_BAD_PARAMETER:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.deserialize: "
             "bad parameter";
    case DDS::RETCODE_ALREADY_DELETED:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.deserialize: "
             "this ssafy_msgs::msg::dds_::TargetGrid_TypeSupport has already been deleted";
    case DDS::RETCODE_OUT_OF_RESOURCES:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.deserialize: "
             "out of resources";
    case DDS::RETCODE_OK:
      break;
    default:
      return "ssafy_msgs::msg::dds_::TargetGrid_TypeSupport.deserialize failed with "
             "unknown return code";
  }

  errs = convert_dds_to_ros_ssafy_msgs__msg__TargetGrid(&dds_message, untyped_ros_message);

  return errs;
}


static message_type_support_callbacks_t TargetGrid__callbacks = {
  "ssafy_msgs::msg",  // message_namespace
  "TargetGrid",  // message_name
  register_type_ssafy_msgs__msg__TargetGrid,  // register_type
  publish_ssafy_msgs__msg__TargetGrid,  // publish
  take_ssafy_msgs__msg__TargetGrid,  // take
  serialize_ssafy_msgs__msg__TargetGrid,  // serialize message
  deserialize_ssafy_msgs__msg__TargetGrid,  // deserialize message
  convert_ros_to_dds_ssafy_msgs__msg__TargetGrid,  // convert_ros_to_dds
  convert_dds_to_ros_ssafy_msgs__msg__TargetGrid,  // convert_dds_to_ros
};

static rosidl_message_type_support_t TargetGrid__type_support = {
  rosidl_typesupport_opensplice_c__identifier,
  &TargetGrid__callbacks,  // data
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_opensplice_c,
  ssafy_msgs, msg,
  TargetGrid)()
{
  return &TargetGrid__type_support;
}

#if defined(__cplusplus)
}
#endif
