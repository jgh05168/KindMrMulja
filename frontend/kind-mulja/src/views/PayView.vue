<template>
  <AppHeader>
    <template #header-bar>결제</template>
  </AppHeader>
  <div class="cart-frame">
    <div class="set-address">
      <div style="display: flex; justify-content: space-between; align-items: center">
        <h3 v-if="orderStore.order_type == 0">배송지 설정</h3>
        <h3 v-else>픽업 장소</h3>
        <div v-if="orderStore.order_type == 0">
          <SelectDialog
            @click="getAddressMore()"
            @update:addressId="updateAddressId"
            @update:selectedAddress="updateSelectedAddress"
          />
        </div>
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
            <div>{{ selected_address?.address_name }}</div>

            <!-- 지금 배송지의 id 를 인자로 수정 페이지로 이동 -->
            <v-btn
              @click="slotProps.editAddress(selected_address?.address_id)"
              icon="mdi-home-edit-outline"
              variant="plain"
            ></v-btn>
          </div>
        </template>
        <template #address-detail>
          <p>{{ selected_address?.address_normal }}</p>
          <p>{{ selected_address?.address_detail }}</p>
          <p>받는사람 : {{ selected_address?.user_name }}</p>
        </template>
      </AddressItem>
    </div>

    <div class="set-pay">
      <div style="display: flex; justify-content: space-between; align-items: center">
        <h3>결제 수단</h3>
        <v-btn icon="mdi-swap-horizontal" variant="plain"></v-btn>
      </div>
      <CheckoutView :order-create="orderCreate" :total-price="total_price"/>
    </div>

    <div class="order-info">
      <CartRecipt>
        <template #items-price>{{ item_price }}</template>
        <template #delivery-price>{{ delivery_price }}</template>
        <template #total-price>{{ total_price }}</template>
      </CartRecipt>
    </div>
  </div>
</template>

<script setup>
import AppHeader from '@/layouts/AppHeader.vue'
import AddressItem from '@/components/AddressItem.vue'
import SelectDialog from '@/components/SelectDialog.vue'
import CartRecipt from '@/components/cart/CartRecipt.vue'

import { useOrderStore } from '@/stores/order'
import { useAuthStore } from '@/stores/auth'
import { ref, onMounted, computed } from 'vue'
import Service from '@/api/api'
import { useRouter } from 'vue-router'
import CheckoutView from './CheckoutView.vue'

const router = useRouter()
const orderStore = useOrderStore()
const authStore = useAuthStore()

const item_price = orderStore.item_price
const delivery_price = orderStore.delivery_price
const total_price = orderStore.total_price

const address_id = ref(null)
// 선택된 id 로 선택된 배송지 저장
const selected_address = ref(null)

const getAddressMore = () => {}

const updateAddressId = (id) => {
  address_id.value = id
}

const updateSelectedAddress = (address) => {
  selected_address.value = address
}

const selected_cart_id = computed(() => {
  if (orderStore.selected_item && orderStore.selected_item.length > 0) {
    let res = orderStore.selected_item.map((item) => item.cart_id)
    console.log(res)
    return res
  } else {
    return null
  }
})

const orderCreate = async () => {
  console.log(
    '보내는 주소지',
    JSON.stringify(selected_address.value.address_normal) +
      ',' +
      JSON.stringify(selected_address.value.address_detail)
  )
  const order_info = {
    user_id: authStore.user_id,
    address_content:
      JSON.stringify(selected_address.value.address_normal) +
      ',' +
      JSON.stringify(selected_address.value.address_detail),
    order_type: orderStore.order_type,
    selected_cart_id: selected_cart_id.value
  }
  console.log(order_info)
  await Service.createOrder(order_info)
}

onMounted(() => {
  if (orderStore.address_list && orderStore.address_list.length > 0) {
    let selected = orderStore.address_list.find((address) =>
      address.is_default === 1 ? address : null
    )
    selected_address.value = selected
    address_id.value = selected.address_id
  }
})
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
  bottom: 15%;
  margin: auto auto;
  width: 370px;
}

.pay-button {
  position: fixed;
  bottom: 8%;
  margin: auto auto;
}
</style>
