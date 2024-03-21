import { ref, computed } from 'vue'
import { defineStore } from 'pinia'


export const useOrderStore = defineStore('order', () => {
    const selected_item = ref([]) // 장바구니에서 선택된 상품들 리스트
    const order_type = ref(0) // 0 : 배송, 1 : 픽업
    const item_price = ref(0)
    const delivery_price = ref(0)
    const total_price = ref(0) 
    const address_list = ref([])
    const default_id = computed(() => {
      return address_list.value.find(address => address.is_default === 1).address_id;
    })

    const selected_cart_id = computed(() => {
      if (selected_item.value && selected_item.value.length > 0) {
        return selected_item.value.map(item => item.cart_id);
      }
      else {
        return null
      }
    })

  return { selected_item, order_type,
  item_price,delivery_price,total_price, address_list,
  selected_cart_id,default_id}
}, { persist: true })
