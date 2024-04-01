<template>
  <v-card>
    <v-layout style="position: relative; height: 100vh">
      <v-navigation-drawer floating permanent color="#212121" style="position: relative">
        <div style="height: 100%">
          <div class="nav-item" style="padding-left: 20px; display: flex; align-items: center">
            <v-avatar size="50"
              ><v-img style="width: 80px; height: 80px" src="/paid.png"></v-img
            ></v-avatar>
            <h2 class="ms-4">친절한 물자씨</h2>
          </div>
          <v-divider class="nav-divider"></v-divider>
          <div class="nav-item-link" @click="router.push({ name: 'factory_map' })">
            <v-icon size="40">mdi-factory</v-icon>
            <p>Factory Map</p>
          </div>
          <div class="nav-item-link" @click="router.push({ name: 'robots_status' })">
            <v-icon size="40">mdi-robot</v-icon>
            <p>Robots</p>
          </div>
        </div>
      </v-navigation-drawer>
      <v-app-bar title="실시간 모니터링 시스템"></v-app-bar>
      <v-main style="padding-left: 0">
        <RouterView />
      </v-main>
    </v-layout>
  </v-card>
</template>

<script setup>
import { RouterView, useRouter } from 'vue-router'

const router = useRouter()
</script>

<style scoped>
.nav-item {
  height: 7%;
}

.nav-divider {
  margin-bottom: 10px;
}
.nav-item-link {
  height: 80px;
  padding-left: 40px;
  display: flex;
  align-items: center;
}

.nav-item-link > p {
  width: 100%;
  text-align: center;
}
</style>
