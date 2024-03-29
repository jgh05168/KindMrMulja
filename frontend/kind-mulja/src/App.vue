<template>
  <div>
    <RouterLink :to="{ name: 'main' }" class="link">main</RouterLink> /
    <RouterLink :to="{ name: 'login' }" class="link">login</RouterLink> /
    <RouterLink :to="{ name: 'home' }" class="link">home</RouterLink> /
    <RouterLink :to="{ name: 'address' }" class="link">address</RouterLink> /
    <RouterLink :to="{ name: 'create-address' }" class="link">create-address</RouterLink> /
    <RouterLink :to="{ name: 'cart' }" class="link">my-cart</RouterLink> /
    <RouterLink :to="{ name: 'pay' }" class="link">Pay</RouterLink> /
    <RouterLink :to="{ name: 'paid' }" class="link">Paid</RouterLink> /
    <RouterLink :to="{ name: 'order' }" class="link">my-order</RouterLink> /
    <RouterLink :to="{ name: 'zzim' }" class="link">ZZIM</RouterLink> /
  </div>

  <!-- 만약 관리자 계정으로 로그인 된 경우, (조건문 걸어주기) -->
  <v-card>
    <v-layout style="position: relative; height: 100vh">
      <v-navigation-drawer floating permanent style="position: relative">
        <v-list dense nav>
          <RouterLink :to="{ name: 'factory_map' }" tag="v-list-item" class="link">
            <template v-slot:default="{ attrs }">
              <v-list-item
                v-bind="attrs"
                prepend-icon="mdi-factory"
                title="Factory Map"
                value="factory_map"
                color="black"
              ></v-list-item>
            </template>
          </RouterLink>
          <RouterLink :to="{ name: 'robots_status' }" tag="v-list-item" class="link">
            <template v-slot:default="{ attrs }">
              <v-list-item
                v-bind="attrs"
                prepend-icon="mdi-robot"
                title="Robots"
                value="robots"
                color="black"
              ></v-list-item>
            </template>
          </RouterLink>
        </v-list>
      </v-navigation-drawer>
      <v-main style="padding-left: 0; flex-grow: 1">
        <RouterView />
      </v-main>
    </v-layout>
  </v-card>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import AppFooter from '@/layouts/AppFooter.vue'
import { useProductStore } from './stores/product'
import Service from '@/api/api.js'
import io from 'socket.io-client'

const productStore = useProductStore()

onMounted(async () => {
  const productList_res = await Service.getProductList()
  productList_res.forEach(async (product) => {
    product.is_zzim = false
  })

  const socket = io('http://localhost:12002/')

  socket.on('connect', () => {
    console.log('웹소켓 연결이 열렸습니다.')
  })

  socket.on('error', (error) => {
    console.error('웹소켓 에러:', error)
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
