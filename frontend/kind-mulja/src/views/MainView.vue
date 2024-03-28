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
import { io } from 'socket.io-client'

const router = useRouter()

const GoToNext = () => {
  router.push({ name: 'home' })
}

onMounted(() => {
  console.log('메인입니다.')
  // 서버 연결
  const socket = io('http://localhost:12002/')

  // 연결이 수립되었을 때의 처리
  socket.on('connect', () => {
    console.log('웹소켓 연결이 열렸습니다.')
    // 데이터를 수신 받았을 때의 처리
  })
  socket.on('sendToFront', (data) => {
    console.log(data)
  })

  // 에러가 발생했을 때의 처리
  socket.on('error', (error) => {
    console.error('웹소켓 에러:', error)
  })
})
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
