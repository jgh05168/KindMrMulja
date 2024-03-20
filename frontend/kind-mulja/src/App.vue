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
  </div>
  <div class="galaxy_24">
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
  console.log('상품 전체 리스트 : ', productList_res)
  productStore.product_list = productList_res
})
</script>

<style scoped>
.galaxy_24 {
  width: 415px;
  height: 900px;
}
</style>
