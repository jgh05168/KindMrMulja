<template>
  <div class="recipt">
    <h2>주문 내역</h2>
    <div class="items-price">
      <span>제품 가격</span>
      <div>
        <v-icon size="xs" icon="mdi-currency-krw"></v-icon>
        <slot name="items-price"> 1000 </slot>
      </div>
    </div>
    <div class="delivery-price">
      <span>배송비</span>
      <div>
        <v-icon size="xs" icon="mdi-currency-krw"></v-icon>
        <slot name="delivery-price"> 1000 </slot>
      </div>
    </div>

    <v-divider :thickness="3" class="border-opacity-100"></v-divider>

    <div class="total-price">
      <span>총 주문금액</span>
      <div>
        <v-icon size="xs" icon="mdi-currency-krw"></v-icon>
        <slot name="total-price"> 1000 </slot>
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.recipt {
  width: 90%;
  margin: auto auto;
}

.recipt > div {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.items-price {
}

.delivery-price {
}

.total-price {
}
</style>
