import { ref } from 'vue'
import { defineStore } from 'pinia'
import router from '@/router'
import { useProductStore } from './product'

export const useAuthStore = defineStore('auth', () => {
  const productStore = useProductStore()
  const user_id = ref(null)
  const user_name = ref(null)
  const allow_alarm = ref(null)
  const redirectUrl = ref(null)
  const is_admin = ref(false)



  const logout = async () => {
        user_id.value = null
        const productList = await JSON.parse(localStorage.getItem('product')).product_list
        await localStorage.clear()
        console.log(productList)

        // 전체 상품 돌면서 찜 기능을 위한 속성 초기화
        productList.forEach(async (product) => {
          product.is_zzim = false // 찜 속성 추가 및 초기화
        })

        productStore.product_list = productList
         // 앱을 새로고침
        window.location.reload();
        if (is_admin.value == 1) {
          router.push({name:'factory_map'})

        } else {
          router.push({name:'home'})
        }     
      }

    // allow_alarm 값이 바뀌면 백엔드로 권한 설정 바꾸는 요청 보내기
    const toggleAlarm = async () =>{
      allow_alarm.value = !allow_alarm.value
    }

  return { user_id ,user_name, allow_alarm, redirectUrl, logout, is_admin, toggleAlarm }
}, { persist: true })
