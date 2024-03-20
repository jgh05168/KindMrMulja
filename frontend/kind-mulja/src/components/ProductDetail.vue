<template>
  <ProductItem>
    <template #item-img>
      <v-carousel height="500" show-arrows="hover" hide-delimiters>
        <v-carousel-item :src="`/product/${item_id}.jpg`"></v-carousel-item>
        <v-carousel-item :src="`/product/${item_id}_showroom.jpg`"></v-carousel-item>
        <v-carousel-item :src="`/product/${item_id}_size.jpg`"></v-carousel-item>
      </v-carousel>
    </template>
    <template #item-title>
      <p>{{ props.item }}</p>
    </template>
    <template #item-price>
      <div style="display: flex; flex-direction: row; justify-content: space-between">
        <div>상품 가격</div>
      </div>
    </template>

    <template #item-description>
      상품 설명ㄴㅇㅁ나엄너아ㅣㅁ너이ㅏ먼엄나ㅣㅓ이ㅏㅁ너아ㅣㅁ너ㅏ임너ㅏㅣ엄 ㅇㅁㄴㅇㅁㄴㅇㅁ
    </template>
  </ProductItem>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'
import ProductItem from '@/components/home/item/ProductItem.vue'

const route = useRoute()

const props = defineProps({
  item: Object
})

const item_id = ref(route.params.id)
</script>

<style scoped>
.detail-frame {
  position: relative;
  margin: 0 7%;
}

.buy-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  position: fixed;
  bottom: 8%;
  width: 356.91px;
}
</style>
