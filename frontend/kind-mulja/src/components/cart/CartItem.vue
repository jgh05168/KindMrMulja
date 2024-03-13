<template>
  <v-card class="mb-auto" style="position: relative">
    <div class="d-flex flex-no-wrap">
      <v-avatar class="ma-3" rounded="0" size="125">
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

<script setup></script>

<style scoped></style>
