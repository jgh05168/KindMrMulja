<template>
  <div class="recipt">
    <h2>주문 내역</h2>
    <div class="items-price mt-2 price-info">
      <span>제품 가격</span>
      <div>
        <slot name="items-price"> 1000 </slot>
        <v-icon class="ms-2" size="xs" icon="mdi-currency-krw"></v-icon>
      </div>
    </div>
    <div class="delivery-price mt-2 price-info">
      <span
        >배송비<v-chip size="small" color="orange" style="font-size: 10px; z-index: 0"
          >조립 서비스일 경우 추가비용 청구</v-chip
        ></span
      >
      <div>
        <slot name="delivery-price"> 1000 </slot>
        <v-icon class="ms-2" size="xs" icon="mdi-currency-krw"></v-icon>
      </div>
    </div>

    <v-divider :thickness="3" class="border-opacity-100 mt-2"></v-divider>

    <div class="total-price mt-2 price-info">
      <span>총 주문금액</span>
      <div>
        <slot name="total-price"> 1000 </slot>
        <v-icon class="ms-2" size="xs" icon="mdi-currency-krw"></v-icon>
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

.price-info {
  font-size: 17px;
  display: flex;
  align-items: center;
}

.items-price {
}

.delivery-price {
}

.total-price {
}
</style>
