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
  
  const mapContainer = ref(null);
  const image = ref(null);
  const marker = ref(null);
  
  // 이미지 좌표
  const imageCoords = { x: 250, y: 250 };
  
  onMounted(() => {
    adjustMarkerPosition(100, 100); // 예시: 원하는 x와 y 좌표 (100, 100)으로 설정
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
  