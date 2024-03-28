import { ref } from 'vue'
import { defineStore } from 'pinia'
import router from '@/router'
import { useProductStore } from './product'

export const useAuthStore = defineStore('auth', () => {
  const productStore = useProductStore()
  const user_id = ref(null)
  const redirectUrl = ref(null)


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
        router.push({name:'home'})

      }

    


  return { user_id , redirectUrl, logout }
}, { persist: true })
