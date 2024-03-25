<template>
  <div class="detail-frame">
    <v-btn
      @click="router.go(-1)"
      icon="mdi-chevron-left"
      style="position: absolute; left: -5%; top: 3%; z-index: 99"
    >
    </v-btn>

    <ProductDetail :item="productStore.item" />
    <div>
      <v-btn :disabled="cnt <= 1" @click="cnt--">-</v-btn>
      <input style="width: 20px" type="number" :value="cnt" />
      <v-btn @click="cnt++">+</v-btn>
    </div>
    <div class="buy-button">
      <v-btn
        class="me-5"
        @click="zzim(productStore.item.product_id)"
        width="55px"
        height="55px"
        rounded="lg"
        ><v-icon size="30" color="red-darken-1">{{ zzim_state }}</v-icon>
      </v-btn>

      <CartModal :add-cart="addCart">
        <template v-slot:modal-button="slotProps">
          <BlackButton :buttonWidth="width" @click="slotProps.modalOpen">
            <template #button-text>장바구니</template>
          </BlackButton>
        </template>
        <template #modal-choice>
          <v-btn
            class="modal-choice-btn"
            rounded="xl"
            size="x-large"
            @click="router.push({ name: 'home' })"
            >쇼핑 계속하기</v-btn
          >
          <v-btn
            class="modal-choice-btn"
            rounded="xl"
            size="x-large"
            @click="router.push({ name: 'cart' })"
            >장바구니로 이동하기</v-btn
          >
        </template>
      </CartModal>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import ProductDetail from '@/components/ProductDetail.vue'
import BlackButton from '@/components/BlackButton.vue'
import { useProductStore } from '@/stores/product'
import Service from '@/api/api'
import { useAuthStore } from '@/stores/auth'
import CartModal from '@/components/cart/CartModal.vue'
import { onMounted } from 'vue'

const productStore = useProductStore()
const authStore = useAuthStore()

const router = useRouter()

const width = ref('280px')
const cnt = ref(1)

const is_zzim = ref(false)
const zzim_state = computed(() => {
  if (is_zzim.value) {
    return 'mdi-heart'
  } else {
    return 'mdi-heart-outline'
  }
})

const zzim = async (product_id) => {
  // 사용자 찜 목록에 추가/삭제
  is_zzim.value = await Service.toggleWish(authStore.user_id, product_id)
}

const addCart = async () => {
  // 사용자 장바구니에 추가 요청
  // 만약 로그인 안되어 있으면 로그인 창으로 이동
  const addToCart_res = await Service.addToCart(
    authStore.user_id,
    productStore.now_product_id,
    cnt.value
  )
  if (addToCart_res) {
    // 장바구니에 추가되면 모달창 띄워야 함
    // 로그인 후 현재 창으로 올 수 있도록 해야 됨
  }
}

onMounted(async () => {
  if (authStore.user_id) {
    is_zzim.value = Service.checkProductWish(authStore.user_id, productStore.item.product_id)
  }
})
</script>

<style scoped>
.detail-frame {
  position: relative;
  margin: 0 7%;
  padding-bottom: 100px;
}

.buy-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  position: fixed;
  bottom: 8%;
  width: 356.91px;
}

.modal-choice-btn {
  width: 90%;
  height: 55px;
  margin: 15px auto;
  border: solid 2px black;
}
</style>
