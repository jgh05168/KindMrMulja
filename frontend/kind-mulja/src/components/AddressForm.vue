<template>
  <div class="address-form">
    <v-form class="signup" v-model="form" @submit.prevent="createAddress()">
      <!-- 도로명 주소 API 를 사용해 클릭하면 모달창, 선택 결과를 해당 value 값으로 사용 -->
      <h3>배송 주소</h3>
      <v-text-field
        clearable
        :label="address_label"
        variant="outlined"
        v-model="address"
        @click="sample6_execDaumPostcode()"
        :rules="[rules.required]"
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
        :rules="[rules.required]"
      ></v-text-field>

      <v-text-field
        clearable
        label="받는사람"
        variant="outlined"
        v-model="name"
        :rules="[rules.required]"
      ></v-text-field>

      <h3>연락처</h3>
      <v-text-field
        clearable
        label="전화번호"
        variant="outlined"
        v-model="phone_number"
        :rules="[rules.required, rules.phoneNumber]"
        hint="하이픈(-)을 빼고 입력해주세요"
      ></v-text-field>

      <v-checkbox
        v-model="is_default"
        color="secondary"
        label="기본 배송지로 설정하기"
        @click="toggle"
      ></v-checkbox>

      <div class="create-address-button">
        <BlackButton type="submit" :buttonWidth="width">
          <template v-slot:button-text>배송지 저장</template>
        </BlackButton>
      </div>
    </v-form>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue'
import BlackButton from '@/components/BlackButton.vue'
import Service from '@/api/api.js'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { useAddressStore } from '@/stores/address'

const props = defineProps({
  nowView: String
})

const emit = defineEmits(['address-created'])

const addressStore = useAddressStore()

const router = useRouter()

const form = ref(null)

// 배송지 저장 버튼 가로길이 커스텀
const width = ref('100%')
const authStore = useAuthStore()
// 기본 배송지 체크
const is_default = ref(0)
const address = ref('')
const extra_address = ref('')
const address_name = ref('')
const name = ref('')
const phone_number = ref('')
let address_label = ref('우편번호 찾기')

const phoneRegex = /^\d{10,11}$/ // 숫자 10자리 또는 11자리

const rules = ref({
  required: (value) => !!value || '값이 입력되어야 합니다.',
  phoneNumber: (value) => {
    if (!phoneRegex.test(value.trim())) {
      return '올바른 전화번호 형식이 아닙니다. (숫자 10자리 또는 11자리만 입력 가능)'
    } else {
      return true
    }
  }
})

// 배송지 생성 요청이 성공했을 때 해당 함수를 호출하여 이벤트를 발생시킵니다
const handleAddressSubmit = async () => {
  // console.log("상위 컴포넌트로 배송지 생성 했다고 보내기")
  // 성공했다고 가정하고:
  emit('address-created')
}

const createAddress = async () => {
  if (form.value == true) {
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
      // console.log(info)
      await Service.addDelivery(info)
      await addressStore.getAddress()
      handleAddressSubmit()
      if (props.nowView == 'from-addressview') {
        // 이전 페이지로 이동
        router.go(-1)
      } else if (props.nowView == 'from-payview') {
        //
      }
    } catch (error) {
      console.log(error)
    }
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
  padding-bottom: 50px;
}

/* 폼 안의 모든 요소들의 넓이와 레이아웃 설정 */
.address-form * {
  width: 90%;
  margin: 8px auto;
}

/* 폼 구성 요소 중 span 태그의 텍스트 정렬 속성 추가 */
.address-form span {
  text-align: center;
}
</style>
