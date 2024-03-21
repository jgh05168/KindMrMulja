<template>
  <ProductItem>
    <template #item-img>
      <v-carousel height="500" show-arrows="hover" hide-delimiters>
        <v-carousel-item :src="`/product/${item_id}.jpg`"></v-carousel-item>
        <v-carousel-item :src="`/product/${item_id}_showroom.jpg`"></v-carousel-item>
      </v-carousel>
    </template>

    <template #item-title>
      <h2>{{ props.item.product_name }}</h2>
      <div>
        {{ props.item.summary }}
      </div>
    </template>

    <template #item-price>
      <div style="display: flex; flex-direction: row; justify-content: space-between">
        <div><v-icon>mdi-currency-krw</v-icon>{{ props.item.product_price }}</div>
      </div>
    </template>

    <template #item-description>
      <h3>상품 정보</h3>
      <div>
        {{ props.item.description }}
      </div>
    </template>
    <template #item-size>
      <h3>치수</h3>
      <span>가로 {{ props.item.width }}</span>
      <span>세로 {{ props.item.length }}</span>
      <span>높이 {{ props.item.height }}</span>
      <v-img :src="`/product/${item_id}_size.jpg`"></v-img>
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
