<template>
  <!-- 앱을 키면 나오는 화면 -->
  <div class="main">
    <!-- 로그인 정보가 저장 되어 있으면 홈화면으로 -->
    <!-- 로그인 정보 없으면 로그인 창으로 -->
    <v-btn @click="GoToNext()" class="start-btn" elevation="16" size="x-large" color="#212121"
      >start</v-btn
    >
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const GoToNext = () => {
  router.push({ name: 'home' })
}
</script>

<style scoped>
.main {
  width: 100%;
  height: 100%;
  /* border-radius: solid black 2px; */
  background-image: url('@/assets/main2.png');
  background-size: cover;
  position: relative;
}

.start-btn {
  position: absolute;
  left: 50%;
  top: 70%;
  transform: translate(-50%, -50%);
}
</style>
