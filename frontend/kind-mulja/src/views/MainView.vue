<template>
  <!-- 앱을 키면 나오는 화면 -->
  <div class="main">
    <v-btn class="start-btn" elevation="16" size="x-large" color="#212121">start</v-btn>
  </div>
</template>

<script setup></script>

<style scoped>
.main {
  width: 100%;
  height: 100%;
  background-image: url('@/assets/main2.png');
  background-size: cover;
  position: relative;
}

.start-btn {
  position: absolute;
  left: 50%;
  top:70%;
  transform: translate(-50%,-50%);
}
</style>
