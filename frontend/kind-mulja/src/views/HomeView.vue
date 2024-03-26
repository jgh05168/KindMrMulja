<template>
  <div>
    <AppHeader>
      <template #header-bar>친절한 물자씨</template>
    </AppHeader>

    <CategoryList></CategoryList>

    <ProductList :items="items"></ProductList>
  </div>
</template>

<script setup>
import { computed, onUpdated, onMounted } from 'vue'
import CategoryList from '@/components/home/CategoryList.vue'
import ProductList from '@/components/home/item/ProductList.vue'
import AppHeader from '@/layouts/AppHeader.vue'
import { useProductStore } from '@/stores/product'
import { useAuthStore } from '@/stores/auth'
import Service from '@/api/api'
import {} from 'vue'

const productStore = useProductStore()
const authStore = useAuthStore()

const items = computed(() => {
  // 전체 상품 리스트에서 현재 선택된 카테고리 기준으로 필터링 해주기
  if (productStore.now_category === 'popular') {
    // 인기순으로 정렬하여 반환
    return productStore.product_list
  } else {
    const category_product = []
    // product_list 배열을 순회하면서 조건을 만족하는 상품들을 찾음
    productStore.product_list.forEach((product) => {
      // 상품의 id 속성의 첫 번째 문자와 category_id가 일치하는지 확인
      if (product.product_category === productStore.now_category) {
        // 일치하는 경우에만 matchedProducts 배열에 상품 추가
        category_product.push(product)
      }
    })
    return category_product
  }
})

const zzim_check = () => {
  // 만약 로컬 환경에 로그인 되어 있으면
  productStore.product_list.forEach(async (product) => {
    // 찜 목록 체크하는 로직 추가
    const check_res = await Service.checkProductWish(authStore.user_id, product.product_id)
    console.log('home Mounted 상품 찜 여부 : ', check_res.result)
    product.is_zzim = check_res.result
  })
}

onUpdated(async () => {
  if (authStore.user_id) {
    await zzim_check()
  }
})

onMounted(async () => {
  if (authStore.user_id) {
    await zzim_check()
  }
})
</script>

<style scoped></style>
