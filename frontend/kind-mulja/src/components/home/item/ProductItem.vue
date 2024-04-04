<template>
  <div class="product-item">
    <slot name="item-img">
      <!-- 상품 이미지가 출력되는 곳 -->
    </slot>

    <slot name="item-title">
      <!-- 상품 제목이 출력되는 곳 -->
    </slot>

    <slot name="item-price">
      <!-- 상품 가격이 출력되는 곳 -->
    </slot>

    <slot name="item-description">
      <!-- 상품 가격이 출력되는 곳 -->
    </slot>
    <slot name="item-size">
      <!-- 상품 가격이 출력되는 곳 -->
    </slot>
  </div>
</template>

<script setup></script>

<style scoped></style>
