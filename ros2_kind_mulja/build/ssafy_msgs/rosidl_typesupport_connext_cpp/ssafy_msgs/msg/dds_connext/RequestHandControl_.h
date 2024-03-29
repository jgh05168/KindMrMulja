

/*
WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

This file was generated from RequestHandControl_.idl using "rtiddsgen".
The rtiddsgen tool is part of the RTI Connext distribution.
For more information, type 'rtiddsgen -help' at a command shell
or consult the RTI Connext manual.
*/

#ifndef RequestHandControl__1603364384_h
#define RequestHandControl__1603364384_h

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

            extern const char *RequestHandControl_TYPENAME;

            struct RequestHandControl_Seq;
            #ifndef NDDS_STANDALONE_TYPE
            class RequestHandControl_TypeSupport;
            class RequestHandControl_DataWriter;
            class RequestHandControl_DataReader;
            #endif

            class RequestHandControl_ 
            {
              public:
                typedef struct RequestHandControl_Seq Seq;
                #ifndef NDDS_STANDALONE_TYPE
                typedef RequestHandControl_TypeSupport TypeSupport;
                typedef RequestHandControl_DataWriter DataWriter;
                typedef RequestHandControl_DataReader DataReader;
                #endif

                DDS_Octet   control_mode_ ;

            };
            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT_ssafy_msgs)
            /* If the code is building on Windows, start exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport __declspec(dllexport)
            #endif

            NDDSUSERDllExport DDS_TypeCode* RequestHandControl__get_typecode(void); /* Type code */

            DDS_SEQUENCE(RequestHandControl_Seq, RequestHandControl_);

            NDDSUSERDllExport
            RTIBool RequestHandControl__initialize(
                RequestHandControl_* self);

            NDDSUSERDllExport
            RTIBool RequestHandControl__initialize_ex(
                RequestHandControl_* self,RTIBool allocatePointers,RTIBool allocateMemory);

            NDDSUSERDllExport
            RTIBool RequestHandControl__initialize_w_params(
                RequestHandControl_* self,
                const struct DDS_TypeAllocationParams_t * allocParams);  

            NDDSUSERDllExport
            void RequestHandControl__finalize(
                RequestHandControl_* self);

            NDDSUSERDllExport
            void RequestHandControl__finalize_ex(
                RequestHandControl_* self,RTIBool deletePointers);

            NDDSUSERDllExport
            void RequestHandControl__finalize_w_params(
                RequestHandControl_* self,
                const struct DDS_TypeDeallocationParams_t * deallocParams);

            NDDSUSERDllExport
            void RequestHandControl__finalize_optional_members(
                RequestHandControl_* self, RTIBool deletePointers);  

            NDDSUSERDllExport
            RTIBool RequestHandControl__copy(
                RequestHandControl_* dst,
                const RequestHandControl_* src);

            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT_ssafy_msgs)
            /* If the code is building on Windows, stop exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport
            #endif
        } /* namespace dds_  */
    } /* namespace msg  */
} /* namespace ssafy_msgs  */

#endif /* RequestHandControl_ */

