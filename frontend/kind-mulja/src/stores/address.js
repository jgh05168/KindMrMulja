import { ref, reactive} from 'vue'
import { defineStore } from 'pinia'
// import router from '@/router'
import { useAuthStore } from '@/stores/auth';
import Service from '@/api/api';


export const useAddressStore = defineStore('address', () => {
    const authStore = useAuthStore()
    
    const state = reactive({
        address_list: [] // 주소 리스트 초기화
      })
    
    
    const getAddress = async () => {
        state.address_list = await Service.getAddress(authStore.user_id)
    }

    


  return {state, getAddress}
}, { persist: true })
