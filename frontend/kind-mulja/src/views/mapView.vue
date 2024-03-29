<template>
  <v-card>
    <v-layout style="position: relative; height: 100vh">
      <v-navigation-drawer floating permanent style="position: relative">
        <v-list density="compact" nav>
          <v-list-item
            @click="navigateTo('factory_map')"
            prepend-icon="mdi-factory"
            title="Factory Map"
            value="factory_map"
          ></v-list-item>
          <v-list-item
            @click="navigateTo('robots')"
            prepend-icon="mdi-robot"
            title="Robots"
            value="robots"
          ></v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-main style="padding-left: 0; flex-grow: 1">
        <!-- 패딩 제거 및 flex-grow 추가 -->
        <div v-if="selectedPage === 'factory_map'">
          <!-- Home 페이지에 대한 내용 -->
          <h2>Factory Map 페이지</h2>
          <p>이 곳은 Factory Map 페이지입니다.</p>
          <div ref="mapContainer" class="container">
            <img
              ref="image"
              src="/map/image.jpg"
              alt="Map Image"
              style="width: 100%; height: 100%; transform: scaleX(-1)"
            />
            <div ref="marker" class="marker"></div>
          </div>
        </div>
        <div v-else-if="selectedPage === 'robots'">
          <!-- About 페이지에 대한 내용 -->
          <h2>Robots 페이지</h2>
          <p>이 곳은 Robots 페이지입니다.</p>
        </div>
      </v-main>
    </v-layout>
  </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import io from 'socket.io-client'

const mapContainer = ref(null)
const image = ref(null)
const marker = ref(null)

const selectedPage = ref('factory_map') // 초기 선택 페이지 설정

const navigateTo = (page) => {
  selectedPage.value = page
}

// 이미지 좌표
const imageCoords = { x: 498, y: 498 }

onMounted(() => {
  const socket = io('http://localhost:12002/')
  
  socket.on('connect', () => {
    console.log('웹소켓 연결이 열렸습니다.')
  })

  socket.on('connect', () => {
    console.log('웹소켓 연결이 열렸습니다.')
    // 데이터를 수신 받았을 때의 처리
  })
  // 데이터를 수신하여 마커 위치를 조정
  socket.on('sendToFront', (data) => {
    const parsedData = JSON.parse(data) // 문자열을 JSON 객체로 변환
    // 시뮬레이터의 위치와 맵 상의 위치를 맞춰주기
    const adjustedX = Math.abs(-parsedData.x - 50) * 10
    const adjustedY = Math.abs(-parsedData.y - 50) * 10 - 2.5
    adjustMarkerPosition(adjustedX, adjustedY)
  })

  // 에러가 발생했을 때의 처리
  socket.on('error', (error) => {
    console.error('웹소켓 에러:', error)
  })
})

function adjustMarkerPosition(x, y) {
  // 이미지 컨테이너의 크기
  const containerWidth = mapContainer.value.clientWidth
  const containerHeight = mapContainer.value.clientHeight

  // 이미지 내에서의 마커 위치 계산
  const markerX = (x / imageCoords.x) * containerWidth
  const markerY = (y / imageCoords.y) * containerHeight

  // 마커 위치를 조정
  marker.value.style.left = `${markerX}px`
  marker.value.style.top = `${markerY}px`
}
</script>

<style>
/* 필요한 스타일 추가 */

.container {
  width: 500px;
  height: 500px;
  border: 1px solid black;
}

.marker {
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: red;
  border-radius: 50%;
}
</style>
