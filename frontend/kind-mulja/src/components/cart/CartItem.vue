<template>
  <v-card class="mb-auto" style="position: relative; display: flex; flex-direction: row">
    <div class="d-flex flex-no-wrap">
      <slot name="item-check"> </slot>
      <v-avatar class="ma-3" rounded="0" size="95">
        <slot name="item-image">
          <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
        </slot>
      </v-avatar>

      <div>
        <v-card-title class="ps-0" style="font-size: 20px">
          <slot name="item-name">상품 이름</slot>
        </v-card-title>

        <v-card-subtitle class="ps-0" style="font-size: 15px">
          <v-icon size="xs" icon="mdi-currency-krw"></v-icon>
          <slot name="item-price">상품 가격</slot>
        </v-card-subtitle>

        <v-card-actions class="ps-0 mt-5">
          <slot name="item-cnt">수량 조절 버튼</slot>
        </v-card-actions>
      </div>
    </div>

    <div style="position: absolute; top: 10%; right: 5%">
      <slot name="cancel-btn">X</slot>
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

<style scoped></style>
