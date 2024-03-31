<template>
  <div
    style="
      width: 100%;
      height: 90px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 99;
      background-color: white;
    "
  >
    <v-btn size="50" @click="router.go(-1)" variant="plain"
      ><v-icon size="40">mdi-chevron-left</v-icon></v-btn
    >
    <span style="font-weight: bold; font-size: 25px">
      <slot name="header-bar"> </slot>
    </span>
    <v-btn size="50" variant="plain">
      <v-icon v-if="authStore.user_id == null" size="30">mdi-login</v-icon>
      <v-icon v-else size="30">mdi-logout</v-icon>
      <v-menu activator="parent">
        <v-list>
          <v-list-item @click="changeApp()">
            <v-list-item-title v-if="authStore.is_admin == false">admin전환</v-list-item-title>
            <v-list-item-title v-else>user전환</v-list-item-title>
          </v-list-item>
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

const changeApp = () => {
  authStore.is_admin = !authStore.is_admin
  if (authStore.is_admin == true) {
    router.push({ name: 'factory_map' })
  } else {
    router.push({ name: 'home' })
  }
}
</script>

<style scoped></style>
