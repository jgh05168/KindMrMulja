<template>
  <v-card class="mb-2 cart-item" elevation="0">
    <slot name="item-check" style="width: 10%"> </slot>
    <v-avatar class="me-3" rounded="0" size="80">
      <slot name="item-image">
        <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
      </slot>
    </v-avatar>

    <div class="item-info">
      <v-card-title class="mt-2 ps-0" style="font-size: 18px">
        <slot name="item-name">상품 이름</slot>
      </v-card-title>

      <v-card-subtitle class="ps-0" style="font-size: 19px; display: flex; align-items: center">
        <v-icon class="me-1" size="xs" icon="mdi-currency-krw"></v-icon>
        <slot name="item-price">상품 가격</slot>
      </v-card-subtitle>

      <v-card-actions class="pt-0 ps-0">
        <slot name="item-cnt"></slot>
      </v-card-actions>
    </div>

    <div style="position: absolute; top: 35%; right: 1%">
      <slot name="cancel-btn"></slot>
    </div>
  </v-card>
</template>

<script setup>
import { defineProps, watch } from 'vue'
import Service from '@/api/api'

const props = defineProps({
  cartId: Number,
  itemQuentity: Number
})

watch(
  () => props.itemQuentity,
  (newValue, oldValue) => {
    // props.productQuentity 값이 변경될 때 실행되는 로직
    console.log('productQuentity 변경:', oldValue, '->', newValue)
    // 업데이트 함수 실행
    Service.cartUpdate(props.cartId, newValue)
  }
)
</script>

<style scoped>
.cart-item {
  position: relative;
  display: flex;
  width: 95%;
  margin: 5px auto;
  height: 100px;
  align-items: center;
  border: 1px solid gray;
}

.item_info {
  height: 100px;
  overflow: hidden;
}
</style>
