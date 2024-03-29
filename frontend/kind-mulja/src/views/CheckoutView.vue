<template>
  <div class="wrapper">
    <div class="box_section">
      <!-- 결제 UI -->
      <div id="payment-method"></div>
      <!-- 이용약관 UI -->
      <div id="agreement" class="agreement"></div>
      <!-- 결제하기 버튼 -->
      <div class="result wrapper">
        <BlackButton class="pay-button" button-width="90%" @click="requestPayment">
          <template #button-text>결제하기</template>
        </BlackButton>
      </div>
    </div>
  </div>
</template>

<script setup>
import { loadPaymentWidget, ANONYMOUS } from '@tosspayments/payment-widget-sdk'
import { nanoid } from 'nanoid'
import { defineProps } from 'vue'
import BlackButton from '@/components/BlackButton.vue'
import { onMounted } from 'vue'
import { useOrderStore } from '@/stores/order'

const orderStore = useOrderStore()

const props = defineProps({
  orderCreate: Function,
  totalPrice: Number
})

let paymentWidget = null
let paymentMethodWidget = null
const clientKey = 'test_ck_BX7zk2yd8y6qRb5GR54Y3x9POLqK'
const amount = props.totalPrice

const requestPayment = async () => {
  try {
    orderStore.orderInfo = await props.orderCreate() // 주문지 생성
    console.log(orderStore.orderInfo)
    if (paymentWidget) {
      await paymentWidget.requestPayment({
        orderId: nanoid(),
        orderName: '친절한 물자씨 상품 구매',
        customerName: '이싸피',
        customerEmail: 'ssafy@gmail.com',
        customerMobilePhone: '01012341234',
        successUrl: `${window.location.origin}/paid`,
        failUrl: `${window.location.origin}/pay`
      })
    }
  } catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  paymentWidget = await loadPaymentWidget(clientKey, ANONYMOUS)
  paymentMethodWidget = paymentWidget.renderPaymentMethods(
    '#payment-method',
    { value: amount },
    { variantKey: 'DEFAULT' }
  )
  paymentWidget.renderAgreement('#agreement', { variantKey: 'AGREEMENT' })
})
</script>
<style scoped>
.pay-button {
  position: fixed;
  bottom: 8%;
  margin: auto auto;
}

.agreement {
  margin-top: 0px;
  padding-bottom: 10px;
}
</style>
