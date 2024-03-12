<template>
  <div class="detail-frame">
    <v-btn icon="mdi-chevron-left" style="position: absolute; left: -5%; top: 3%; z-index: 99">
    </v-btn>

    <ProductItem>
      <template #item-img>
        <v-img
          aspect-ratio="3/4"
          src="https://source.unsplash.com/random/300x400/?furniture"
          style="border-bottom-left-radius: 10%"
        >
        </v-img>
      </template>
      <template #item-title>
        <p>상품 이름</p>
      </template>
      <template #item-price>
        <div style="display: flex; flex-direction: row; justify-content: space-between">
          <div>상품 가격</div>
          <div>
            <v-btn :disabled="cnt <= 1" @click="cnt--">-</v-btn>
            <input style="width: 20px" type="number" :value="cnt" />
            <v-btn @click="cnt++">+</v-btn>
          </div>
        </div>
      </template>

      <template #item-description>
        상품 설명ㄴㅇㅁ나엄너아ㅣㅁ너이ㅏ먼엄나ㅣㅓ이ㅏㅁ너아ㅣㅁ너ㅏ임너ㅏㅣ엄 ㅇㅁㄴㅇㅁㄴㅇㅁ
      </template>
    </ProductItem>

    <div class="buy-button">
      <v-btn @click="zzim" width="55px" height="55px" rounded="lg" :icon="zzim_state"></v-btn>
      <BlackButton @click="addCart" :buttonWidth="width">
        <template v-slot:button-text> 장바구니 </template>
      </BlackButton>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductItem from '@/components/home/item/ProductItem.vue'
import BlackButton from '@/components/BlackButton.vue'

const width = ref('280px')
const cnt = ref(1)

const is_zzim = ref(0)
const zzim_state = ref('mdi-bookmark-outline')

const zzim = () => {
  is_zzim.value = ~is_zzim.value
  // 사용자 찜 목록에 추가/삭제
  if (is_zzim.value == 0) {
    zzim_state.value = 'mdi-bookmark-outline'
  } else {
    zzim_state.value = 'mdi-bookmark'
  }
}

const addCart = () => {
  // 사용자 장바구니에 추가 요청
}
</script>

<style scoped>
.detail-frame {
  position: relative;
  margin: 0 7%;
}

.buy-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  position: fixed;
  bottom: 8%;
  width: 356.91px;
}
</style>
