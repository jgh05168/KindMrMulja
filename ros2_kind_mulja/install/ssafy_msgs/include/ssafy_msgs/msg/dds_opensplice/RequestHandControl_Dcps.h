//******************************************************************
// 
//  Generated by IDL to C++ Translator
//  
//  File name: RequestHandControl_Dcps.h
//  Source: ssafy_msgs\msg\RequestHandControl_.idl
//  Generated: timestamp removed to make the build reproducible
//  OpenSplice 6.9.190403OSS
//  
//******************************************************************
#ifndef _REQUESTHANDCONTROL_DCPS_H_
#define _REQUESTHANDCONTROL_DCPS_H_

#include "sacpp_mapping.h"
#include "dds_dcps.h"
#include "RequestHandControl_.h"
#include "ssafy_msgs/msg/rosidl_typesupport_opensplice_cpp__visibility_control.h"


namespace ssafy_msgs
{
   namespace msg
   {
      namespace dds_
      {

         class ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_ssafy_msgs RequestHandControl_TypeSupportInterface;

         typedef RequestHandControl_TypeSupportInterface * RequestHandControl_TypeSupportInterface_ptr;
         typedef DDS_DCPSInterface_var < RequestHandControl_TypeSupportInterface> RequestHandControl_TypeSupportInterface_var;
         typedef DDS_DCPSInterface_out < RequestHandControl_TypeSupportInterface> RequestHandControl_TypeSupportInterface_out;


         class ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_ssafy_msgs RequestHandControl_DataWriter;

         typedef RequestHandControl_DataWriter * RequestHandControl_DataWriter_ptr;
         typedef DDS_DCPSInterface_var < RequestHandControl_DataWriter> RequestHandControl_DataWriter_var;
         typedef DDS_DCPSInterface_out < RequestHandControl_DataWriter> RequestHandControl_DataWriter_out;


         class ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_ssafy_msgs RequestHandControl_DataReader;

         typedef RequestHandControl_DataReader * RequestHandControl_DataReader_ptr;
         typedef DDS_DCPSInterface_var < RequestHandControl_DataReader> RequestHandControl_DataReader_var;
         typedef DDS_DCPSInterface_out < RequestHandControl_DataReader> RequestHandControl_DataReader_out;


         class ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_ssafy_msgs RequestHandControl_DataReaderView;

         typedef RequestHandControl_DataReaderView * RequestHandControl_DataReaderView_ptr;
         typedef DDS_DCPSInterface_var < RequestHandControl_DataReaderView> RequestHandControl_DataReaderView_var;
         typedef DDS_DCPSInterface_out < RequestHandControl_DataReaderView> RequestHandControl_DataReaderView_out;

         struct RequestHandControl_Seq_uniq_ {};
         typedef DDS_DCPSUFLSeq < RequestHandControl_, struct RequestHandControl_Seq_uniq_> RequestHandControl_Seq;
         typedef DDS_DCPSSequence_var < RequestHandControl_Seq> RequestHandControl_Seq_var;
         typedef DDS_DCPSSequence_out < RequestHandControl_Seq> RequestHandControl_Seq_out;
         class ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_ssafy_msgs RequestHandControl_TypeSupportInterface
         :
            virtual public DDS::TypeSupport
         { 
         public:
            typedef RequestHandControl_TypeSupportInterface_ptr _ptr_type;
            typedef RequestHandControl_TypeSupportInterface_var _var_type;

            static RequestHandControl_TypeSupportInterface_ptr _duplicate (RequestHandControl_TypeSupportInterface_ptr obj);
            DDS::Boolean _local_is_a (const char * id);

            static RequestHandControl_TypeSupportInterface_ptr _narrow (DDS::Object_ptr obj);
            static RequestHandControl_TypeSupportInterface_ptr _unchecked_narrow (DDS::Object_ptr obj);
            static RequestHandControl_TypeSupportInterface_ptr _nil () { return 0; }
            static const char * _local_id;
            RequestHandControl_TypeSupportInterface_ptr _this () { return this; }


         protected:
            RequestHandControl_TypeSupportInterface () {};
            ~RequestHandControl_TypeSupportInterface () {};
         private:
            RequestHandControl_TypeSupportInterface (const RequestHandControl_TypeSupportInterface &);
            RequestHandControl_TypeSupportInterface & operator = (const RequestHandControl_TypeSupportInterface &);
         };

         class ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_ssafy_msgs RequestHandControl_DataWriter
         :
            virtual public DDS::DataWriter
         { 
         public:
            typedef RequestHandControl_DataWriter_ptr _ptr_type;
            typedef RequestHandControl_DataWriter_var _var_type;

            static RequestHandControl_DataWriter_ptr _duplicate (RequestHandControl_DataWriter_ptr obj);
            DDS::Boolean _local_is_a (const char * id);

            static RequestHandControl_DataWriter_ptr _narrow (DDS::Object_ptr obj);
            static RequestHandControl_DataWriter_ptr _unchecked_narrow (DDS::Object_ptr obj);
            static RequestHandControl_DataWriter_ptr _nil () { return 0; }
            static const char * _local_id;
            RequestHandControl_DataWriter_ptr _this () { return this; }

            virtual DDS::LongLong register_instance (const RequestHandControl_& instance_data) = 0;
            virtual DDS::LongLong register_instance_w_timestamp (const RequestHandControl_& instance_data, const DDS::Time_t& source_timestamp) = 0;
            virtual DDS::Long unregister_instance (const RequestHandControl_& instance_data, DDS::LongLong handle) = 0;
            virtual DDS::Long unregister_instance_w_timestamp (const RequestHandControl_& instance_data, DDS::LongLong handle, const DDS::Time_t& source_timestamp) = 0;
            virtual DDS::Long write (const RequestHandControl_& instance_data, DDS::LongLong handle) = 0;
            virtual DDS::Long write_w_timestamp (const RequestHandControl_& instance_data, DDS::LongLong handle, const DDS::Time_t& source_timestamp) = 0;
            virtual DDS::Long dispose (const RequestHandControl_& instance_data, DDS::LongLong handle) = 0;
            virtual DDS::Long dispose_w_timestamp (const RequestHandControl_& instance_data, DDS::LongLong handle, const DDS::Time_t& source_timestamp) = 0;
            virtual DDS::Long writedispose (const RequestHandControl_& instance_data, DDS::LongLong handle) = 0;
            virtual DDS::Long writedispose_w_timestamp (const RequestHandControl_& instance_data, DDS::LongLong handle, const DDS::Time_t& source_timestamp) = 0;
            virtual DDS::Long get_key_value (RequestHandControl_& key_holder, DDS::LongLong handle) = 0;
            virtual DDS::LongLong lookup_instance (const RequestHandControl_& instance_data) = 0;

         protected:
            RequestHandControl_DataWriter () {};
            ~RequestHandControl_DataWriter () {};
         private:
            RequestHandControl_DataWriter (const RequestHandControl_DataWriter &);
            RequestHandControl_DataWriter & operator = (const RequestHandControl_DataWriter &);
         };

         class ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_ssafy_msgs RequestHandControl_DataReader
         :
            virtual public DDS::DataReader
         { 
         public:
            typedef RequestHandControl_DataReader_ptr _ptr_type;
            typedef RequestHandControl_DataReader_var _var_type;

            static RequestHandControl_DataReader_ptr _duplicate (RequestHandControl_DataReader_ptr obj);
            DDS::Boolean _local_is_a (const char * id);

            static RequestHandControl_DataReader_ptr _narrow (DDS::Object_ptr obj);
            static RequestHandControl_DataReader_ptr _unchecked_narrow (DDS::Object_ptr obj);
            static RequestHandControl_DataReader_ptr _nil () { return 0; }
            static const char * _local_id;
            RequestHandControl_DataReader_ptr _this () { return this; }

            virtual DDS::Long read (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long take (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long read_w_condition (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::ReadCondition_ptr a_condition) = 0;
            virtual DDS::Long take_w_condition (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::ReadCondition_ptr a_condition) = 0;
            virtual DDS::Long read_next_sample (RequestHandControl_& received_data, DDS::SampleInfo& sample_info) = 0;
            virtual DDS::Long take_next_sample (RequestHandControl_& received_data, DDS::SampleInfo& sample_info) = 0;
            virtual DDS::Long read_instance (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long take_instance (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long read_next_instance (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long take_next_instance (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long read_next_instance_w_condition (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ReadCondition_ptr a_condition) = 0;
            virtual DDS::Long take_next_instance_w_condition (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ReadCondition_ptr a_condition) = 0;
            virtual DDS::Long return_loan (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq) = 0;
            virtual DDS::Long get_key_value (RequestHandControl_& key_holder, DDS::LongLong handle) = 0;
            virtual DDS::LongLong lookup_instance (const RequestHandControl_& instance) = 0;

         protected:
            RequestHandControl_DataReader () {};
            ~RequestHandControl_DataReader () {};
         private:
            RequestHandControl_DataReader (const RequestHandControl_DataReader &);
            RequestHandControl_DataReader & operator = (const RequestHandControl_DataReader &);
         };

         class ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_ssafy_msgs RequestHandControl_DataReaderView
         :
            virtual public DDS::DataReaderView
         { 
         public:
            typedef RequestHandControl_DataReaderView_ptr _ptr_type;
            typedef RequestHandControl_DataReaderView_var _var_type;

            static RequestHandControl_DataReaderView_ptr _duplicate (RequestHandControl_DataReaderView_ptr obj);
            DDS::Boolean _local_is_a (const char * id);

            static RequestHandControl_DataReaderView_ptr _narrow (DDS::Object_ptr obj);
            static RequestHandControl_DataReaderView_ptr _unchecked_narrow (DDS::Object_ptr obj);
            static RequestHandControl_DataReaderView_ptr _nil () { return 0; }
            static const char * _local_id;
            RequestHandControl_DataReaderView_ptr _this () { return this; }

            virtual DDS::Long read (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long take (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long read_w_condition (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::ReadCondition_ptr a_condition) = 0;
            virtual DDS::Long take_w_condition (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::ReadCondition_ptr a_condition) = 0;
            virtual DDS::Long read_next_sample (RequestHandControl_& received_data, DDS::SampleInfo& sample_info) = 0;
            virtual DDS::Long take_next_sample (RequestHandControl_& received_data, DDS::SampleInfo& sample_info) = 0;
            virtual DDS::Long read_instance (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long take_instance (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long read_next_instance (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long take_next_instance (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ULong sample_states, DDS::ULong view_states, DDS::ULong instance_states) = 0;
            virtual DDS::Long read_next_instance_w_condition (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ReadCondition_ptr a_condition) = 0;
            virtual DDS::Long take_next_instance_w_condition (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq, DDS::Long max_samples, DDS::LongLong a_handle, DDS::ReadCondition_ptr a_condition) = 0;
            virtual DDS::Long return_loan (RequestHandControl_Seq& received_data, DDS::SampleInfoSeq& info_seq) = 0;
            virtual DDS::Long get_key_value (RequestHandControl_& key_holder, DDS::LongLong handle) = 0;
            virtual DDS::LongLong lookup_instance (const RequestHandControl_& instance) = 0;

         protected:
            RequestHandControl_DataReaderView () {};
            ~RequestHandControl_DataReaderView () {};
         private:
            RequestHandControl_DataReaderView (const RequestHandControl_DataReaderView &);
            RequestHandControl_DataReaderView & operator = (const RequestHandControl_DataReaderView &);
         };

      }
   }
}




#endif
