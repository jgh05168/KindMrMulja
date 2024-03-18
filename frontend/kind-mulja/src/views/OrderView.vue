<template>
  <AppHeader>
    <template #header-bar>주문 목록</template>
  </AppHeader>
  <div class="oreder-frame">
    <div class="state">
      <div>
        <v-tabs v-model="tab" align-tabs="center" color="#424242" >
          <v-tab :value="1">진행중</v-tab>
          <v-tab :value="2">배송완료</v-tab>
          <v-tab :value="3">취소</v-tab>
        </v-tabs>
        <v-window v-model="tab">
          <v-window-item v-for="n in 3" :key="n" :value="n"> </v-window-item>
        </v-window>
      </div>
    </div>
  </div>
</template>

<script setup>
import AppHeader from '@/layouts/AppHeader.vue'

import { ref } from 'vue'

const tab = ref('')
</script>

<style scoped></style>
