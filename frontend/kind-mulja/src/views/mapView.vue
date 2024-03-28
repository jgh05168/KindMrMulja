<template>
  <div>
    <div ref="mapContainer" style="position: relative; width: 250px; height: 250px; border: 1px solid black;">
      <img ref="image" src="/map/image.jpg" alt="Map Image" style="width: 100%; height: auto;">
      <div ref="marker" class="marker"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import io from 'socket.io-client';

const mapContainer = ref(null);
const image = ref(null);
const marker = ref(null);

// 이미지 좌표
const imageCoords = { x: 250, y: 250 };

onMounted(() => {
  const socket = io('http://localhost:12002/')

  // 연결이 수립되었을 때의 처리
  socket.on('connect', () => {
    console.log('웹소켓 연결이 열렸습니다.')
    // 데이터를 수신 받았을 때의 처리
  })

  // 데이터를 수신하여 마커 위치를 조정
  socket.on("sendToFront", (data) => {
    console.log(data);
    const adjustedX = Math.abs(data.x) * 5;
    const adjustedY = Math.abs(data.y) * 5;
    adjustMarkerPosition(adjustedX, adjustedY);
  })

  // 에러가 발생했을 때의 처리
  socket.on('error', (error) => {
    console.error('웹소켓 에러:', error)
  })
});

function adjustMarkerPosition(x, y) {
  // 이미지 컨테이너의 크기
  const containerWidth = mapContainer.value.clientWidth;
  const containerHeight = mapContainer.value.clientHeight;

  // 이미지 내에서의 마커 위치 계산
  const markerX = (x / imageCoords.x) * containerWidth;
  const markerY = (y / imageCoords.y) * containerHeight;

  // 마커 위치를 조정
  marker.value.style.left = `${markerX}px`;
  marker.value.style.top = `${markerY}px`;
  console.log(marker.value.style.left, marker.value.style.top)
}
</script>

<style>
/* 필요한 스타일 추가 */
.marker {
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: red;
  border-radius: 50%;
}
</style>
