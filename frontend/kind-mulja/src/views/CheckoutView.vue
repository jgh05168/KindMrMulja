<template>
  <div class="wrapper">
    <div class="box_section">
      <!-- 결제 UI -->
      <div id="payment-method"></div>
      <!-- 이용약관 UI -->
      <div id="agreement"></div>
      <!-- 쿠폰 체크박스 -->
      <div style="padding-left: 25px"></div>
      <!-- 결제하기 버튼 -->
      <div class="result wrapper">
        <BlackButton class="pay-button" button-width="380px" @click="requestPayment">
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
    await props.orderCreate()
    if (paymentWidget) {
      await paymentWidget.requestPayment({
        orderId: nanoid(),
        orderName: '토스 티셔츠 외 2건',
        customerName: '김토스',
        customerEmail: 'customer123@gmail.com',
        customerMobilePhone: '01012341234',
        successUrl: `${window.location.origin}/paid`,
        failUrl: `${window.location.origin}/paid`
      })
    }
  } catch (error) {
    console.error(error)
  }
}

import { onMounted } from 'vue'
import { useOrderStore } from '@/stores/order'
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
</style>
