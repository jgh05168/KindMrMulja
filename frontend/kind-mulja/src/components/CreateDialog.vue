<template>
   <div class="pa-4 text-center">
    <v-dialog
      v-model="dialog"
      max-width="600"
    >
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          size="xs"
          icon="mdi-plus-box"
          variant="flat"
          class="text-none font-weight-regular"
          v-bind="activatorProps"

        ></v-btn>
      </template>

      <v-card>
        <AddressForm></AddressForm>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            text="Close"
            variant="plain"
            @click="dialog = false"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import AddressForm from '@/components/AddressForm.vue'

import {ref} from 'vue'

const dialog = ref(false)

</script>

<style scoped>

</style>