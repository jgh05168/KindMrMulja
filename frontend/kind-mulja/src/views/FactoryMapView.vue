<template>
  <!-- <h2>Factory Map 페이지</h2>
  <p>이 곳은 Factory Map 페이지입니다.</p> -->
  <div ref="mapContainer" class="container">
    <img
      ref="image"
      src="/map/image.jpg"
      alt="Map Image"
      style="width: 100%; height: 100%; transform: scaleX(-1)"
    />
    <div ref="marker" class="marker"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import io from 'socket.io-client'

const mapContainer = ref(null)
const marker = ref(null)

// 이미지 좌표 (수정 필요)
const imageCoords = { x: 600, y: 600 }

onMounted(() => {
  // 서버 주소 수정

  const socket = io('https://j10c109.p.ssafy.io:3000', {
    // note changed URL here
    path: '/socket'
  })

  // 연결이 수립되었을 때의 처리
  socket.on('connect', () => {
    console.log('웹소켓 연결이 열렸습니다.')
  })

  // 데이터를 수신하여 마커 위치를 조정
  socket.on('sendToFront', (data) => {
    const parsedData = JSON.parse(data) // 문자열을 JSON 객체로 변환
    console.log(parsedData)
    // 서버에서 받은 데이터를 기반으로 마커 위치 조정
    const adjustedX = Math.abs(-parsedData.x - 50) * 24 - 2.5
    const adjustedY = Math.abs(-parsedData.y - 50) * 24 - 2.5
    adjustMarkerPosition(adjustedX, adjustedY)
  })

  // 에러가 발생했을 때의 처리
  socket.on('error', (error) => {
    console.error('웹소켓 에러:', error)
  })
})

// 마커 위치 조정 함수

function adjustMarkerPosition(x, y) {
  // mapContainer가 null이면 함수 종료
  if (!mapContainer.value) return

  // 이미지 컨테이너의 크기
  const containerWidth = mapContainer.value.clientWidth
  const containerHeight = mapContainer.value.clientHeight
  // 이미지 내에서의 마커 위치 계산
  const markerX = (x / imageCoords.x) * containerWidth
  const markerY = (y / imageCoords.y) * containerHeight
  // console.log(markerX, markerY)

  // 마커 위치를 조정
  marker.value.style.left = `${markerX}px`
  marker.value.style.top = `${markerY}px`
}
</script>

<style>
/* 필요한 스타일 추가 */

.container {
  position: relative;
  width: 600px;
  height: 600px;
  border: 1px solid black;
  margin: 5%;
}

.marker {
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: red;
  border-radius: 50%;
}
</style>
