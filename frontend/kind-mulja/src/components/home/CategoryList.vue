<template>
  <v-sheet class="" max-width="415px">
    <!-- 다중선택 multiple 옵션 -->
    <v-slide-group show-arrows>
      <v-slide-group-item v-for="n in 25" :key="n">
        <CategoryItem>
          <!-- CategoryItem 이라는 하위 컴포넌트의 img-btn slot 에 표시할 버튼을 정의 -->
          <template #category-img>
            <v-img
              :src="`https://picsum.photos/500/300?image15`"
              aspect-ratio="1"
              class="bg-grey-lighten-2"
              :class="{ 'selected-category': NowCategory === n }"
              cover
              @click="toggle(n)"
            >
            </v-img>
          </template>
          <template #category-title>
            <span>title</span>
          </template>
        </CategoryItem>
      </v-slide-group-item>
    </v-slide-group>
  </v-sheet>
</template>

<script setup>
import { ref } from 'vue'
import CategoryItem from '@/components/home/CategoryItem.vue'

const NowCategory = ref(1)

const toggle = (n) => {
  NowCategory.value = n
}
</script>

<style scoped>
.selected-category {
  border: 2px solid red;
}
</style>
