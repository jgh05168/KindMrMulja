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
      :items="sortedOrderItems"
      :search="search"
      items-per-page="5"
    ></v-data-table>
  </v-card>
</template>
<script setup>
import { ref, onMounted,computed} from 'vue'
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
const orderItems = ref([{}])
const robots = ref([{}])

setInterval(async () => {
  robots.value = await Service.getOrderTutle()
}, 5000)

onMounted(async () => {
  orderItems.value = await Service.getOrderProcessingList()
  robots.value = await Service.getOrderTutle()
})

const sortedOrderItems = computed(() => {
  // robots 배열에서 progress_detail_id를 키로 하는 객체 생성
  const robotMap = {}
  robots.value.forEach(robot => {
    robotMap[robot.progress_detail_id] = true
  })

  // progress_detail_id를 가진 orderItems와 가지지 않은 orderItems 분리
  const itemsWithProgress = []
  const itemsWithoutProgress = []
  orderItems.value.forEach(item => {
    if (robotMap[item.order_detail_id]) {
      itemsWithProgress.push(item)
    } else {
      itemsWithoutProgress.push(item)
    }
  })

  // 가지고 있는 progress_detail_id를 기준으로 정렬된 배열 생성
  const sortedItems = [...itemsWithProgress, ...itemsWithoutProgress]

  return sortedItems
})

</script>
