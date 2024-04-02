<template>
  <!-- <h2>Factory Map 페이지</h2>
  <p>이 곳은 Factory Map 페이지입니다.</p> -->
  <div class="monitoring-layout">
    <div ref="mapContainer" class="container">
      <img
        ref="image"
        src="/map/map.png"
        alt="Map Image"
        style="width: 100%; height: 100%; transform: scaleY(-1) scaleX(-1)"
      />
      <div ref="marker_1" class="marker_1"></div>
      <div ref="marker_2" class="marker_2"></div>
      <div ref="marker_3" class="marker_3"></div>
    </div>
    <div class="live-board">
      <div class="live-order-list">
        <LiveOrder :robots="robots" />
      </div>
      <div class="robots-status">
        <RobotsStatus @robotSelected="handleRobotSelected" :robots="robots" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import io from 'socket.io-client'
import LiveOrder from '@/components/LiveOrder.vue'
import RobotsStatus from '@/components/RobotsStatus.vue'
import Service from '@/api/api'

const mapContainer = ref(null)
const image = ref(null)
const marker_1 = ref(null)
const marker_2 = ref(null)
const marker_3 = ref(null)

var socket = null
const socket_connection = ref(false)

const robots = ref([{}])

setInterval(async () => {
  robots.value = await Service.getOrderTutle()
}, 2000)

const handleRobotSelected = (robotId) => {
  // marker 에 달린 .selected-turtle-marker 제거
  const markers = [marker_1, marker_2, marker_3]
  markers.forEach((markerRef) => {
    const marker = markerRef.value
    if (marker) {
      marker.classList.remove('selected-turtle-marker')
    }
  })

  // 선택된 로봇 번호에 따라 해당하는 마커에 클래스 추가
  if (robotId !== null) {
    const selectedMarker = `marker_${robotId}`
    const selectedMarkerRef = eval(selectedMarker)
    if (selectedMarkerRef && selectedMarkerRef.value) {
      selectedMarkerRef.value.classList.add('selected-turtle-marker')
    }
  }
}

// 이미지 좌표 (수정 필요)
const imageCoords = { x: 600, y: 600 }

const connect_socket = (id, marker) => {
  // 데이터를 수신하여 마커 위치를 조정
  socket.on(`sendToFrontLoc${id}`, (data) => {
    const parsedData = JSON.parse(data) // 문자열을 JSON 객체로 변환
    // console.log(parsedData)
    // 서버에서 받은 데이터를 기반으로 마커 위치 조정
    // 전달받은 데이터가 null이 아닐 경우 실행
    if (parsedData !== null) {
      const adjustedX = Math.abs(-parsedData.x - 50) * 24 - 2.5
      const adjustedY = Math.abs(-parsedData.y - 50) * 24 - 2.5
      adjustMarkerPosition(marker, adjustedX, adjustedY)
    }
  })

  // 에러가 발생했을 때의 처리
  socket.on('error', (error) => {
    console.error('웹소켓 에러:', error)
  })
}

// 마커 위치 조정 함수

function adjustMarkerPosition(marker, x, y) {
  // mapContainer가 null이면 함수 종료
  if (!mapContainer.value) return

  // 이미지 컨테이너의 크기
  const containerWidth = mapContainer.value.clientWidth
  const containerHeight = mapContainer.value.clientHeight
  // 이미지 내에서의 마커 위치 계산
  const markerX = (x / imageCoords.x) * containerWidth
  const markerY = (y / imageCoords.y) * containerHeight

  // 마커 위치를 조정
  marker.style.left = `${markerX}px`
  marker.style.top = `${imageCoords.y - markerY - 10}px`
  // console.log(marker.style.left, marker.style.top)
}

onMounted(async () => {
  robots.value = await Service.getOrderTutle()
  // socket = io(socket_url, {
  //   // note changed URL here
  //   path: '/socket.io',
  //   transports: ['websocket'],
  //   namespace: `/camloc` // namespace를 수정해가며 설정하기
  // })

  socket = io('http://localhost:12002')
  // 연결이 수립되었을 때의 처리
  socket.on('connect', () => {
    console.log('웹소켓 연결이 열렸습니다.')
    console.log(socket_connection.value)
    socket_connection.value = true
    // 데이터를 수신 받았을 때의 처리
  })

  connect_socket(1, marker_1.value)
  connect_socket(2, marker_2.value)
  connect_socket(3, marker_3.value, 'https://j10c109.p.ssafy.io')
})
</script>

<style>
/* 필요한 스타일 추가 */
.monitoring-layout {
  display: flex;
}

.container {
  position: relative;
  width: 600px;
  height: 600px;
  border: 1px solid black;
  margin: 7% 3%;
}

.marker_1 {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  position: absolute;
  background-color: #ff1744;
}

.marker_2 {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  position: absolute;
  background-color: #ffff00;
}

.marker_3 {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  position: absolute;
  background-color: #1de9b6;
}

.live-order-list {
  margin-top: 5%;
}

.robots-status {
}

@keyframes blink-animation {
  0% {
    opacity: 1; /* 0% 지점에서는 표시 */
  }
  50% {
    opacity: 0.7; /* 100% 지점에서는 숨김 */
  }
  100% {
    opacity: 0.4; /* 100% 지점에서는 숨김 */
  }
}

.marker_1,
.marker_2,
.marker_3 {
  transition:
    left 0.5s ease,
    top 0.5s ease; /* left와 top 속성에 대해 0.5초간의 부드러운 변화를 적용 */
}

.selected-turtle-marker {
  scale: 2;
  transform: scale(2); /* 선택된 마커를 2배로 확대 */
  animation: blink-animation 1s infinite alternate;
}
</style>
