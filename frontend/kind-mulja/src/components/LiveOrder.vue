<template>
  <v-card title="" flat>
    <template v-slot:text>
      <v-card-title class="d-flex align-center pe-2">
        <v-icon icon="mdi-video-input-component"></v-icon> &nbsp; 실시간 주문 정보
        <v-spacer></v-spacer>

        <v-text-field
          v-model="search"
          density="compact"
          label="Search"
          prepend-inner-icon="mdi-magnify"
          variant="solo-filled"
          flat
          hide-details
          single-line
        ></v-text-field>
      </v-card-title>
    </template>

    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
      items-per-page="5"
    ></v-data-table>
  </v-card>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import Service from '@/api/api'

const search = ref('')
const headers = [
  {
    align: 'start',
    key: 'order_id',
    sortable: false,
    title: '주문번호'
  },
  { key: 'order_detail_id', title: '상세id' },
  { key: 'product_id', title: '상품코드' },
  { key: 'order_quentity', title: '주문수량' },
  { key: 'order_progress', title: '진행수량' },
  { key: 'moving_zone', title: '분류장소' },
  { key: 'is_progress', title: '완료수량' }
]
const orderItems = [{}]

onMounted(async () => {
  orderItems.value = await Service.getOrderProcessingList()
})
</script>
