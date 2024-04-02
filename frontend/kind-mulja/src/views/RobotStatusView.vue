<template>
  <v-container>
    <h2>카메라 모니터링</h2>
    <v-row>
      <v-col v-for="n in 3" :key="n" :value="n" cols="4">
        <v-card>
          <div>
            <v-card-title>{{ n }} 번 로봇 카메라</v-card-title>
            <v-divider></v-divider>
            <!-- 이미지 요소의 참조를 업데이트하여 이미지가 표시되도록 함 -->
            <v-img
              width="200px"
              :src="imageSources[n - 1]"
              aspect-ratio="1"
              :ref="`image${n}`"
              style="scale: 2"
            ></v-img>
          </div>
        </v-card> </v-col
    ></v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import io from 'socket.io-client'

// 이미지 소스를 저장할 배열
const imageSources = ref(['', '', ''])

var socket = null

// 이미지 요소에 대한 참조를 저장할 배열
const imageRefs = [ref(null), ref(null), ref(null)]

onMounted(() => {
  socket = io('http://localhost:12002/')

  // const socket = io(socket_url, {
  //   // note changed URL here
  //   path: '/socket.io',
  //   transports: ['websocket'],
  //   namespace: `/camloc` // namespace를 수정해가며 설정하기
  // })

  switchSocket(1)
  switchSocket(2)
  switchSocket(3)
})

function switchSocket(id) {
  // 탭 값이 1인 경우에만 소켓 열기

  socket.on('error', (error) => {
    console.error('웹소켓 에러:', error)
  })
  // 데이터를 수신하여 이미지 표시
  socket.on(`sendToFrontImage${id}`, (data) => {
    // 이미지 데이터를 Base64로 인코딩
    const imageData = btoa(String.fromCharCode.apply(null, new Uint8Array(data)))

    // 이미지 소스를 업데이트
    imageSources.value[id - 1] = 'data:image/webp;base64,' + imageData

    // 이미지 요소의 참조를 업데이트
    const imgElement = imageRefs[id - 1].value

    // 이미지 데이터를 img 요소의 src 속성에 할당하여 표시
    if (imgElement) {
      imgElement.src = imageSources.value[id - 1]
    }
  })
}
</script>
<style scoped>
.tab-item {
  font-size: 15px;
  font-family: 'pretendard-extrabold';
}
</style>
