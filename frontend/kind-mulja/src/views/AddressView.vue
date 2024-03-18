<template>
  <div style="position: relative">
    <AppHeader>
      <template #header-bar> 배송지 목록 </template>
    </AppHeader>
    <div>
      <AddressItem
        :width="'360px'"
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
      @click="goCreate"
      icon="mdi-plus"
      style="position: fixed; bottom: 10%; right: 5%"
    ></v-btn>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import AddressItem from '@/components/AddressItem.vue'
import AppHeader from '@/layouts/AppHeader.vue'

const router = useRouter()

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

const click_id = ref(null)

const clickAddress = (id) => {
  click_id.value = id
  console.log('클릭된 주소 순서-', click_id.value)
}

const default_address = ref(1)

const setDefault = (id) => {
  default_address.value = id
  // 기본 배송지 설정 버튼을 눌렀으므로 현재 선택된 배송지 초기화
  click_id.value = null
  console.log('기본 배송지 설정, 클릭 요소 초기화', click_id.value)
}

const sorted_address_list = computed(() => {
  const default_idx = address_list.value.findIndex(
    (address) => address.id === default_address.value
  )

  if (default_idx !== -1) {
    return [
      address_list.value[default_idx],
      ...address_list.value.slice(0, default_idx),
      ...address_list.value.slice(default_idx + 1)
    ]
  } else {
    return [...address_list.value]
  }
})

const goCreate = () => {
  router.push({ name: 'create-address' })
}
</script>

<style scoped>
.address-list {
}

.default-address {
  border: 2px solid #424242;
}

.set-default {
}
</style>
