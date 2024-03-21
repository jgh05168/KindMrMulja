<template>
  <v-card class="mx-auto my-8" elevation="5" max-width="344">
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
  </v-card>
</template>

<script setup>
import { defineProps, onMounted, ref } from 'vue'
import CartItem from '../cart/CartItem.vue'
import Service from '@/api/api'

const order_item_list = ref([])

const props = defineProps({
  orderBundle: Object
})

onMounted(async () => {
  order_item_list.value = await Service.getOrderDetailList(props.orderBundle.order_id)
})
</script>

<style scoped></style>
