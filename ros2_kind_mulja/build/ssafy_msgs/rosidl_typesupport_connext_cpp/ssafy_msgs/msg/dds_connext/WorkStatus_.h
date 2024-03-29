

/*
WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

This file was generated from WorkStatus_.idl using "rtiddsgen".
The rtiddsgen tool is part of the RTI Connext distribution.
For more information, type 'rtiddsgen -help' at a command shell
or consult the RTI Connext manual.
*/

#ifndef WorkStatus__343918088_h
#define WorkStatus__343918088_h

#ifndef NDDS_STANDALONE_TYPE
#ifndef ndds_cpp_h
#include "ndds/ndds_cpp.h"
#endif
#else
#include "ndds_standalone_type.h"
#endif

namespace ssafy_msgs {
    namespace msg {
        namespace dds_ {

            extern const char *WorkStatus_TYPENAME;

            struct WorkStatus_Seq;
            #ifndef NDDS_STANDALONE_TYPE
            class WorkStatus_TypeSupport;
            class WorkStatus_DataWriter;
            class WorkStatus_DataReader;
            #endif

            class WorkStatus_ 
            {
              public:
                typedef struct WorkStatus_Seq Seq;
                #ifndef NDDS_STANDALONE_TYPE
                typedef WorkStatus_TypeSupport TypeSupport;
                typedef WorkStatus_DataWriter DataWriter;
                typedef WorkStatus_DataReader DataReader;
                #endif

                DDS_Boolean   is_done_ ;
                DDS_Boolean   is_start_ ;

            };
            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT_ssafy_msgs)
            /* If the code is building on Windows, start exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport __declspec(dllexport)
            #endif

            NDDSUSERDllExport DDS_TypeCode* WorkStatus__get_typecode(void); /* Type code */

            DDS_SEQUENCE(WorkStatus_Seq, WorkStatus_);

            NDDSUSERDllExport
            RTIBool WorkStatus__initialize(
                WorkStatus_* self);

            NDDSUSERDllExport
            RTIBool WorkStatus__initialize_ex(
                WorkStatus_* self,RTIBool allocatePointers,RTIBool allocateMemory);

            NDDSUSERDllExport
            RTIBool WorkStatus__initialize_w_params(
                WorkStatus_* self,
                const struct DDS_TypeAllocationParams_t * allocParams);  

            NDDSUSERDllExport
            void WorkStatus__finalize(
                WorkStatus_* self);

            NDDSUSERDllExport
            void WorkStatus__finalize_ex(
                WorkStatus_* self,RTIBool deletePointers);

            NDDSUSERDllExport
            void WorkStatus__finalize_w_params(
                WorkStatus_* self,
                const struct DDS_TypeDeallocationParams_t * deallocParams);

            NDDSUSERDllExport
            void WorkStatus__finalize_optional_members(
                WorkStatus_* self, RTIBool deletePointers);  

            NDDSUSERDllExport
            RTIBool WorkStatus__copy(
                WorkStatus_* dst,
                const WorkStatus_* src);

            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT_ssafy_msgs)
            /* If the code is building on Windows, stop exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport
            #endif
        } /* namespace dds_  */
    } /* namespace msg  */
} /* namespace ssafy_msgs  */

#endif /* WorkStatus_ */

