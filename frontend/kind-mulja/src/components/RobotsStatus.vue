<template>
  <v-item-group selected-class="selected-turtle">
    <v-container>
      <v-row>
        <v-col v-for="robot in robots" :key="robot.turtle_id" cols="12" md="4">
          <v-item :value="robot.turtle_id" v-slot="{ selectedClass, toggle }">
            <v-card
              :class="[
                'd-flex align-center',
                selectedClass,
                robot.turtlebot_status == 1 ? 'moving-turtle' : 'stay-turtle'
              ]"
              height="200"
              dark
              @click="toggle"
              style="display: flex; flex-direction: column"
            >
              <v-card-title>
                <h3>터틀봇 {{ robot.turtle_id }}</h3>
                <p>{{ robot.turtlebot_status == 1 ? '상품 이송 중' : '대기중' }}</p>
                <p>현재 {{ robot.progress_detail_id }}</p>
              </v-card-title>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
</template>

<script setup>
import Service from '@/api/api'
import { ref, onMounted } from 'vue'

const robots = ref([{}])

onMounted(async () => {
  robots.value = await Service.getOrderTutle()
})
</script>

<style scoped>
.moving-turtle {
  border: 6px solid #4caf50;
  border-radius: 10%;
}

.stay-turtle {
  border: 2px solid #b71c1c;
}

.selected-turtle {
  background-color: #c8e6c9;
}
</style>
