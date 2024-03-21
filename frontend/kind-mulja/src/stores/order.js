import { ref} from 'vue'
import { defineStore } from 'pinia'


export const useOrderStore = defineStore('order', () => {
    const selected_item = ref([]) // 장바구니에서 선택된 상품들 리스트
    const order_type = ref(0) // 0 : 배송, 1 : 픽업
    const item_price = ref(0)
    const delivery_price = ref(0)
    const total_price = ref(0) 
    const address_list = ref([])
   

  return { selected_item, order_type,
  item_price,delivery_price,total_price, address_list,
  }
}, { persist: true })
