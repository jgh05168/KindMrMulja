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
      <div v-if="cart_items.length > 0">
        <div style="height: 40px; display: flex; align-items: center">
          <v-btn variant="plain" @click="all_select" label="전체 상품 선택하기">
            <v-icon size="20" v-if="selected_items.length !== cart_items.length"
              >mdi-checkbox-blank-outline</v-icon
            >
            <v-icon size="20" v-else>mdi-checkbox-intermediate</v-icon>
            <p class="ms-3" style="font-size: 20px">전체 상품 선택하기</p>
          </v-btn>
        </div>
        <CartItem
          v-for="(item, idx) in cart_items"
          :value="item.product_id"
          :key="idx"
          :cart-id="item.cart_id"
          :item-quentity="item.product_quentity"
        >
          <template #item-check>
            <div>
              <v-badge
                v-if="item.product_stock == 0"
                style="position: absolute; top: 10%; left: 15%; z-index: 2"
                color="#E53935"
                content="품절"
              ></v-badge>
              <v-checkbox
                :disabled="item.product_stock == 0"
                hide-details
                v-model="selected_items"
                :value="item"
              >
              </v-checkbox>
            </div>
          </template>

          <template #item-image>
            <v-img :src="`/product/${item.product_id}.jpg`"></v-img>
          </template>
          <template #item-name>{{ item.product_name.slice(0, 10) }}</template>
          <template #item-price>{{ Utils.numberWithCommas(item.product_price) }}</template>
          <template #item-cnt>
            <!-- 상품 수량 변경 시 DB 에도 장바구니 수량 변경 요청 보내야 함 -->
            <v-btn
              size="xs"
              icon="mdi-minus"
              varient="tonal"
              :disabled="item.product_quentity <= 1"
              @click="item.product_quentity--"
            ></v-btn>
            <input
              style="width: 20px; text-align: center"
              type="number"
              :value="item.product_quentity"
            />
            <v-btn
              class="ps-0"
              size="xs"
              icon="mdi-plus"
              varient="tonal"
              :disabled="item.product_quentity + 1 > item.product_stock"
              @click="item.product_quentity++"
            ></v-btn>
          </template>

          <template #cancel-btn>
            <v-btn
              @click="removeItem(item.product_id, item.cart_id)"
              size="xs"
              icon="mdi-close-circle-outline"
              variant="plain"
            ></v-btn>
          </template>
        </CartItem>
      </div>
      <div style="width: 100%; height: 300px; text-align: center; margin-top: 30%" v-else>
        <v-icon @click="router.push({ name: 'home' })" color="grey" size="100"
          >mdi-cart-arrow-down</v-icon
        >
        <h2>담으러 가기</h2>
      </div>
    </div>

    <div class="pay-button">
      <div style="position: relative">
        <v-btn
          v-if="expand"
          style="position: absolute; top: 5%; right: 5%; z-index: 9999"
          variant="plain"
          size="xs"
          @click="change_expand()"
          ><v-icon size="30">mdi-close</v-icon></v-btn
        >
        <v-slide-y-transition>
          <v-card v-show="expand" class="mx-auto" style="width: 100%">
            <CartRecipt style="padding-top: 7%; margin-bottom: 5%">
              <template #items-price>{{ Utils.numberWithCommas(items_price) }}</template>
              <template #delivery-price>{{ Utils.numberWithCommas(delivery_price) }}</template>
              <template #total-price>{{ Utils.numberWithCommas(total_price) }}</template>
            </CartRecipt>
          </v-card>
        </v-slide-y-transition>
      </div>
      <BlackButton v-if="expand" button-width="100%" @click="goToOrder()">
        <template #button-text> 결제하기 </template>
      </BlackButton>
      <BlackButton v-else button-width="100%" @click="expand = !expand">
        <template #button-text>결제하기</template>
      </BlackButton>
    </div>
    <v-snackbar v-model="checkbar" :timeout="timeout" color="#B71C1C">
      {{ check_message }}
    </v-snackbar>
  </div>
</template>

<script setup>
import AppHeader from '@/layouts/AppHeader.vue'
import DeliveryChoice from '@/components/cart/DeliveryChoice.vue'
import CartItem from '@/components/cart/CartItem.vue'
import CartRecipt from '@/components/cart/CartRecipt.vue'
import BlackButton from '@/components/BlackButton.vue'
import Service from '@/api/api'
import { useAuthStore } from '@/stores/auth'
import { useOrderStore } from '@/stores/order'
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Utils from '@/utils/utils'
const router = useRouter()
const authStore = useAuthStore()
const orderStore = useOrderStore()

const selectedOption = ref(0) // 선택된 옵션을 저장할 변수

const select = (option) => {
  selectedOption.value = option
}

const expand = ref(false)

const change_expand = () => {
  expand.value = !expand.value
}

const checkbar = ref(false)
const check_message = ref('')
const timeout = 3000 // Snackbar가 표시될 시간

const check_stock = () => {
  let res = false
  selected_items.value.forEach(async (item) => {
    const detail = await Service.getProduct(item.product_id)
    if (item.product_quentity > detail.product_stock) {
      check_message.value = '품절 상품이거나 재고 수량보다 많이 주문하였습니다.'
      res = true
    }
  })
  return res
}

const cart_items = ref([])
const selected_items = ref([])

const all_select = () => {
  if (selected_items.value.length == 0 || selected_items.value.length < cart_items.value.length) {
    selected_items.value = cart_items.value.filter((item) => item.product_stock > 0)
  } else {
    selected_items.value = []
  }
}

const items_price = computed(() => {
  let item_total_price = 0
  selected_items.value.forEach((item) => {
    item_total_price += item.product_price * item.product_quentity
  })
  return item_total_price
})
const delivery_price = computed(() => {
  if (selectedOption.value == 1) {
    return 0
  } else {
    if (selected_items.value.length > 0) {
      return 5000
    } else {
      return 0
    }
  }
})
const total_price = computed(() => {
  return items_price.value + delivery_price.value
})

const removeItem = async (product_id, cart_id) => {
  // 장바구니에서 해당 상품 삭제하는 요청 보내야 함
  await Service.cartDelete(cart_id)
  // 선택된 상품에 있으면 선택된 상품에서 제외해줘야함
  selected_items.value = selected_items.value.filter((item) => item.cart_id !== cart_id)
  // 화면상에서도 삭제
  const idx = cart_items.value.findIndex((item) => item.product_id === product_id)
  if (idx !== -1) {
    cart_items.value.splice(idx, 1)
  }
}

const save_data = () => {
  orderStore.selected_item = selected_items.value
  // 선택된 배송 옵션 저장
  orderStore.order_type = selectedOption.value
  // 결제 금액 정보 저장
  orderStore.item_price = items_price.value
  orderStore.delivery_price = delivery_price.value
  orderStore.total_price = total_price.value
}

const goToOrder = async () => {
  if (!check_stock()) {
    // 결제하기 버튼 클릭 시 사전 정보 orderstore 에 저장
    await save_data()
    console.log(orderStore.selected_item)
    orderStore.address_list = await Service.getAddress(authStore.user_id)
    // 결제하기 버튼 클릭 시 결제 페이지로 이동
    await router.push({ name: 'pay' })
  } else {
    checkbar.value = true
  }
}

onMounted(async () => {
  const cart_list_res = await Service.cartList(authStore.user_id)
  cart_items.value = cart_list_res

  // 페이지 로드 시 화면 상단으로 스크롤
  window.scrollTo({ top: 0, behavior: 'smooth' })
})
</script>

<style scoped>
.cart-frame {
  width: 90%;
  height: 120%;
  margin: 0 auto;
  position: relative;
}

.cart-main-frame {
  width: 100%;
  height: fit-content;
  margin: 0 auto;
}

.pay-button {
  width: 90%;
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
  border: 3px solid black;
  transition: ease-in-out 0.1s;
}

.modal-choice-btn {
  width: 90%;
  height: 55px;
  margin: 15px auto;
  border: solid 2px black;
}
</style>
