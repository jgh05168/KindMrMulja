<template>
  <div class="detail-frame">
    <div class="detail-frame-main">
      <v-btn
        @click="router.push({ name: 'home' })"
        icon="mdi-chevron-left"
        style="position: fixed; left: 5%; top: 3%; z-index: 99"
      >
      </v-btn>

      <ProductDetail :item="productStore.item" />
    </div>

    <div class="fixed-frame">
      <div class="buy-button">
        <v-btn
          class="me-5 zzim-btn"
          @click="zzim(productStore.now_product_id)"
          width="55px"
          height="55px"
          rounded="lg"
          color="#212121"
          :ripple="false"
          ><div class="zzim-icon">
            <v-icon v-if="is_zzim == true" size="30" color="red">mdi-heart</v-icon>
            <v-icon v-else size="30" color="white">mdi-heart-outline</v-icon>
          </div>
        </v-btn>

        <CartModal :add-cart="addCart">
          <template v-slot:modal-button="slotProps">
            <div class="pay-button">
              <BlackButton button-width="100%" @click="slotProps.modalOpen">
                <template #button-text>장바구니</template>
              </BlackButton>
            </div>
          </template>
          <template v-slot:modal-choice="slotProps">
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
                    <v-btn
                      size="xs"
                      variant="plain"
                      @click="cnt++"
                      :disabled="cnt + 1 > productStore.item.product_stock"
                      ><v-icon size="30">mdi-plus-box-outline</v-icon></v-btn
                    >
                  </div>
                </div>
              </div>
              <v-divider class="mt-3 mb-3" hickness="3" color="black"></v-divider>
              <div style="display: flex; justify-content: space-between; align-items: center">
                <h2>총 가격 :</h2>
                <h2 class="me-3" style="display: flex; align-items: center">
                  {{ Utils.numberWithCommas(productStore.item.product_price * cnt) }} 원
                </h2>
              </div>
              <v-card rounded="5" class="mt-2" style="width: 100%; border: 1px solid #212121">
                <v-btn
                  class=""
                  color="white"
                  height="55px"
                  width="30%"
                  style="font-size: 20px; font-weight: bold"
                  @click="addCart(slotProps.modalClose)"
                >
                  <v-icon color="">mdi-cart-arrow-down</v-icon>담기
                </v-btn>
                <v-btn
                  color="#212121"
                  height="55px"
                  width="70%"
                  style="font-size: 20px; font-weight: bold"
                  @click="addCartAndGo(slotProps.modalClose)"
                  >담고 구매하러 가기</v-btn
                >
              </v-card>
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
        <v-snackbar v-model="snackbar" :timeout="timeout" color="success">
          상품이 장바구니에 추가되었습니다.
        </v-snackbar>
        <v-snackbar v-model="checkbar" :timeout="timeout" color="#B71C1C">
          {{ check_message }}
        </v-snackbar>
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

const add_like = () => {
  const button = document.querySelector('.zzim-btn')
  const icon = document.querySelector('.zzim-icon')
  button.addEventListener('click', () => {
    icon.classList.add('like')

    // 1초 후에 like 클래스 제거
    setTimeout(() => {
      icon.classList.remove('like')
    }, 1000)
  })
}

const zzim = async (product_id) => {
  // 사용자 찜 목록에 추가/삭제
  const res = await Service.toggleWish(authStore.user_id, product_id)
  is_zzim.value = res.result
  await add_like()
}

const snackbar = ref(false) // Snackbar를 제어하기 위한 변수
const checkbar = ref(false)
const check_message = ref('')
const timeout = 3000 // Snackbar가 표시될 시간

const check_stock = () => {
  let res = false
  if (productStore.item.product_stock == 0) {
    check_message.value = '품절된 상품입니다.'
    res = true
  } else if (cnt.value > productStore.item.product_stock) {
    check_message.value = '재고 수량 보다 많이 선택하셨습니다.'
    res = true
  }
  if (res) {
    checkbar.value = true
  }
  return res
}
const addCart = async (modalClose) => {
  // 사용자 장바구니에 추가 요청
  // 만약 로그인 안되어 있으면 로그인 창으로 이동
  if (authStore.user_id == null) {
    alert('로그인이 필요한 서비스입니다.')
    router.push({ name: 'login' })
  } else {
    if (!check_stock()) {
      const addToCart_res = await Service.addToCart(
        authStore.user_id,
        productStore.now_product_id,
        cnt.value
      )
      if (addToCart_res) {
        // 장바구니에 추가되면 모달 창 닫기
        modalClose()
        snackbar.value = true
      }
    } else {
      modalClose()
    }
  }
}

const addCartAndGo = async (modalClose) => {
  // 사용자 장바구니에 추가 요청
  // 만약 로그인 안되어 있으면 로그인 창으로 이동
  if (authStore.user_id == null) {
    alert('로그인이 필요한 서비스입니다.')
    router.push({ name: 'login' })
  } else {
    if (!check_stock()) {
      const addToCart_res = await Service.addToCart(
        authStore.user_id,
        productStore.now_product_id,
        cnt.value
      )
      if (addToCart_res) {
        router.push({ name: 'cart' })
      }
    } else {
      modalClose()
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
  margin: 0 0%;
  height: 100%;
  padding-bottom: 100px;
}
.detail-frame-main {
  margin: 0 7%;
  height: 100%;
}

.fixed-frame {
  position: fixed;
  bottom: 0;
  width: 100%;
  margin: 0 auto;
  z-index: 99;
  background-color: white;
}

.first-modal {
  height: 120%;
  display: flex;
  flex-direction: column;
  background-color: white;
  border-top-left-radius: 10%;
  border-top-right-radius: 10%;
  padding: 5% 5%;
}

.buy-button {
  width: 90%;
  margin: 0 auto;
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

@keyframes like_effect {
  0% {
    transform: scale(0.5);
  }

  50% {
    transform: scale(1.3);
  }

  100% {
    transform: scale(1);
  }
}

@keyframes dislike_effect {
  0% {
    transform: scale(0.5);
  }

  50% {
    transform: scale(1.3);
  }

  100% {
    transform: scale(1);
  }
}

.like {
  animation: like_effect 1s ease-in-out;
}

.dislike {
  animation: dislike_effect 1s ease-in-out;
}
</style>
