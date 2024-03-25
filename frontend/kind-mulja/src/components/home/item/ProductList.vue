<template>
  <v-container>
    <v-infinite-scroll height="900" side="end" @load="load">
      <v-row style="margin: 0 0">
        <v-col v-for="(item, idx) in props.items" :key="idx" cols="6">
          {{ item.is_zzim }}
          <ProductItem>
            <template #item-img>
              <div @click="GoDetail(item.product_id)">
                <v-img
                  :aspect-ratio="1 / 1"
                  width="cover"
                  style="border-radius: 3%"
                  :src="`/product/${item.product_id}.jpg`"
                >
                </v-img>
              </div>
            </template>

            <template #item-title>
              <v-card-subtitle>
                {{ item.product_name }}
              </v-card-subtitle>
            </template>

            <template #item-price>
              <v-card-title>
                <v-icon size="xs">mdi-currency-krw</v-icon>
                {{ item.product_price }}
                <v-btn size="xs" variant="plain" @click="zzim(item, item.product_id)">
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

const props = defineProps({
  items: Array
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
const GoDetail = (id) => {
  // 디테일 페이지로 이동
  // 1. api 함수 모음집에서 함수 가져와서 상품 상세정보 요청
  getItemDetail(id)
  // 2. 응답 데이터가 온 다음에 데이터를 저장하거나 가지고 이동
  router.push({ name: 'detail', params: { id: id } })
}

const zzim = async (item, product_id) => {
  if (authStore.user_id) {
  // 내 찜 목록에 추가거나 삭제
  // 추가하면 true, 삭제하면 false
  await Service.toggleWish(authStore.user_id, product_id)
  item.is_zzim = !item.is_zzim
}
  
}

const load = ({ side, done }) => {
  setTimeout(() => {
    if (side === 'start') {
      const arr = Array.from({ length: 10 }, (k, v) => props.items[0] - (10 - v))
      this.items = [...arr, ...this.items]
    } else if (side === 'end') {
      const arr = Array.from({ length: 10 }, (k, v) => this.items.at(-1) + 1 + v)
      this.items = [...this.items, ...arr]
    }

    done('ok')
  }, 1000)
}
</script>

<style scoped></style>
