<template>
  <AppHeader>
    <template #header-bar>프로필</template>
  </AppHeader>
  <div class="profile-view-frame">
    <div class="profile-frame">
      <v-avatar size="80" style="border: 1px solid darkblue">
        <v-img src="/src/assets/paid.png"></v-img>
      </v-avatar>
      <div class="ms-3">
        <div v-if="authStore.user_id == null">
          <span>로그인하기</span> | <span>회원가입하기</span>
        </div>
        <h2 v-else>{{ authStore.user_name }} 님, 안녕하세요!</h2>
      </div>
    </div>
    <v-divider></v-divider>
    <div class="list-frame">
      <v-card class="profile-list">
        <h2 @click="router.push({ name: 'order' })">주문 목록</h2>
      </v-card>
      <v-card class="profile-list">
        <h2 @click="router.push({ name: 'address' })">배송지 관리</h2>
      </v-card>
      <!-- <v-card class="profile-list" style="align-items: center; justify-content: space-between">
        <h2>psuh 알림 설정</h2>
        <v-switch
          class="ms-15"
          hide-details
          :model-value="authStore.allow_alarm"
          color="success"
        ></v-switch>
      </v-card> -->
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import AppHeader from '@/layouts/AppHeader.vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const router = useRouter()
</script>

<style scoped>
.profile-view-frame {
  width: 90%;
  margin: 0 auto;
}

.profile-frame {
  width: 100%;
  margin: 5% auto;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.profile-list {
  width: 100%;
  height: 90px;
  margin-top: 2%;
  display: flex;
  align-items: center;
  padding-left: 5%;
}
</style>
