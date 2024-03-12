<template>
  <v-card width="360" class="mx-auto mt-10">
    <v-card-title>
      <slot name="address-title" :editAddress="editAddress"></slot>
    </v-card-title>
    <v-divider class="border-opacity-50" color="success"></v-divider>
    <v-card-text>
      <slot name="address-detail"></slot>
    </v-card-text>
  </v-card>
</template>

<script setup>
const editAddress = (address_id) => {
  // 주소지 수정하는 페이지로 이동
  console.log(address_id, '번 주소지 수정 페이지로 이동')
}
</script>

<style scoped></style>
