<template>
  <v-card>
    <v-tabs v-model="tab" align-tabs="start" color="deep-purple-accent-4">
      <v-tab class="tab-item" :value="1">1번 로봇</v-tab>
      <v-tab class="tab-item" :value="2">2번 로봇</v-tab>
      <v-tab class="tab-item" :value="3">3번 로봇</v-tab>
    </v-tabs>
    <v-window v-model="tab">
      <v-window-item v-for="n in 3" :key="n" :value="n">
        <!-- 이미지 요소의 참조를 업데이트하여 이미지가 표시되도록 함 -->
        <v-img
          v-if="tab === n"
          :src="imageSources[n - 1]"
          aspect-ratio="1"
          :ref="`image${n}`"
        ></v-img>
      </v-window-item>
    </v-window>
  </v-card>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import io from 'socket.io-client'

const tab = ref(1) // 초기 탭 값 설정

// 이미지 소스를 저장할 배열
const imageSources = ref(['', '', ''])

// 이미지 요소에 대한 참조를 저장할 배열
const imageRefs = [ref(null), ref(null), ref(null)]

let socket = null

onMounted(() => {
  switchSocket() // 초기 소켓 상태 설정
})

watch(tab, (newValue) => {
  console.log('Tab value changed to:', newValue)
  if (newValue !== 1) {
    socket.close() // 탭 값이 1이 아닌 경우 소켓 닫기
  } else if (newValue === 1) {
    switchSocket() // 탭 값이 1인 경우 소켓 열기
  }
})

function switchSocket() {
  // 탭 값이 1인 경우에만 소켓 열기
  if (tab.value === 1) {
    socket = io('http://localhost:12002/')
    // socket = io('https://j10c109.p.ssafy.io:12003/')
    socket.on('connect', () => {
      console.log('웹소켓 연결이 열렸습니다.')
    })
    socket.on('error', (error) => {
      console.error('웹소켓 에러:', error)
    })
    // 데이터를 수신하여 이미지 표시
    socket.on('sendToFrontImage', (data) => {
      // 이미지 데이터를 Base64로 인코딩
      const imageData = btoa(String.fromCharCode.apply(null, new Uint8Array(data)))

      // 이미지 소스를 업데이트
      imageSources.value[tab.value - 1] = 'data:image/jpeg;base64,' + imageData

      // 이미지 요소의 참조를 업데이트
      const imgElement = imageRefs[tab.value - 1].value

      // 이미지 데이터를 img 요소의 src 속성에 할당하여 표시
      if (imgElement) {
        imgElement.src = imageSources.value[tab.value - 1]
      }
    })
  }
}
</script>
<style scoped>
.tab-item {
  font-size: 15px;
  font-family: 'pretendard-extrabold';
}
</style>
