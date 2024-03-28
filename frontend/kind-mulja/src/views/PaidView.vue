<template>
  <div class="paid-frame">
    <h1>결제 완료</h1>
    <v-img width="300" src="/src/assets/paid.png"></v-img>
    <div>
      <p>주문이 완료되었습니다.</p>
      <p>곧 친절한 문자씨가 상품을 준비해줄 거에요!</p>
    </div>

    <BlackButton @click="router.push({ name: 'order' })" class="go-order-list" button-width="360px">
      <template #button-text>주문정보 확인하기</template>
    </BlackButton>
    <BlackButton
      @click="router.push({ name: 'home' })"
      class="go-order-list"
      button-width="360px"
      color="#fafafa"
    >
      <template #button-text>BACK TO HOME</template>
    </BlackButton>
  </div>
</template>

<script setup>
import BlackButton from '@/components/BlackButton.vue'
import { useRoute, useRouter } from 'vue-router'
import { confirmPayment } from '@/confirmPayments'
import { ref, onMounted } from 'vue'
import Service from '@/api/api'
import { useOrderStore } from '@/stores/order'

const router = useRouter()
const route = useRoute()
const orderStore = useOrderStore()

const confirmed = ref(false)

onMounted(async () => {
  const requestData = {
    orderId: route.query.orderId,
    amount: route.query.amount,
    paymentKey: route.query.paymentKey
  }

  const confirm = async () => {
    try {
      const { response, json } = await confirmPayment(requestData)
      console.log(json)
      if (!response.ok) {
        router.push(`/fail?message=${json.message}&code=${json.code}`)
      } else {
        confirmed.value = true
      }
    } catch (error) {
      console.log(error)
    }
  }

  await confirm()
  await Service.createOrder(orderStore.orderInfo)
  orderStore.orderInfo = null
})
</script>

<style scoped>
.paid-frame {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  align-items: center;
  margin-top: 100px;
}

.paid-frame * {
  margin: 10px auto;
}

.go-order-list {
  border: 1px solid #212121;
}
</style>
