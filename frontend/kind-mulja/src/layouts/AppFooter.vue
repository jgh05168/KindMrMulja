<template>
  <slot name="app-footer">
    <v-layout class="overflow-visible" style="height: 56px">
      <v-bottom-navigation v-model="value" color="teal" grow>
        <v-btn @click="router.push({ name: 'home' })">
          <v-icon>mdi-home</v-icon>
        </v-btn>

        <v-btn @click="router.push({ name: 'address' })">
          <v-icon>mdi-bookmark-outline</v-icon>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const value = ref(1)
</script>

<style scoped></style>
