<template>
  <div style="position: relative">
    <AppHeader>
      <template #header-bar> 배송지 목록 </template>
    </AppHeader>
    <div>
      <AddressItem
        :width="'90%'"
        @click="clickAddress(n)"
        :class="{ 'default-address': address.id == default_address }"
        v-for="(address, n) in sorted_address_list"
        :value="address.id"
        :key="n"
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
            <div>
              <span style="font-size: 23px; font-weight: bold">{{ address.title }}</span
              ><v-chip class="ms-2" size="small" v-if="default_address == address.id"
                >기본배송지</v-chip
              >
            </div>
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
          <div style="text-align: end" v-if="default_address !== address.id && n == click_id">
            <v-btn
              @click="setDefault(address.id)"
              class="set-default"
              color="success"
              prepend-icon="mdi-home"
              variant="tonal"
              >기본 배송지로 설정하기
            </v-btn>
          </div>
        </template>
      </AddressItem>
    </div>
    <v-btn
      color="success"
      @click="goCreate"
      icon="mdi-plus"
      style="position: fixed; bottom: 10%; right: 5%"
    ></v-btn>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AddressItem from '@/components/AddressItem.vue'
import AppHeader from '@/layouts/AppHeader.vue'
import { useAuthStore } from '@/stores/auth'
import Service from '@/api/api.js'
import { useOrderStore } from '@/stores/order'
const router = useRouter()
const authStore = useAuthStore()
const orderStore = useOrderStore()
// console.log(authStore.user_id)
const default_address = ref([null])
// getAddress 메서드 호출
onMounted(async () => {
  const address_res = await Service.getAddress(authStore.user_id)
  orderStore.address_list = address_res.map((item) => ({
    id: item.address_id,
    title: item.address_name,
    detail: `${item.address_normal} ${item.address_detail}`,
    is_default: item.is_default
  }))
  const defaultAddress = address_res.find((item) => item.is_default === 1)
  default_address.value = defaultAddress ? defaultAddress.address_id : null
})
const click_id = ref(null)

const clickAddress = (id) => {
  click_id.value = id
  // console.log('클릭된 주소 순서-', click_id.value)
}

const sorted_address_list = computed(() => {
  const default_idx = orderStore.address_list.findIndex(
    (address) => address.id == default_address.value
  )
  let sorted_array = []
  if (default_idx !== -1) {
    sorted_array = [
      orderStore.address_list[default_idx],
      ...orderStore.address_list.slice(0, default_idx),
      ...orderStore.address_list.slice(default_idx + 1)
    ]
  } else {
    sorted_array = [...orderStore.address_list]
  }
  return sorted_array
})

const setDefault = async (id) => {
  default_address.value = id
  // 기본 배송지 설정 버튼을 눌렀으므로 현재 선택된 배송지 초기화
  click_id.value = null
  // console.log('기본 배송지 설정, 클릭 요소 초기화', click_id.value)
  await Service.setDefaultAddress(authStore.user_id, id)
  // orderStore.address_list = await Service.getAddress(authStore.user_id)
  // console.log(sorted_address_list.value)
}

const goCreate = () => {
  router.push({ name: 'create-address' })
}
</script>

<style scoped>
.address-list {
}

.default-address {
}

.set-default {
}
</style>
