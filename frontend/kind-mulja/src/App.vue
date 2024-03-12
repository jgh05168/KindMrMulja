<template>
  <div>
    <RouterLink :to="{ name: 'main' }">main</RouterLink> /
    <RouterLink :to="{ name: 'login' }">login</RouterLink> /
    <RouterLink :to="{ name: 'home' }">home</RouterLink> /
    <RouterLink :to="{ name: 'address' }">address</RouterLink> /
    <RouterLink :to="{ name: 'create-address' }">create-address</RouterLink> /
  </div>
  <div class="galaxy_20_ultra">
    <RouterView />
    <AppFooter />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import AppHeader from '@/layouts/AppHeader.vue'
import AppFooter from '@/layouts/AppFooter.vue'
</script>

<style scoped>
.galaxy_20_ultra {
  width: 415px;
  height: 915px;
}
</style>
