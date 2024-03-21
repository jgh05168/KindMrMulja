<template>
  <div>
    <CategoryList></CategoryList>

    <ProductList :items="items"></ProductList>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import CategoryList from '@/components/home/CategoryList.vue'
import ProductList from '@/components/home/item/ProductList.vue'
import { useProductStore } from '@/stores/product'

const productStore = useProductStore()

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

// onMounted(() => {
//   productStore.now_category = 'popular'
// })
</script>

<style scoped></style>
