<template>
  <div class="address-form">
    <!-- 도로명 주소 API 를 사용해 클릭하면 모달창, 선택 결과를 해당 value 값으로 사용 -->
    <v-text-field
      clearable
      :label="address_label"
      variant="outlined"
      v-model="address"
      @click="sample6_execDaumPostcode()"
      :error-messages="address_errors"
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
      :error-messages="address_name_errors"
    ></v-text-field>

    <v-text-field
      clearable
      label="이름"
      variant="outlined"
      v-model="name"
      :error-messages="name_errors"
    ></v-text-field>

    <h3>연락처</h3>
    <v-text-field
      clearable
      label="전화번호"
      variant="outlined"
      v-model="phone_number"
      :error-messages="phone_number_errors"
      hint="하이픈(-)을 빼고 입력해주세요"
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
import { ref, watchEffect, watch } from 'vue'
import BlackButton from '@/components/BlackButton.vue'
import Service from '@/api/api.js'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
const router = useRouter()

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
const address_errors = ref([])
const address_name_errors = ref([])
const name_errors = ref([])
const phone_number_errors = ref([])
let address_label = ref('우편번호 찾기')

const validateForm = () => {
  let isValid = true
  address_errors.value = []
  address_name_errors.value = []
  name_errors.value = []
  phone_number_errors.value = []

  if (!address.value || !address.value.trim()) {
    address_errors.value.push('주소를 입력해주세요.')
    isValid = false
  }

  if (!address_name.value || !address_name.value.trim()) {
    address_name_errors.value.push('배송지명을 입력해주세요.')
    isValid = false
  }

  if (!name.value || !name.value.trim()) {
    name_errors.value.push('이름을 입력해주세요.')
    isValid = false
  }

  if (!phone_number.value || !phone_number.value.trim()) {
    phone_number_errors.value.push('전화번호를 입력해주세요.')
    isValid = false
  }

  const phoneRegex = /^\d{10,11}$/ // 숫자 10자리 또는 11자리
  if (!phoneRegex.test(phone_number.value.trim())) {
    phone_number_errors.value.push(
      '올바른 전화번호 형식이 아닙니다. (숫자 10자리 또는 11자리만 입력 가능)'
    )
    isValid = false
  }

  return isValid
}

const createAddress = async () => {
  try {
    if (!validateForm()) return
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
    router.go(-1)
  } catch (error) {
    console.log(error)
  }
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
      var addr = ''
      var extraAddr = ''
      if (data.userSelectedType === 'R') {
        addr = data.roadAddress
      } else {
        addr = data.jibunAddress
      }
      if (data.userSelectedType === 'R') {
        if (data.bname !== '' && /[동|로|가]$/g.test(data.bname)) {
          extraAddr += data.bname
        }
        if (data.buildingName !== '' && data.apartment === 'Y') {
          extraAddr += extraAddr !== '' ? ', ' + data.buildingName : data.buildingName
        }
        if (extraAddr !== '') {
          extraAddr = ' (' + extraAddr + ')'
        }
        extra_address.value = extraAddr
      } else {
        extra_address.value = ''
      }
      address.value = addr
      address_label.value = '주소'
    }
  }).open()
}

watch(address, (newValue) => {
  if (newValue && newValue.trim() !== '') {
    address_errors.value = []
  }
})

// address_name 값이 변경될 때마다 유효성 검사 수행
watch(address_name, (newValue) => {
  if (newValue && newValue.trim() !== '') {
    address_name_errors.value = []
  }
})

// name 값이 변경될 때마다 유효성 검사 수행
watch(name, (newValue) => {
  if (newValue && newValue.trim() !== '') {
    name_errors.value = []
  }
})

// phone_number 값이 변경될 때마다 유효성 검사 수행
watch(phone_number, (newValue) => {
  if (newValue && newValue.trim() !== '') {
    phone_number_errors.value = []
  }
})

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
