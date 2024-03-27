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
        <h2 v-else>이물자님, 안녕하세요!</h2>
      </div>
    </div>
    <div class="list-frame">
      <div>
        <h3 @click="router.push({ name: 'order' })">주문 목록</h3>
      </div>
      <div>
        <h3 @click="router.push({ name: 'address' })">배송지 관리</h3>
      </div>
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
</style>
