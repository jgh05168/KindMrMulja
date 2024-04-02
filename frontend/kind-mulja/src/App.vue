<template>
  <div>
    <!-- <RouterLink :to="{ name: 'main' }">main</RouterLink> /
    <RouterLink :to="{ name: 'login' }">login</RouterLink> /
    <RouterLink :to="{ name: 'home' }">home</RouterLink> /
    <RouterLink :to="{ name: 'address' }">address</RouterLink> /
    <RouterLink :to="{ name: 'create-address' }">create-address</RouterLink> /
    <RouterLink :to="{ name: 'cart' }">my-cart</RouterLink> /
    <RouterLink :to="{ name: 'pay' }">Pay</RouterLink> /
    <RouterLink :to="{ name: 'paid' }">Paid</RouterLink> /
    <RouterLink :to="{ name: 'order' }">my-order</RouterLink> /
    <RouterLink :to="{ name: 'zzim' }">ZZIM</RouterLink> / -->
  </div>
  <!-- 만약 관리자 계정으로 로그인 된 경우, (조건문 걸어주기) -->
  <div v-if="authStore.is_admin == true" class="admin">
    <AdminPage />
  </div>

  <div v-else class="phone">
    <RouterView />
    <AppFooter />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterView } from 'vue-router'
// import AppHeader from '@/layouts/AppHeader.vue'
import AppFooter from '@/layouts/AppFooter.vue'
import { useProductStore } from './stores/product'
import Service from '@/api/api.js'
import { useAuthStore } from './stores/auth'
import AdminPage from '@/layouts/AdminPage.vue'

const productStore = useProductStore()
const authStore = useAuthStore()

onMounted(async () => {
  const productList_res = await Service.getProductList()
  productList_res.forEach(async (product) => {
    product.is_zzim = false
  })

  console.log('상품 전체 리스트 - is_zzim 추가 : ', productList_res)
  productStore.product_list = productList_res
})
</script>

<style scoped>
.galaxy_24 {
  width: 415px;
  height: 900px;
}

.phone {
  position: relative;
  width: 100%;
  height: 100vh;
  font-family: 'pretendard';
}

.admin {
  font-family: 'pretendard-extrabold';
}

.app-footer {
  position: fixed;
}

.link {
  text-decoration: none;
  color: black;
}

.link:hover {
  color: black; /* 변경하고자 하는 색상으로 설정하세요 */
}
</style>
