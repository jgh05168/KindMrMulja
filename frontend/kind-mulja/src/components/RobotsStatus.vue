<template>
  <v-item-group selected-class="bg-primary">
    <v-container>
      <v-row>
        <v-col v-for="n in 3" :key="n" cols="12" md="4">
          <v-item v-slot="{selectedClass, toggle }">
            <v-card
              :class="['d-flex align-center', selectedClass]"
              height="200"
              dark
              @click="toggle"
              style="display: flex; flex-direction: column"
            >
              <v-card-title>
                <h3>로봇 {{ n }}</h3>
                <v-icon><mdi-dot></mdi-dot></v-icon>
              </v-card-title>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
</template>

<script setup>

</script>

<style scoped></style>
