<template>
  <div class="detail-frame">
    <v-btn icon="mdi-chevron-left" style="position: absolute; left: -5%; top: 3%; z-index: 99">
    </v-btn>

    <ProductDetail :item="productStore.item" />
    <div>
      <v-btn :disabled="cnt <= 1" @click="cnt--">-</v-btn>
      <input style="width: 20px" type="number" :value="cnt" />
      <v-btn @click="cnt++">+</v-btn>
    </div>
    <div class="buy-button">
      <v-btn @click="zzim" width="55px" height="55px" rounded="lg" :icon="zzim_state"></v-btn>
      <BlackButton @click="addCart" :buttonWidth="width">
        <template v-slot:button-text> 장바구니 </template>
      </BlackButton>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductDetail from '@/components/ProductDetail.vue'
import BlackButton from '@/components/BlackButton.vue'
import { useProductStore } from '@/stores/product'
import Service from '@/api/api'
import { useAuthStore } from '@/stores/auth'

const productStore = useProductStore()
const authStore = useAuthStore()

const width = ref('280px')
const cnt = ref(1)

const is_zzim = ref(0)
const zzim_state = ref('mdi-bookmark-outline')

const zzim = () => {
  is_zzim.value = ~is_zzim.value
  // 사용자 찜 목록에 추가/삭제
  if (is_zzim.value == 0) {
    zzim_state.value = 'mdi-bookmark-outline'
  } else {
    zzim_state.value = 'mdi-bookmark'
  }
}

const addCart = async () => {
  // 사용자 장바구니에 추가 요청
  const addToCart_res = await Service.addToCart(
    authStore.user_id,
    productStore.now_product_id,
    cnt.value
  )
  // 장바구니에 추가되면 모달창 띄워야 함
  if (addToCart_res) {
    // 만약 로그인 안되어 있으면 로그인 창으로 이동
    // 로그인 후 현재 창으로 올 수 있도록 해야 됨
  }
}
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
</style>
