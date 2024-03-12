<template>
  <v-btn
    class="black-button"
    elevation="3"
    rounded="lg"
    color="#212121"
    :style="{ width: props.buttonWidth }"
    height="55px"
  >
    <slot name="button-text">{{ buttonText }}</slot>
  </v-btn>
</template>

<script setup>
import { ref, defineProps } from 'vue'

const props = defineProps({
  buttonWidth: String
})

// 기본값 설정
const buttonText = ref('Click me')
</script>

<style scoped>
.black-button {
  font-size: 20px;
  font-weight: bold;
}
</style>
