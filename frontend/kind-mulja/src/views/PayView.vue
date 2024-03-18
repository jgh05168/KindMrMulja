<template>
  <AppHeader>
    <template #header-bar>결제</template>
  </AppHeader>
  <div class="cart-frame">
    <div class="set-address">
      <div style="display: flex; justify-content: space-between; align-items: center">
        <h3>배송지 설정</h3>
        <SelectDialog />
      </div>
      <AddressItem :width="'360px'">
        <template v-slot:address-title="slotProps">
          <div
            style="
              display: flex;
              flex-direction: row;
              justify-content: space-between;
              align-items: center;
            "
          >
            <div>{{ address.title }}</div>
            <!-- 지금 배송지의 id 를 인자로 수정 페이지로 이동 -->
            <v-btn
              @click="slotProps.editAddress(address.id)"
              icon="mdi-home-edit-outline"
              variant="plain"
            ></v-btn>
          </div>
        </template>
        <template #address-detail>
          <div>{{ address.detail }}</div>
        </template>
      </AddressItem>
    </div>

    <div class="set-pay">
      <div style="display: flex; justify-content: space-between; align-items: center">
        <h3>결제 수단</h3>
        <v-btn icon="mdi-swap-horizontal" variant="plain"></v-btn>
      </div>

      <div style="width: 360px; height: 70px; border: 1px solid red; margin: 2px auto"></div>
    </div>

    <div class="order-info">
      <CartRecipt>
        <template #items-price>{{ items_price }}</template>
        <template #delivery-price>{{ delivery_price }}</template>
        <template #total-price>{{ total_price }}</template>
      </CartRecipt>
    </div>

    <BlackButton class="pay-button" button-width="380px">
      <template #button-text>결제하기</template>
    </BlackButton>
  </div>
</template>

<script setup>
import AppHeader from '@/layouts/AppHeader.vue'
import AddressItem from '@/components/AddressItem.vue'
import SelectDialog from '@/components/SelectDialog.vue'
import CartRecipt from '@/components/cart/CartRecipt.vue'
import BlackButton from '@/components/BlackButton.vue'

import { ref } from 'vue'

const address = ref({
  id: 1,
  title: '삼성전자 광주사업장 1',
  detail: '광주 관산구 하남산단 6번로 107, SSAFY 멀티캠퍼스'
})

const items_price = ref(0)
const delivery_price = ref(0)
const total_price = ref(0)
</script>

<style scoped>
.cart-frame {
  width: 90%;
  margin: 0 auto;
  position: relative;
}

.set-address {
}

.set-pay {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.order-info {
  position: fixed;
  bottom: 20%;
  margin: auto auto;
  width: 370px;
}

.pay-button {
  position: fixed;
  bottom: 8%;
  margin: auto auto;
}
</style>
