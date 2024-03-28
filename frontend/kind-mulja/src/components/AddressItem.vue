<template>
  <v-card elevation="5" rounded="xl" :width="props.width" class="mx-auto mt-5 mb-5 address-item">
    <v-card-title>
      <slot name="address-title" :editAddress="editAddress"> </slot>
    </v-card-title>
    <v-divider class="border-opacity-50" color="#757575"></v-divider>
    <v-card-text>
      <slot name="address-detail"></slot>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { defineProps } from 'vue'

const editAddress = (address_id) => {
  // 주소지 수정하는 페이지로 이동
  console.log(address_id, '번 주소지 수정 페이지로 이동')
}

const props = defineProps({
  width: String
})
</script>

<style scoped>
.address-item {
  border: 1px solid #757575;
}
</style>
