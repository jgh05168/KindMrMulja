<template>
  <v-sheet class="" max-width="415px">
    <!-- 다중선택 multiple 옵션 -->
    <v-slide-group show-arrows>
      <v-slide-group-item v-for="(item, idx) in productStore.category" :key="idx">
        <CategoryItem>
          <!-- CategoryItem 이라는 하위 컴포넌트의 img-btn slot 에 표시할 버튼을 정의 -->
          <template #category-img>
            <v-btn
              :icon="item.icon"
              aspect-ratio="1"
              class="bg-grey-lighten-2"
              :class="{ 'selected-category': productStore.now_category === item.id }"
              @click="toggle(item.id)"
              size="large"
              style="border-radius: 20%"
            >
            </v-btn>
          </template>
          <template #category-title>
            <span>{{ item.title }}</span>
          </template>
        </CategoryItem>
      </v-slide-group-item>
    </v-slide-group>
  </v-sheet>
</template>

<script setup>
import { ref } from 'vue'
import CategoryItem from '@/components/home/CategoryItem.vue'
import { useProductStore } from '@/stores/product'

const productStore = useProductStore()

const NowCategory = ref('popular')

const toggle = (id) => {
  NowCategory.value = id
  productStore.now_category = id
}
</script>

<style scoped>
.selected-category {
  border: 2px solid red;
}
</style>
