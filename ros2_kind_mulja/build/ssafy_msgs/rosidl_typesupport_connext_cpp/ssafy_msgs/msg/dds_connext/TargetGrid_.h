

/*
WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

This file was generated from TargetGrid_.idl using "rtiddsgen".
The rtiddsgen tool is part of the RTI Connext distribution.
For more information, type 'rtiddsgen -help' at a command shell
or consult the RTI Connext manual.
*/

#ifndef TargetGrid__1828626421_h
#define TargetGrid__1828626421_h

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

            extern const char *TargetGrid_TYPENAME;

            struct TargetGrid_Seq;
            #ifndef NDDS_STANDALONE_TYPE
            class TargetGrid_TypeSupport;
            class TargetGrid_DataWriter;
            class TargetGrid_DataReader;
            #endif

            class TargetGrid_ 
            {
              public:
                typedef struct TargetGrid_Seq Seq;
                #ifndef NDDS_STANDALONE_TYPE
                typedef TargetGrid_TypeSupport TypeSupport;
                typedef TargetGrid_DataWriter DataWriter;
                typedef TargetGrid_DataReader DataReader;
                #endif

                DDS_Double   product_x_ ;
                DDS_Double   product_y_ ;
                DDS_Double   moving_zone_x_ ;
                DDS_Double   moving_zone_y_ ;
                DDS_Double   charge_x_ ;
                DDS_Double   charge_y_ ;

            };
            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT_ssafy_msgs)
            /* If the code is building on Windows, start exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport __declspec(dllexport)
            #endif

            NDDSUSERDllExport DDS_TypeCode* TargetGrid__get_typecode(void); /* Type code */

            DDS_SEQUENCE(TargetGrid_Seq, TargetGrid_);

            NDDSUSERDllExport
            RTIBool TargetGrid__initialize(
                TargetGrid_* self);

            NDDSUSERDllExport
            RTIBool TargetGrid__initialize_ex(
                TargetGrid_* self,RTIBool allocatePointers,RTIBool allocateMemory);

            NDDSUSERDllExport
            RTIBool TargetGrid__initialize_w_params(
                TargetGrid_* self,
                const struct DDS_TypeAllocationParams_t * allocParams);  

            NDDSUSERDllExport
            void TargetGrid__finalize(
                TargetGrid_* self);

            NDDSUSERDllExport
            void TargetGrid__finalize_ex(
                TargetGrid_* self,RTIBool deletePointers);

            NDDSUSERDllExport
            void TargetGrid__finalize_w_params(
                TargetGrid_* self,
                const struct DDS_TypeDeallocationParams_t * deallocParams);

            NDDSUSERDllExport
            void TargetGrid__finalize_optional_members(
                TargetGrid_* self, RTIBool deletePointers);  

            NDDSUSERDllExport
            RTIBool TargetGrid__copy(
                TargetGrid_* dst,
                const TargetGrid_* src);

            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT_ssafy_msgs)
            /* If the code is building on Windows, stop exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport
            #endif
        } /* namespace dds_  */
    } /* namespace msg  */
} /* namespace ssafy_msgs  */

#endif /* TargetGrid_ */

