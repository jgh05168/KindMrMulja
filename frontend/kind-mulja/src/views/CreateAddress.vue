<template>
  <div class="address-form">
    <h2>배송주소</h2>
    <!-- 도로명 주소 API 를 사용해 클릭하면 모달창, 선택 결과를 해당 value 값으로 사용 -->
    <v-text-field
      clearable
      label="우편번호"
      hint="도로명 주소를 제외한 상세주소만 입력해주세요."
      variant="outlined"
    ></v-text-field>
    <v-text-field clearable label="상세주소" variant="outlined"></v-text-field>

    <h3>기본 정보</h3>
    <v-text-field clearable label="배송지명" variant="outlined"></v-text-field>

    <v-text-field clearable label="이름" variant="outlined"></v-text-field>

    <h3>연락처</h3>
    <v-text-field
      clearable
      label="전화번호"
      hint="국가번호 없이 입력해주세요."
      variant="outlined"
    ></v-text-field>
    <v-text-field clearable label="이메일" hint="ssafy@gmail.com" variant="outlined"></v-text-field>

    <v-checkbox v-model="is_default" color="secondary" label="기본 배송지로 설정하기"></v-checkbox>

    <div class="create-address-button">
      <BlackButton @click="createAddress" :buttonWidth="width">
        <template v-slot:button-text>배송지 저장</template>
      </BlackButton>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BlackButton from '@/components/BlackButton.vue'

// 배송지 저장 버튼 가로길이 커스텀
const width = ref('100%')

// 기본 배송지 체크
const is_default = ref(false)

const createAddress = () => {
  // 배송지 생성 요청
}
</script>

<style scoped>
.create-address-button {
  position: fixed;
  bottom: 8%;
}

/*  폼의 배치 설정 */
.address-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* 폼 안의 모든 요소들의 넓이와 레이아웃 설정 */
.address-form * {
  width: 80%;
  margin: 8px auto;
}

/* 폼 구성 요소 중 span 태그의 텍스트 정렬 속성 추가 */
.address-form span {
  text-align: center;
}
</style>
