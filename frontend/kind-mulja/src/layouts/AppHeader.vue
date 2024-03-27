<template>
  <div
    style="
      width: 415px;
      height: 50px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 99;
      background-color: white;
      padding-top: 3%;
      padding-bottom: 5%;
    "
  >
    <v-btn size="50" @click="router.go(-1)" variant="plain"
      ><v-icon size="40">mdi-chevron-left</v-icon></v-btn
    >
    <span style="font-weight: bold; font-size: 25px">
      <slot name="header-bar"> </slot>
    </span>
    <v-btn size="50" variant="plain">
      <v-icon size="30">mdi-view-headline</v-icon>
      <v-menu activator="parent">
        <v-list>
          <v-list-item v-if="authStore.user_id == null" @click="router.push({ name: 'login' })">
            <v-list-item-title>로그인</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="authStore.user_id == null" @click="router.push({ name: 'signup' })">
            <v-list-item-title>회원가입</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="authStore.user_id !== null" @click="authStore.logout()">
            <v-list-item-title>로그아웃</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-btn>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const router = useRouter()
</script>

<style scoped></style>
