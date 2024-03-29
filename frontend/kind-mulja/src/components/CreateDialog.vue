<template>
  <div class="pa-4 text-center">
    <v-dialog v-model="dialog" max-width="600">
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          size="xs"
          icon="mdi-plus-box"
          variant="flat"
          class="text-none font-weight-regular"
          v-bind="activatorProps"
        ></v-btn>
      </template>

      <v-card rounded="xl">
        <v-card-title
          class="mt-2"
          style="text-align: center; font-size: 30px; font-weight: bold; height: 60px"
        >
          배송지 작성하기
        </v-card-title>

        <v-divider></v-divider>
        <AddressForm :now-view="'from-payview'" :dialog="dialog" @address-created="handleAddressCreated"></AddressForm>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import AddressForm from '@/components/AddressForm.vue'

import { ref } from 'vue'

const dialog = ref(false)

const handleAddressCreated = () => {
  dialog.value = false // 배송지가 생성되면 다이얼로그를 닫음
}

</script>

<style scoped></style>
