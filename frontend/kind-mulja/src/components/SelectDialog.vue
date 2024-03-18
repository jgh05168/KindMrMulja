<template>
  <v-dialog v-model="dialog" width="400px" scrollable>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        icon="mdi-home-switch-outline"
        variant="plain"
        size="xs"
        style="scale: 1.4"
        v-bind="activatorProps"
      ></v-btn>
    </template>

    <v-card>
      <v-card-title style="display: flex; justify-content: space-between">
        <div style="display: flex; align-items: center">
          <v-icon icon="mdi-truck-delivery-outline" class="me-3"></v-icon>
          <p>Select Address</p>
        </div>
        <CreateDialog></CreateDialog>
      </v-card-title>
      <v-divider class="mt-1"></v-divider>

      <v-card-text class="px-4" style="height: 500px">
        <AddressItem
          :width="'300px'"
          @click="clickAddress(idx)"
          :class="{ 'selected-address': idx == selected_Address }"
          v-for="(address, idx) in address_list"
          :value="address.id"
          :key="idx"
        >
          <template v-slot:address-title="slotProps">
            <div
              style="
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
              "
            >
              <div>{{ address.title }}</div>
              <!-- 지금 배송지의 id 를 인자로 수정 페이지로 이동 -->
              <v-btn
                @click="slotProps.editAddress(address.id)"
                icon="mdi-home-edit-outline"
                variant="plain"
              ></v-btn>
            </div>
          </template>
          <template #address-detail>
            <div>{{ address.detail }}</div>
          </template>
        </AddressItem>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn text="Close" @click="dialog = false"></v-btn>

        <v-spacer></v-spacer>

        <v-btn color="surface-variant" text="Save" variant="flat" @click="saveChange"></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script setup>
import AddressItem from '@/components/AddressItem.vue'
import CreateDialog from '@/components/CreateDialog.vue'

import { ref } from 'vue'

const dialog = ref(false)

const address_list = ref([
  {
    id: 1,
    title: '삼성전자 광주사업장 1',
    detail: '광주 관산구 하남산단 6번로 107, SSAFY 멀티캠퍼스'
  },
  {
    id: 2,
    title: '삼성전자 광주사업장 2',
    detail: '광주 관산구 하남산단 6번로 107, SSAFY 멀티캠퍼스'
  },
  {
    id: 3,
    title: '삼성전자 광주사업장 3',
    detail: '광주 관산구 하남산단 6번로 107, SSAFY 멀티캠퍼스'
  }
])

const selected_Address = ref('')

const clickAddress = (idx) => {
  selected_Address.value = idx
}

const saveChange = () => {
  dialog.value = false
  // 상위 컴포넌트에 선택된 주소지를 현재 다이얼로그에서 선택된 주소로 바꾸기
  // address = address_list[idx]
}
</script>

<style scoped>
.selected-address {
  border: 2px solid greenyellow;
}
</style>
