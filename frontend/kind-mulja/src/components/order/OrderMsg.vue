<template>
  <!-- <div class="now-state"> -->
  <div class="now-state" :class="stateClass">
    <p>{{ stateText }}</p>
  </div>
  <!-- <p class="item-processing">{{ stateText }}</p>
    <p class="take-processing">{{ stateText }}</p>
    <p class="deliver-ready">{{ stateText }}</p>
    <p class="take-ready">{{ stateText }}</p>
    <p class="shipping">{{ stateText }}</p>
    <p class="delivered">{{ stateText }}</p>
    <p class="canceled">{{ stateText }}</p> -->
  <!-- </div> -->
</template>

<script setup>
import { onMounted } from 'vue'
import { defineProps } from 'vue'

const props = defineProps({
  orderState: Number,
  orderType: Number
})

const nowState = () => {
  let stateClass = ''
  let stateText = ''

  if (props.orderState == 0) {
    if (props.orderType == 0) {
      stateClass = 'item-processing'
      stateText = '상품 준비중'
    } else {
      stateClass = 'take-processing'
      stateText = '픽업 준비중'
    }
  } else if (props.orderState == 1) {
    if (props.orderType == 0) {
      stateClass = 'deliver-ready'
      stateText = '배송 준비 완료'
    } else {
      stateClass = 'take-ready'
      stateText = '픽업 준비 완료'
    }
  } else if (props.orderState == 2) {
    stateClass = 'shipping'
    stateText = '배송 중'
  } else if (props.orderState == 3) {
    stateClass = 'delivered'
    stateText = '배송 완료'
  } else if (props.orderState == 4) {
    stateClass = 'canceled'
    stateText = '취소'
  }

  return { stateClass, stateText }
}

const { stateClass, stateText } = nowState()

onMounted(() => {})
</script>

<style scoped>
.now-state {
  text-align: end;
  font-family: 'pretendard-extrabold';
  font-size: 22px;
}

.item-processing {
  color: #fb8c00;
}
.take-processing {
  color: #fb8c00;
}

.deliver-ready {
  color: #4caf50;
}

.take-ready {
  color: #4caf50;
}
.shipping {
  color: #757575;
}
.delivered {
  color: #212121;
}
.canceled {
  color: #f44336;
}
</style>
