<template>
  <AppHeader>
    <template #header-bar> ZZIM </template>
  </AppHeader>
  <div class="wish-frame">
    <v-container>
        <v-row v-if="wish_list.length > 0">
          <v-col
            v-for="item in wish_list"
            :key="item.order_detail_id"
            :value="item.product_id"
            cols="12"
            style="padding: 0 0;"
            
          >
            <CartItem :item-quentity="item.order_quentity">
              <template #item-image>
                <v-img
                  aspect-ratio="1"
                  @click="router.push({ name: 'detail', params: { id: item.product_id } })"
                  :src="`/product/${item.product_id}.jpg`"
                ></v-img>
              </template>
              <template #item-name
                ><div @click="router.push({ name: 'detail', params: { id: item.product_id } })">
                  {{ item.product_name }}
                </div></template
              >
              <template #item-price>{{ item.product_price }}</template>

              <template #cancel-btn>
                <v-btn variant="plain" @click="deleteZzim(item.wishlist_id)"
                  ><v-icon size="35">mdi-close-circle-outline</v-icon></v-btn
                >
              </template>
            </CartItem>
            </v-col>
        </v-row>
        <v-row v-else>
          <v-col cols="12" style="text-align: center; height: fit-content">
            <p>아직 좋아요를 누른 상품이 없습니다.</p>
            <v-icon @click="router.push({ name: 'home' })" color="grey" size="100"
              >mdi-cart-arrow-down</v-icon
            >
            <p>담으러 가기</p>
          </v-col>
        </v-row>
    </v-container>
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
