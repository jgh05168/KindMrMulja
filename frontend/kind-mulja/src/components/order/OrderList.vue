<template>
  <v-card class="mx-auto my-8" elevation="5" max-width="344">
    <v-card-title style="display: flex; flex-direction: row; justify-content: space-between">
      <span>No.{{ props.orderBundle.order_id }}</span>
      <span>주문일자 : {{ props.orderBundle.order_date.slice(0, 10) }}</span>
    </v-card-title>
    <v-divider></v-divider>
    <CartItem
      v-for="item in order_item_list"
      :key="item.order_detail_id"
      :value="item.product_id"
      :item-quentity="item.order_quentity"
    >
      <template #item-image>
        <v-img :src="`/product/${item.product_id}.jpg`"></v-img>
      </template>
      <template #item-name>{{ item.product_name }}</template>
      <template #item-price>{{ item.product_price }}</template>
      <template #item-cnt>
        <!-- 상품 수량 변경 시 DB 에도 장바구니 수량 변경 요청 보내야 함 -->
        <span>{{ item.order_quentity }}</span>
      </template>
    </CartItem>
    <v-card-text>
      {{ now_state(props.orderBundle.order_state) }}
    </v-card-text>
  </v-card>
</template>

<script setup>
import { defineProps, onMounted, ref } from 'vue'
import CartItem from '../cart/CartItem.vue'
import Service from '@/api/api'

const order_item_list = ref([])

const now_state = (state) => {
  if (state <= 1) {
    return 'processing'
  } // 값이 3 이면 배송완료
  else if (state >= 2 && state <= 3) {
    return 'delivered'
  } // 값이 4 이면 취소된 상품
  else if (state == 4) {
    return 'canceled'
  }
}

const props = defineProps({
  orderBundle: Object
})

onMounted(async () => {
  order_item_list.value = await Service.getOrderDetailList(props.orderBundle.order_id)
})
</script>

<style scoped></style>
