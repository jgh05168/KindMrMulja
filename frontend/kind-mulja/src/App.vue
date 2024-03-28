<template>
  <div>
    <RouterLink :to="{ name: 'main' }">main</RouterLink> /
    <RouterLink :to="{ name: 'login' }">login</RouterLink> /
    <RouterLink :to="{ name: 'home' }">home</RouterLink> /
    <RouterLink :to="{ name: 'address' }">address</RouterLink> /
    <RouterLink :to="{ name: 'create-address' }">create-address</RouterLink> /
    <RouterLink :to="{ name: 'cart' }">my-cart</RouterLink> /
    <RouterLink :to="{ name: 'pay' }">Pay</RouterLink> /
    <RouterLink :to="{ name: 'paid' }">Paid</RouterLink> /
    <RouterLink :to="{ name: 'order' }">my-order</RouterLink> /
    <RouterLink :to="{ name: 'zzim' }">ZZIM</RouterLink> /
  </div> -->
  <div class="phone">
    <RouterView />
    <AppFooter />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
// import AppHeader from '@/layouts/AppHeader.vue'
import AppFooter from '@/layouts/AppFooter.vue'
import { useProductStore } from './stores/product'
import Service from '@/api/api.js'

const productStore = useProductStore()

onMounted(async () => {
  const productList_res = await Service.getProductList()
  // console.log('상품 전체 리스트 : ', productList_res)
  // 전체 상품 돌면서 찜 기능을 위한 속성 추가
  productList_res.forEach(async (product) => {
    product.is_zzim = false // 찜 속성 추가 및 초기화
  })

  // productList_res가 어디서 온 것인지 확인이 필요합니다.
  console.log('상품 전체 리스트 - is_zzim 추가 : ', productList_res)
  productStore.product_list = productList_res
})
</script>

<style scoped>
.phone {
  position: relative;
  height: 100vh;
}

.app-footer {
  position: fixed;
}
</style>
