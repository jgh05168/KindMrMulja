<template>
  <AppHeader>
    <template #header-bar>친절한 물자씨</template>
  </AppHeader>
  <div class="home-frame">
    <v-tabs
      v-model="tab"
      align-tabs="center"
      :center-active="true"
      show-arrows
      height="70px"
      density="comfortable"
      color="black"
    >
      <v-tab
        v-for="(item, idx) in productStore.category"
        :key="idx"
        :value="item.id"
        elevation="1"
        ripple
      >
        <CategoryItem>
          <!-- CategoryItem 이라는 하위 컴포넌트의 img-btn slot 에 표시할 버튼을 정의 -->
          <template #category-img>
            <v-icon size="30">{{ item.icon }}</v-icon>
          </template>
          <template #category-title>
            <span>{{ item.title }}</span>
          </template>
        </CategoryItem>
      </v-tab>
    </v-tabs>
    <v-window v-model="tab">
      <v-window-item
        v-for="(category, idx) in productStore.category"
        :key="idx"
        :value="category.id"
      >
        <ProductList :category-id="category.id"></ProductList>
      </v-window-item>
    </v-window>
  </div>
</template>

<script setup>
import { onUpdated, onMounted } from 'vue'
// import CategoryList from '@/components/home/CategoryList.vue'
import CategoryItem from '@/components/home/CategoryItem.vue'
import ProductList from '@/components/home/item/ProductList.vue'
import AppHeader from '@/layouts/AppHeader.vue'
import { useProductStore } from '@/stores/product'
import { useAuthStore } from '@/stores/auth'
import Service from '@/api/api'
import { ref } from 'vue'

const productStore = useProductStore()
const authStore = useAuthStore()

const tab = ref(null)

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

<style scoped>
.home-frame {
  width: 100%;
  height: 100vh;
}
</style>
