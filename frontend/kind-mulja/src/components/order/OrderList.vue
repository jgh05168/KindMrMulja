<template>
  <v-card class="mx-auto mt-4" style="border: 1px solid grey" max-width="90%">
    <v-card-title style="display: flex; flex-direction: row; justify-content: space-between">
      <span>No.{{ props.orderBundle.order_id }}</span>
      <span>주문일자 : {{ props.orderBundle.order_date.slice(0, 10) }}</span>
    </v-card-title>
    <CartItem
      v-for="item in order_item_list"
      :key="item.order_detail_id"
      :value="item.product_id"
      :item-quentity="item.order_quentity"
      style="border: none"
    >
      <template #item-image>
        <v-img :src="`/product/${item.product_id}.jpg`"></v-img>
      </template>
      <template #item-name>{{ item.product_name }}</template>
      <template #item-price>{{ item.product_price }}</template>
      <template #item-cnt>
        <span>{{ item.order_quentity }} 개</span>
      </template>
    </CartItem>
    <v-card-text>
      <OrderMsg
        :order-state="props.orderBundle.order_state"
        :order-type="props.orderBundle.order_type"
      />
    </v-card-text>
  </v-card>
</template>

<script setup>
import { defineProps, onMounted, ref } from 'vue'
import CartItem from '../cart/CartItem.vue'
import OrderMsg from '@/components/order/OrderMsg.vue'
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
