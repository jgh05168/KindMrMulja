<template>
  <v-dialog v-model="dialog" width="85%" scrollable>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn variant="plain" size="xs" style="scale: 1" v-bind="activatorProps"
        ><v-chip><v-icon size="20">mdi-home-switch-outline</v-icon>배송지 선택</v-chip></v-btn
      >
    </template>

    <v-card rounded="xl">
      <v-card-title style="display: flex; justify-content: space-between">
        <div style="display: flex; align-items: center">
          <v-icon icon="mdi-truck-delivery-outline" class="me-3"></v-icon>
          <p style="font-weight: bold">배송지 목록</p>
        </div>
        <CreateDialog></CreateDialog>
      </v-card-title>
      <v-divider class="mt-1"></v-divider>

      <v-card-text class="px-4" style="height: 500px">
        <AddressItem
          :width="'90%'"
          @click="clickAddress(address)"
          :class="{ 'selected-address': address == selected_Address }"
          v-for="(address, idx) in addressStore.state.address_list"
          :value="address.address_id"
          :key="idx"
        >
          <template #address-title>
            <div
              style="
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
              "
            >
              <div>{{ address.address_name }}</div>
            </div>
          </template>
          <template #address-detail>
            <p>{{ address.address_normal }}</p>
            <p>{{ address.address_detail }}</p>
            <p>{{ address.user_name }}</p>
          </template>
        </AddressItem>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn text="Close" @click="dialog = false"></v-btn>

        <v-spacer></v-spacer>

        <v-btn
          color="surface-variant"
          rounded="xl"
          text="Save"
          variant="flat"
          @click="saveChange"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script setup>
// import Service from '@/api/api'
import AddressItem from '@/components/AddressItem.vue'
import CreateDialog from '@/components/CreateDialog.vue'
// import { useAuthStore } from '@/stores/auth'
import { useAddressStore } from '@/stores/address'
import { defineEmits } from 'vue'
import { ref, onMounted, onUpdated } from 'vue'

const emit = defineEmits(['update:addressId', 'update:selectedAddress'])
// const authStore = useAuthStore()
const addressStore = useAddressStore()

const dialog = ref(false)

const selected_Address = ref('')

const clickAddress = (address) => {
  selected_Address.value = address
}

const saveChange = () => {
  dialog.value = false
  // 상위 컴포넌트에 선택된 주소지를 현재 다이얼로그에서 선택된 주소로 바꾸기
  emit('update:addressId', selected_Address.value.address_id)
  emit('update:selectedAddress', selected_Address.value)
}

onUpdated(async () => {
  await addressStore.getAddress()
})

onMounted(async () => {
  await addressStore.getAddress()
})
</script>

<style scoped>
.selected-address {
  scale: 1.08;
  transition: 0.1s ease-in-out;
  border: 2px solid #757575;
}
</style>
