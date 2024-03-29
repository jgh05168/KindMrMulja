<template>
    <div class="total-order-frame">
        <OrderList v-for="order_bundle in props.orderList" :key="order_bundle.order_id" 
        :order-bundle = order_bundle
        />
    </div>
 
</template>

<script setup>
import { defineProps } from 'vue'
import OrderList from './OrderList.vue'

// 전체 주문 목록에서 state 에 맞는 주문들을 필터링 해서 보여주기
// 여러개의 주문 목록이 있음
// 각각의 주문 목록이 보이도록 하위 컴포넌트로 전달

const props = defineProps({
  state: String,
  orderList: Array
})

console.log(props.orderList)
// props.orderList.order_type == 1 이면 픽업
// 이때 props.orderList.order_state 에 따라 푸쉬 알림?



</script>

<style scoped>
.total-order-frame {

}

</style>
