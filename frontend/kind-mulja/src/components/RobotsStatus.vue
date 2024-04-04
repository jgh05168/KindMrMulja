<template>
  <v-item-group>
    <v-container>
      <v-row>
        <v-col v-for="robot in props.robots" :key="robot.turtle_id" cols="12" md="4">
          <v-item :value="robot.turtle_id">
            <v-card
              rounded="xl"
              elevation="6"
              style="display: flex; align-items: center"
              :class="[
                robot.turtlebot_status == 1 ? 'moving-turtle' : 'stay-turtle',
                robot.turtle_id == selectedId ? `selected-turtle${robot.turtle_id}` : ''
              ]"
              height="100"
              width="210"
              dark
              @click="toggle(robot.turtle_id)"
            >
              <v-avatar
                :class="[
                  robot.turtle_id == selectedId ? `selected-turtle-avatar${robot.turtle_id}` : ''
                ]"
                size="60"
                ><v-img src="/public/mulja.png"></v-img
              ></v-avatar>
              <div>
                <v-card-title style="display: flex">
                  <h4>터틀봇 {{ robot.turtle_id }}</h4>
                </v-card-title>

                <v-card-text>
                  <span>배정상품 : </span>
                  <span>{{
                    robot.progress_detail_id == 0 ? '없음' : robot.progress_detail_id
                  }}</span>
                </v-card-text>
              </div>
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
}

.stay-turtle {
  border: 6px solid #b71c1c;
}

.selected-turtle1 {
}

.selected-turtle2 {
}

.selected-turtle3 {
}

.selected-turtle-avatar1 {
  background-color: #ff1744;
  border: solid 1px black;
}

.selected-turtle-avatar2 {
  background-color: #ffff00;
  border: solid 1px black;
}

.selected-turtle-avatar3 {
  background-color: #1de9b6;
  border: solid 1px black;
}
</style>
