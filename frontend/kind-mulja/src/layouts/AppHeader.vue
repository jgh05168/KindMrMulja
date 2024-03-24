<template>
  <div style="width: 415px; height: 50px; display: flex; flex-direction: row; align-items: center">
    <v-btn @click="router.go(-1)" icon="mdi-chevron-left" variant="plain"></v-btn>
    <span style="font-weight: bold; font-size: 25px">
      <slot name="header-bar"> </slot>
    </span>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<style scoped></style>
