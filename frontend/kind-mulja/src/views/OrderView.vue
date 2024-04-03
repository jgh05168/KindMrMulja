<template>
  <AppHeader>
    <template #header-bar>주문 목록</template>
  </AppHeader>
  <div class="oreder-frame">
    <div class="state">
      <v-tabs v-model="tab" align-tabs="center" density="comfortable" color="#424242">
        <v-tab class="state-tab" :value="0">상품 준비</v-tab>
        <v-tab class="state-tab" :value="1">배송 상태</v-tab>
        <v-tab class="state-tab" :value="2">취소된 상품</v-tab>
      </v-tabs>
      <v-window style="padding-bottom: 8%" v-model="tab">
        <v-window-item v-for="(state, idx) in states" :key="idx" :value="idx">
          <OrderState :state="state" :order-list="state_list[state]" />
        </v-window-item>
      </v-window>
    </div>
  </div>
</template>

<script setup>
import AppHeader from '@/layouts/AppHeader.vue'
import { ref, onMounted } from 'vue'
import Service from '@/api/api'
import { useAuthStore } from '@/stores/auth'
import OrderState from '@/components/order/OrderState.vue'

const states = ref(['processing', 'delivered', 'canceled'])
const state_list = ref({
  processing: [],
  delivered: [],
  canceled: []
})
const authStore = useAuthStore()
const orderList = ref([])

// 일단 주문 목록 데이터를 모두 받아와야 해
// "order_state" 값에 따라 tab 에 나눠서 보여줘야 해
// 0 상품준비중, 픽업준비중
// 1 배송준비완료, 픽업준비완료
// 2 배송중
// 3 배송완료
// 4 취소
// 그러면 tab 값으로 상품을 필터링해서 보여주고
// 날짜값인 order_date 을 기준으로 내림차순 해서 보여줘
// 목록 안의 값은 하위 컴포넌트로 order_id 를 보내줘서
// 상세 목록을 받아와서 보여줘

onMounted(async () => {
  const res = await Service.getOrderList(authStore.user_id)
  orderList.value = res
  await orderList.value.forEach((order) => {
    // state 값이 1 이하일떄 processing
    if (order.order_state <= 1) {
      state_list.value['processing'].push(order)
    } // 값이 3 이면 배송완료
    else if (order.order_state >= 2 && order.order_state <= 3) {
      state_list.value['delivered'].push(order)
    } // 값이 4 이면 취소된 상품
    else if (order.order_state == 4) {
      state_list.value['canceled'].push(order)
    }
  })

  // 각각의 상태별 목록 리스트를 날짜순으로 필터링
  for (let state_key in state_list.value) {
    // console.log(state_list.value[state_key])
    state_list.value[state_key].sort((a, b) => new Date(b.order_date) - new Date(a.order_date))
  }
})

const tab = ref('')
</script>

<style scoped>
.state-tab {
  font-size: 18px;
  font-weight: bold;
}

.order-frame {
}
</style>
