<template>
  <div class="address-form">
    <h2>배송주소</h2>
    <!-- 도로명 주소 API 를 사용해 클릭하면 모달창, 선택 결과를 해당 value 값으로 사용 -->
    <v-text-field
      clearable
      :label="address_label"
      variant="outlined"
      v-model="address"
      @click="sample6_execDaumPostcode()"
    >
    </v-text-field>
    <v-text-field
      clearable
      label="상세주소"
      hint="도로명 주소를 제외한 상세주소만 입력해주세요."
      variant="outlined"
      v-model="extra_address"
    ></v-text-field>

    <h3>기본 정보</h3>
    <v-text-field
      clearable
      label="배송지명"
      variant="outlined"
      v-model="address_name"
    ></v-text-field>

    <v-text-field clearable label="이름" variant="outlined" v-model="name"></v-text-field>

    <h3>연락처</h3>
    <v-text-field
      clearable
      label="전화번호"
      hint="국가번호 없이 입력해주세요."
      variant="outlined"
      v-model="phone_number"
    ></v-text-field>
    <v-checkbox
      v-model="is_default"
      color="secondary"
      label="기본 배송지로 설정하기"
      @click="toggle"
    ></v-checkbox>

    <div class="create-address-button">
      <BlackButton @click="createAddress" :buttonWidth="width">
        <template v-slot:button-text>배송지 저장</template>
      </BlackButton>
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import BlackButton from '@/components/BlackButton.vue'
import Service from '@/api/api.js'
import { useAuthStore } from '@/stores/auth'
// 배송지 저장 버튼 가로길이 커스텀
const width = ref('100%')
const authStore = useAuthStore()
// 기본 배송지 체크
const is_default = ref(0)
const address = ref('')
const extra_address = ref('')
const address_name = ref('')
const combined_address = ref('')
const name = ref('')
const phone_number = ref('')
let address_label = ref('우편번호 찾기')
const createAddress = async () => {
  try {
    const info = {
      user_id: authStore.user_id,
      address_name: address_name.value,
      user_name: name.value,
      address_normal: address.value,
      address_detail: extra_address.value,
      phone_number: phone_number.value,
      is_default: is_default.value
    }
    console.log(info)
    const results = await Service.addDelivery(info)
    console.log(results)
  } catch (error) {}
}

const toggle = () => {
  if (is_default.value === 1) {
    is_default.value = 0
  } else {
    is_default.value = 1
  }
}
function sample6_execDaumPostcode() {
  new daum.Postcode({
    oncomplete: function (data) {
      // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

      // 각 주소의 노출 규칙에 따라 주소를 조합한다.
      // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
      var addr = '' // 주소 변수
      var extraAddr = '' // 참고항목 변수

      //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
      if (data.userSelectedType === 'R') {
        // 사용자가 도로명 주소를 선택했을 경우
        addr = data.roadAddress
      } else {
        // 사용자가 지번 주소를 선택했을 경우(J)
        addr = data.jibunAddress
      }

      // 사용자가 선택한 주소가 도로명 타입일때 참고항목을 조합한다.
      if (data.userSelectedType === 'R') {
        // 법정동명이 있을 경우 추가한다. (법정리는 제외)
        // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
        if (data.bname !== '' && /[동|로|가]$/g.test(data.bname)) {
          extraAddr += data.bname
        }
        // 건물명이 있고, 공동주택일 경우 추가한다.
        if (data.buildingName !== '' && data.apartment === 'Y') {
          extraAddr += extraAddr !== '' ? ', ' + data.buildingName : data.buildingName
        }
        // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
        if (extraAddr !== '') {
          extraAddr = ' (' + extraAddr + ')'
        }
        // 조합된 참고항목을 해당 필드에 넣는다.
        extra_address.value = extraAddr
      } else {
        extra_address.value = ''
      }
      address.value = addr
      address_label = '주소'
    }
  }).open()
}
watchEffect(() => {
  combined_address.value = address.value + ' ' + extra_address.value
  console.log(combined_address.value)
  console.log(is_default)
})
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
