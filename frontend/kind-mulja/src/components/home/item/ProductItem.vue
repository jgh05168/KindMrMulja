<template>
  <v-card class="product-item">
    <slot name="item-img">
      <!-- 상품 이미지가 출력되는 곳 -->
    </slot>

    <slot name="item-title">
      <!-- 상품 제목이 출력되는 곳 -->
    </slot>

    <slot name="item-price">
      <!-- 상품 가격이 출력되는 곳 -->
    </slot>
  </v-card>
</template>

<script setup></script>

<style scoped>
.product_item {
  display: flex;
  flex-direction: column;
}
</style>
