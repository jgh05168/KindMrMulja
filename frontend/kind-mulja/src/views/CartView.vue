<template>
  <AppHeader><template #header-bar>장바구니</template> </AppHeader>

  <div class="cart-frame">
    <div class="cart-main-frame">
      <DeliveryChoice>
        <template #delivery>
          <div
            class="delivery-choice"
            @click="select(0)"
            :class="{ 'selected-option': selectedOption == 0 }"
          >
            <v-icon size="40" icon="mdi-truck-fast-outline"></v-icon>
            <span class="mx-4">배송</span>
          </div>
        </template>
        <template #pick-up>
          <div
            class="delivery-choice"
            @click="select(1)"
            :class="{ 'selected-option': selectedOption == 1 }"
          >
            <v-icon size="40" icon="mdi-store-marker-outline"></v-icon>
            <span class="mx-4">픽업</span>
          </div>
        </template>
      </DeliveryChoice>

      <CartItem v-for="(item, idx) in cart_items" :value="item.id" :key="idx">
        <template #item-image>
          <v-img :src="item.img"></v-img>
        </template>
        <template #item-name>{{ item.name }}</template>
        <template #item-price>{{ item.price }}</template>
        <template #item-cnt>
          <!-- 상품 수량 변경 시 DB 에도 장바구니 수량 변경 요청 보내야 함 -->
          <v-btn
            size="xs"
            icon="mdi-minus"
            varient="tonal"
            :disabled="item.cnt <= 1"
            @click="item.cnt--"
          ></v-btn>
          <input style="width: 20px; text-align: center" type="number" :value="item.cnt" />
          <v-btn class="ps-0" size="xs" icon="mdi-plus" varient="tonal" @click="item.cnt++"></v-btn>
        </template>

        <template #cancel-btn>
          <v-btn
            @click="removeItem(item.id)"
            size="xs"
            icon="mdi-close-circle-outline"
            variant="plain"
          ></v-btn>
        </template>
      </CartItem>

      <CartRecipt>
        <template #items-price>{{ items_price }}</template>
        <template #delivery-price>{{ delivery_price }}</template>
        <template #total-price>{{ total_price }}</template>
      </CartRecipt>
    </div>

    <BlackButton class="pay-button" button-width="380px">결제하기</BlackButton>
  </div>
</template>

<script setup>
import AppHeader from '@/layouts/AppHeader.vue'
import DeliveryChoice from '@/components/cart/DeliveryChoice.vue'
import CartItem from '@/components/cart/CartItem.vue'
import CartRecipt from '@/components/cart/CartRecipt.vue'
import BlackButton from '@/components/BlackButton.vue'

import { ref, computed } from 'vue'

const selectedOption = ref(0) // 선택된 옵션을 저장할 변수

const select = (option) => {
  selectedOption.value = option
}

const cart_items = ref([
  {
    id: 0,
    name: '1번',
    price: 1000,
    cnt: 1,
    img: 'https://source.unsplash.com/random/150x150/?furniture'
  },
  {
    id: 1,
    name: '2번',
    price: 2000,
    cnt: 2,
    img: 'https://source.unsplash.com/random/150x150/?furniture'
  },
  {
    id: 2,
    name: '3번',
    price: 3000,
    cnt: 3,
    img: 'https://source.unsplash.com/random/150x150/?furniture'
  }
])

const items_price = ref(0)
const delivery_price = ref(0)
const total_price = computed(() => {
  return items_price.value + delivery_price.value
})

const removeItem = (id) => {
  // 장바구니에서 해당 상품 삭제하는 요청 보내야 함
  const idx = cart_items.value.findIndex((item) => item.id === id)
  if (idx !== -1) {
    cart_items.value.splice(idx, 1)
  }
}
</script>

<style scoped>
.cart-frame {
  width: 90%;
  margin: 0 auto;
  position: relative;
}

.cart-main-frame {
  width: 100%;
  margin: 0 auto;
}

.pay-button {
  position: fixed;
  bottom: 8%;
  margin: auto auto;
}

.delivery-choice {
  display: flex;
  width: 100%;
  height: 60px;
  margin: 10px auto;
  padding-left: 20px;
  border: 2px solid #bdbdbd;
  align-items: center;
}

.delivery-choice {
  font-size: 15px;
  font-weight: bold;
}

.selected-option {
  border-radius: 2px sloid #424242;
  background-color: antiquewhite;
  transition: ease-in-out 0.3s;
}
</style>
