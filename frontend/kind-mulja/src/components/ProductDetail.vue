<template>
  <ProductItem>
    <template #item-img>
      <v-carousel height="500" show-arrows="hover" hide-delimiters>
        <v-carousel-item :src="`/product/${item_id}.jpg`"></v-carousel-item>
        <v-carousel-item :src="`/product/${item_id}_showroom.jpg`"></v-carousel-item>
      </v-carousel>
    </template>

    <template #item-title>
      <span
        style="color: brown; font-weight: bold"
        v-if="props.item.product_stock !== null && props.item.product_stock < 5"
        >남은 재고 {{ props.item.product_stock }} 개, 품절임박!!</span
      >
      <h2>{{ props.item.product_name }}</h2>
      <div class="mt-3 d-flex">
        <v-chip
          style="font-weight: bold"
          v-for="summary in Utils.splitStringByComma(props.item.summary)"
          :key="summary"
        >
          {{ summary }}
        </v-chip>
      </div>
    </template>

    <template #item-price>
      <div class="mt-3" style="display: flex; flex-direction: row; align-items: center">
        <v-icon>mdi-currency-krw</v-icon>
        <span style="font-size: 30px; font-weight: bold">{{
          Utils.numberWithCommas(props.item.product_price)
        }}</span>
      </div>
    </template>

    <template #item-description>
      <div class="mt-8 mb-7" style="font-size: 17px; font-weight: 500">
        {{ props.item.description }}
      </div>
      <div>
        <span style="font-size: 13px; font-weight: 400">제품번호. </span>
        <span
          style="
            background-color: black;
            color: aliceblue;
            font-weight: 1000;
            padding: 2px 10px;
            border-radius: 10%;
          "
          >{{ item_id }}</span
        >
      </div>
    </template>
    <template #item-size>
      <div style="height: 300px">
        <div
          style="
            border-top: 1px solid gray;
            border-bottom: 1px solid gray;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: space-between;
          "
          class="mt-10 shrink"
          @click="expand = !expand"
        >
          <p class="ms-7" style="font-weight: bold; font-size: 24px">치수</p>
          <v-icon class="me-7">mdi-arrow-down</v-icon>
        </div>
        <v-expand-transition>
          <div
            style="height: 600px; padding: 10px 20px; font-size: 17px; font-weight: bold"
            v-show="expand"
          >
            <p>가로 : {{ props.item.width }} cm</p>
            <p>세로 : {{ props.item.length }} cm</p>
            <p>높이 : {{ props.item.height }} cm</p>
            <v-img width="300px" :src="`/product/${item_id}_size.jpg`"></v-img>
          </div>
        </v-expand-transition>
      </div>
    </template>
  </ProductItem>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'
import Utils from '@/utils/utils'
import ProductItem from '@/components/home/item/ProductItem.vue'

const route = useRoute()

const props = defineProps({
  item: Object
})

const item_id = ref(route.params.id)

const expand = ref(true)
</script>

<style scoped>
.detail-frame {
  position: relative;
  margin: 0 7%;
  padding-bottom: 100px;
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
