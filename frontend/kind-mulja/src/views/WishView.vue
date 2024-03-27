<template>
  <AppHeader>
    <template #header-bar> ZZIM </template>
  </AppHeader>
  <div>
    <CartItem
      v-for="item in wish_list"
      :key="item.order_detail_id"
      :value="item.product_id"
      :item-quentity="item.order_quentity"
      @click="router.push({ name: 'detail', params: { id: item.product_id } })"
    >
      <template #item-image>
        <v-img :src="`/product/${item.product_id}.jpg`"></v-img>
      </template>
      <template #item-name>{{ item.product_name }}</template>
      <template #item-price>{{ item.product_price }}</template>
      <template #item-cnt>
        <!-- 상품 수량 변경 시 DB 에도 장바구니 수량 변경 요청 보내야 함 -->
        <span>{{ item.order_quentity }}</span>
      </template>
      <template #cancel-btn>
        <v-btn @click="deleteZzim(item.wishlist_id)"><v-icon>mdi-close</v-icon></v-btn>
      </template>
    </CartItem>
  </div>
</template>

<script setup>
import AppHeader from '@/layouts/AppHeader.vue'
import CartItem from '@/components/cart/CartItem.vue'
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import Service from '@/api/api'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()
const wish_list = ref([])

const getWishlist = async () => {
  wish_list.value = await Service.getWishList(authStore.user_id)
}

const deleteZzim = async (id) => {
  await Service.deleteWish(id)
  await getWishlist()
}

onMounted(async () => {
  console.log('위시리스트 목록', wish_list)
  await getWishlist()
})
</script>
<style scoped></style>
