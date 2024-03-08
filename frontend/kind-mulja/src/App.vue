<template>
  <div>
    <RouterLink :to="{ name: 'main' }">main</RouterLink> /
    <RouterLink :to="{ name: 'login' }">login</RouterLink> /
    
  </div>
  <div class="galaxy_20_ultra">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.galaxy_20_ultra {
  width: 415px;
  height: 915px;
}
</style>
