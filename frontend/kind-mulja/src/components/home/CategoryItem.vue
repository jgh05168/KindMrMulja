<template>
  <div class="category-item">
    <div class="category-image">
      <slot name="category-img">
        <!-- 부모에서 정의한 버튼이 위치하는 곳  -->
      </slot>
    </div>
    <slot name="category-title">
      <!-- 부모에서 정의한 버튼 title 이 위치하는 곳 -->
    </slot>
  </div>
</template>

<script setup></script>

<style scoped>
.category-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.category-image {
  width: 50px;
  margin: 0 10px;
}
</style>
