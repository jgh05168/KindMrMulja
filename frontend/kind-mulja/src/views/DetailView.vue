<template>
  <div class="detail-frame">
    <v-btn
      @click="router.go(-1)"
      icon="mdi-chevron-left"
      style="position: fixed; left: 5%; top: 3%; z-index: 99"
    >
    </v-btn>

    <ProductDetail :item="productStore.item" />

    <div class="fixed-frame">
      <v-slide-y-transition>
        <div style="position: relative">
          <v-btn
            v-if="expand"
            style="position: absolute; top: 5%; right: 5%; z-index: 9999"
            variant="plain"
            size="xs"
            @click="change_expand()"
            ><v-icon size="30">mdi-close</v-icon></v-btn
          >

          <v-card v-show="expand" class="mx-auto first-modal">
            <h2>
              {{ productStore.item.product_name }}
            </h2>
            <h4>{{ productStore.item.product_price }}</h4>
            <div class="d-flex">
              <span>수량 선택 : </span>
              <div class="select-cnt">
                <v-btn :disabled="cnt <= 1" @click="cnt--">-</v-btn>
                <input style="width: 20px" type="number" :value="cnt" />
                <v-btn @click="cnt++">+</v-btn>
              </div>
            </div>
            <h3>총 가격 : {{ productStore.item.product_price * cnt }}</h3>
          </v-card>
        </div>
      </v-slide-y-transition>
      <div class="buy-button">
        <v-btn
          class="me-5 zzim-btn"
          @click="zzim(productStore.now_product_id)"
          width="55px"
          height="55px"
          rounded="lg"
        >
          <v-icon v-if="is_zzim == true" size="30" color="red-darken-1">mdi-heart</v-icon>
          <v-icon v-else size="30" color="red-darken-1">mdi-heart-outline</v-icon>
        </v-btn>

        <CartModal :add-cart="addCart">
          <template v-slot:modal-button="slotProps">
            <div class="pay-button">
              <BlackButton v-if="expand" button-width="100%" @click="slotProps.modalOpen">
                <template #button-text>장바구니</template>
              </BlackButton>
              <BlackButton v-else button-width="100%" @click="expand = !expand">
                <template #button-text>장바구니</template>
              </BlackButton>
            </div>
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
  </div>
</template>

<script setup>
import { ref } from 'vue'
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

const expand = ref(false)

const change_expand = () => {
  expand.value = !expand.value
}

const cnt = ref(1)

const is_zzim = ref(false)

const zzim = async (product_id) => {
  // 사용자 찜 목록에 추가/삭제
  const res = await Service.toggleWish(authStore.user_id, product_id)
  is_zzim.value = res.result
}

const addCart = async () => {
  // 사용자 장바구니에 추가 요청
  // 만약 로그인 안되어 있으면 로그인 창으로 이동
  if (authStore.user_id == null) {
    alert()
    router.push({ name: 'login' })
  } else {
    const addToCart_res = await Service.addToCart(
      authStore.user_id,
      productStore.now_product_id,
      cnt.value
    )
    if (addToCart_res) {
      // 장바구니에 추가되면 모달창 띄워야 함
    }
  }
}

onMounted(async () => {
  if (authStore.user_id) {
    const res = await Service.checkProductWish(authStore.user_id, productStore.now_product_id)
    console.log(res)
    is_zzim.value = res.result
  }
})
</script>

<style scoped>
.detail-frame {
  margin: 0 7%;
  height: 100%;
}

.fixed-frame {
  position: fixed;
  bottom: 8%;
  width: 85%;
  margin: 0 auto;
}

.first-modal {
  height: 150px;
  display: flex;
  flex-direction: column;
  background-color: white;
}

.buy-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.select-cnt {
  width: 50%;
}

.modal-choice-btn {
  width: 80%;
  height: 55px;
  margin: 15px auto;
  border: solid 2px black;
}
</style>
