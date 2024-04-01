<template>
  <div class="modal-frame">
    <slot name="modal-button" :sheet="sheet" :modalOpen="modalOpen"> </slot>

    <v-bottom-sheet class="modal-sheet" v-model="sheet" inset :elevation="20" color="success">
      <div class="modal-card">
        <v-btn class="close-modal" size="xs" variant="plain" @click="modalClose"
          ><v-icon>mdi-close-circle-outline</v-icon></v-btn
        >
        <slot name="modal-choice" :modalClose="modalClose">
          <!-- 선택 버튼 두개 -->
          <v-btn>전체 상품 보러가기</v-btn>
          <v-btn>장바구니로 이동하기</v-btn>
        </slot>
      </div>
    </v-bottom-sheet>
  </div>
</template>
<script setup>
import { ref } from 'vue'

// const props = defineProps({
//   addCart: Function
// })

const sheet = ref(false)

const modalOpen = () => {
  // props.addCart()
  sheet.value = true
}
const modalClose = () => {
  sheet.value = false
}
</script>
<style scoped>
.modal-frame {
  width: 100%;
}

.modal-sheet {
}

.modal-card {
  width: 100%;
  height: 250px;
  border-top-left-radius: 10%;
  border-top-right-radius: 10%;
  background-color: aliceblue;
  border: 3px solid black;
  display: flex;
  flex-direction: column;
  position: relative;
}

.close-modal {
  position: absolute;
  top: 7%;
  right: 7%;
  scale: 2;
}
</style>
