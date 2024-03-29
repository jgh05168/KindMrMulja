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
              <BlackButton button-width="100%" @click="slotProps.modalOpen">
                <template #button-text>장바구니</template>
              </BlackButton>
            </div>
          </template>
          <template #modal-choice>
            <!-- <div style="position: relative">
              <v-btn
                v-if="expand"
                style="position: absolute; top: 5%; right: 5%; z-index: 9999"
                variant="plain"
                size="xs"
                @click="change_expand()"
                ><v-icon size="30">mdi-close</v-icon></v-btn
              >
            </div> -->
            <v-card class="first-modal">
              <h2>
                {{ productStore.item.product_name }}
              </h2>
              <div class="d-flex modal-summary">
                <h2>
                  <v-icon size="20">mdi-currency-krw</v-icon
                  >{{ Utils.numberWithCommas(productStore.item.product_price) }}
                </h2>
                <div class="d-flex" style="width: fit-content">
                  <div class="select-cnt">
                    <v-btn size="xs" variant="plain" :disabled="cnt <= 1" @click="cnt--"
                      ><v-icon size="30">mdi-minus-box-outline</v-icon></v-btn
                    >
                    <input
                      style="width: 40px; font-size: 23px; text-align: end; padding-right: 5px"
                      type="number"
                      :value="cnt"
                    />
                    <v-btn size="xs" variant="plain" @click="cnt++"
                      ><v-icon size="30">mdi-plus-box-outline</v-icon></v-btn
                    >
                  </div>
                </div>
              </div>
              <v-divider class="mt-3 mb-3" hickness="3" color="black"></v-divider>
              <div style="display: flex; justify-content: space-between; align-items: center">
                <h2>총 가격 :</h2>
                <h2 class="me-3">
                  {{ Utils.numberWithCommas(productStore.item.product_price * cnt) }}
                  <v-icon size="25">mdi-currency-krw</v-icon>
                </h2>
              </div>
              <BlackButton button-width="100%" @click="addCart()">
                <template #button-text>장바구니</template>
              </BlackButton>
            </v-card>
            <!-- <v-btn
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
            > -->
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
import Utils from '@/utils/utils'

const productStore = useProductStore()
const authStore = useAuthStore()

const router = useRouter()

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
  padding-bottom: 200px;
}

.fixed-frame {
  position: fixed;
  bottom: 8%;
  width: 85%;
  margin: 0 auto;
}

.first-modal {
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: white;
  border-top-left-radius: 10%;
  border-top-right-radius: 10%;
  padding: 5% 5%;
}

.buy-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.modal-summary {
  justify-content: space-between;
  margin-top: 10px;
  margin-right: 10px;
  align-items: center;
}
.select-cnt {
  width: 50%;
  display: flex;
  font-weight: bold;
}

.modal-choice-btn {
  width: 80%;
  height: 55px;
  margin: 15px auto;
  border: solid 2px black;
}
</style>
