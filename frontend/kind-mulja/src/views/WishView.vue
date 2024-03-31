<template>
  <AppHeader>
    <template #header-bar>좋아요 누른 상품</template>
  </AppHeader>
  <div class="wish-frame">
    <v-container style="">
      <v-row v-if="wish_list.length > 0">
        <v-col
          v-for="item in wish_list"
          :key="item.order_detail_id"
          :value="item.product_id"
          cols="12"
          style="padding: 0 0"
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
            <template #item-price>{{ Utils.numberWithCommas(item.product_price) }}</template>

            <template #cancel-btn>
              <v-btn size="xs" variant="plain" @click="deleteZzim(item.wishlist_id)"
                ><v-icon size="35">mdi-close-circle-outline</v-icon></v-btn
              >
            </template>
          </CartItem>
        </v-col>
      </v-row>
      <v-row v-else>
        <v-col cols="12" style="text-align: center; margin-top: 40%">
          <v-icon
            class="go-to-zzim bounce"
            @click="router.push({ name: 'home' })"
            color="red-accent-1"
            size="100"
            >mdi-heart-outline</v-icon
          >
          <h2>담으러 가기</h2>
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
import Utils from '@/utils/utils'

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
<style scoped>
.wish-frame {
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

.bounce {
  animation: bounce 1s infinite;
}

.go-to-zzim {
}
</style>
