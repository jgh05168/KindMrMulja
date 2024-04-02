<template>
  <v-container>
    <v-infinite-scroll height="900" side="end">
      <v-row style="margin: 0 0">
        <v-col
          v-for="(item, idx) in productStore.category_items[props.categoryId]"
          :key="idx"
          cols="6"
        >
          <ProductItem>
            <template #item-img>
              <div @click="GoDetail(item?.product_id)">
                <v-img
                  :aspect-ratio="1 / 1"
                  width="cover"
                  style="border-radius: 3%; position: relative"
                  :src="`/product/${item?.product_id}.jpg`"
                >
                  <v-badge
                    v-if="item.product_stock == 0"
                    style="position: absolute; bottom: 10%; left: 15%; z-index: 2"
                    color="red-accent-4"
                    content="품절"
                  ></v-badge>
                </v-img>
              </div>
            </template>

            <template #item-title>
              <v-card-subtitle
                @click="GoDetail(item?.product_id)"
                style="font-size: 16px; font-weight: bold; position: relative"
              >
                {{ item.product_name }}
              </v-card-subtitle>
            </template>

            <template #item-price>
              <v-card-title style="display: flex; justify-content: space-between">
                <p style="font-size: 20px">
                  <v-icon class="me-1" size="15">mdi-currency-krw</v-icon
                  >{{ Utils.numberWithCommas(item?.product_price) }}
                </p>
                <v-btn
                  class="zzim-btn"
                  size="xs"
                  variant="plain"
                  @click="zzim(item, item.product_id)"
                >
                  <v-icon v-if="item.is_zzim == true" size="30" color="red-darken-1"
                    >mdi-heart</v-icon
                  >
                  <v-icon v-else size="30" color="red-darken-1">mdi-heart-outline</v-icon>
                </v-btn>
              </v-card-title>
            </template>
          </ProductItem>
        </v-col>
      </v-row>
    </v-infinite-scroll>
  </v-container>
</template>

<script setup>
import { defineProps } from 'vue'
import { useRouter } from 'vue-router'
import ProductItem from './ProductItem.vue'
import Service from '@/api/api'
import { useProductStore } from '@/stores/product'
import { useAuthStore } from '@/stores/auth'
import Utils from '@/utils/utils'

const props = defineProps({
  categoryId: String
})

const authStore = useAuthStore()
const productStore = useProductStore()

const router = useRouter()

// 일반적으로 상품의 상세 정보를 표시하는 페이지로 이동하기 전에 데이터를 먼저 요청하고 받는 것이 좋습니다. 이 방법은 사용자 경험을 향상시킬 수 있습니다.

// 사용자가 상세 정보 페이지로 이동하려고 클릭하면, 상세 정보를 요청하는 API 호출을 먼저 하고, 그 응답을 받은 후에 페이지를 이동하는 것이 좋습니다. 이 방법은 사용자가 페이지를 빠르게 로드하고 즉시 상세 정보를 볼 수 있게 해줍니다.
const getItemDetail = async (id) => {
  const detail = await Service.getProduct(id)
  console.log('상품 상세 정보,', detail)
  productStore.now_product_id = id
  productStore.item = detail
}
// 따라서 일반적으로는 다음과 같은 순서로 작업을 진행합니다:

// 사용자가 상품을 클릭하여 상세 정보 페이지로 이동하려고 시도합니다.
// 클릭 이벤트를 처리하여 상세 정보를 요청하는 API 호출을 실행합니다.
// API 응답을 기다립니다. 이때 로딩 인디케이터를 표시하여 사용자에게 진행 중임을 알립니다.
// API 응답이 도착하면 응답 데이터를 사용하여 상세 정보 페이지를 렌더링합니다.
// 페이지를 표시하고 사용자에게 상세 정보를 제공합니다.
const GoDetail = async (id) => {
  // 디테일 페이지로 이동
  // 1. api 함수 모음집에서 함수 가져와서 상품 상세정보 요청
  await getItemDetail(id)
  // 2. 응답 데이터가 온 다음에 데이터를 저장하거나 가지고 이동
  router.push({ name: 'detail', params: { id: id } })
}

const zzim = async (item, product_id) => {
  const buttons = document.querySelectorAll('.zzim-btn')

  buttons.forEach((button) => {
    button.addEventListener('click', function () {
      // 다른 버튼의 bounce 클래스 제거
      buttons.forEach((otherButton) => {
        if (otherButton !== button) {
          otherButton.classList.remove('like')
        }
      })

      // 현재 클릭한 버튼에 bounce 클래스 추가
      button.classList.add('like')

      // 1초 후에 bounce 클래스 제거
      setTimeout(() => {
        button.classList.remove('like')
      }, 1000)
    })
  })
  if (authStore.user_id) {
    // 내 찜 목록에 추가거나 삭제
    // 추가하면 true, 삭제하면 false
    const res = await Service.toggleWish(authStore.user_id, product_id)
    item.is_zzim = res.result
  }
}
</script>

<style scoped>
.zzim-btn {
}

@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

@keyframes shake {
  0% {
    transform: translateX(0);
  }
  20% {
    transform: translateX(-5%);
  }
  40% {
    transform: translateX(5%);
  }
  60% {
    transform: translateX(-5%);
  }
  80% {
    transform: translateX(5%);
  }
  100% {
    transform: translateX(0);
  }
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
  animation: like_effect 0.6s ease-in-out;
}

.dislike {
  animation: dislike_effect 1s ease-in-out;
}

.shake {
  animation: shake 0.2s ease-in-out infinite;
}

.bounce {
  animation-duration: 1s;
  animation-name: bounce;
}
</style>
