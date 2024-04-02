<template>
  <v-item-group>
    <v-container>
      <v-row>
        <v-col v-for="robot in props.robots" :key="robot.turtle_id" cols="12" md="4">
          <v-item :value="robot.turtle_id">
            <v-card
              :class="[
                'd-flex align-center',
                robot.turtlebot_status == 1 ? 'moving-turtle' : 'stay-turtle',
                robot.turtle_id == selectedId ? 'selected-turtle' : ''
              ]"
              height="200"
              dark
              @click="toggle(robot.turtle_id)"
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
import { ref, defineProps, defineEmits } from 'vue'

const emit = defineEmits(['robotSelected'])

const props = defineProps({
  robots: Array
})

const selectedId = ref(null)

const toggle = (id) => {
  if (selectedId.value == id) {
    selectedId.value = null
  } else {
    selectedId.value = id
    // console.log(selectedId.value)
  }
  emit('robotSelected', selectedId.value) // 이벤트 발생
}
</script>

<style scoped>
.moving-turtle {
  border: 6px solid #4caf50;
  border-radius: 10%;
}

.stay-turtle {
  border: 6px solid #b71c1c;
  border-radius: 10%;
}

.selected-turtle {
  background-color: #424242;
  color: white;
}
</style>
