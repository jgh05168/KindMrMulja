<template>
  <slot name="app-footer">
    <v-layout class="overflow-visible" style="height: 56px; position: fixed">
      <v-bottom-navigation v-model="viewStore.now_value" grow>
        <v-btn @click="router.push({ name: 'home' })">
          <v-icon>mdi-home</v-icon>
        </v-btn>

        <v-btn @click="router.push({ name: 'zzim' })">
          <v-icon>mdi-heart-outline</v-icon>
        </v-btn>

        <v-btn @click="router.push({ name: 'cart' })">
          <v-icon>mdi-cart-check</v-icon>
        </v-btn>

        <v-btn @click="router.push({ name: 'profile' })">
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </v-bottom-navigation>
    </v-layout>
  </slot>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useViewStore } from '@/stores/view'

const viewStore = useViewStore()
const router = useRouter()

// const now_value = viewStore.now_value
</script>

<style scoped></style>
