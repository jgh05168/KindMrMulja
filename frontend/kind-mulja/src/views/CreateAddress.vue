<template>
  <AppHeader>
    <template #header-bar>배송지 생성</template>
  </AppHeader>
  <AddressForm></AddressForm>
</template>

<script setup>
import AppHeader from '@/layouts/AppHeader.vue'
import AddressForm from '@/components/AddressForm.vue'
</script>

<style scoped></style>
