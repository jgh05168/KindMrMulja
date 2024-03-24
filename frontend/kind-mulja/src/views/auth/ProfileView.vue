<template>
  <div>
    <h1 @click="router.push({ name: 'cart' })">주문 목록</h1>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<style scoped></style>
