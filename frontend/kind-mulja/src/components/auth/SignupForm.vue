<template>
  <div>
    <v-form class="signup" v-model="form" @submit.prevent="CreateAccount()">
      <h1>회원가입</h1>

      <v-text-field
        v-model="name"
        color="primary"
        label="Name"
        variant="underlined"
        :rules="[rules.name]"
      ></v-text-field>

      <v-text-field
        v-model="email"
        :rules="[rules.required, rules.emailform, rules.email_check]"
        :append-inner-icon="email_icon"
        hint="이메일 작성 후, 우측 중복 체크를 해주세요."
        color="primary"
        label="Email"
        variant="underlined"
        @click:append-inner="duplicate_check()"
        :class="{
          'possible-email': email_duplicate == false,
          'impossible-email': email_duplicate == true
        }"
      ></v-text-field>

      <v-text-field
        v-model="password"
        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required, rules.pwform]"
        :type="show1 ? 'text' : 'password'"
        color="primary"
        label="Password"
        variant="underlined"
        @click:append="show1 = !show1"
      ></v-text-field>

      <v-text-field
        v-model="password_check"
        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required, rules.pw_check]"
        :type="show2 ? 'text' : 'password'"
        color="primary"
        label="Password Check"
        variant="underlined"
        @click:append="show2 = !show2"
      ></v-text-field>
      <!-- 
      <v-checkbox
        style="margin: 0 auto; display: flex; justify-content: center"
        v-model="allowAlarm"
        label="푸쉬 알림 권한 동의"
        color="secondary"
      ></v-checkbox> -->

      <BlackButton type="submit" buttonWidth="80%">
        <template #button-text>회원가입</template>
      </BlackButton>
      <span>이미 계정이 있다면, <RouterLink :to="{ name: 'login' }">Login</RouterLink></span>
    </v-form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Service from '@/api/api.js'
import BlackButton from '../BlackButton.vue'

const router = useRouter()

// 비밀번호 표시 ox 기능을 위한 변수
const show1 = ref(false)
const show2 = ref(false)
const rules = ref({
  required: (value) => !!value || '값이 입력되어야 합니다.',
  name: (value) => {
    if (!value) {
      return '값이 입력되어야 합니다.'
    }

    let errorMessage = ''

    if (/[^가-힣a-zA-Z]/g.test(value)) {
      errorMessage += '한글(자음, 모음 불가), 영문자로 이루어진 '
    }

    if (value.length < 2) {
      errorMessage += '2 글자 이상의 '
    }

    if (errorMessage) {
      errorMessage += '이름이어야 합니다.'
      return errorMessage
    }

    return true
  },
  pwform: (value) => {
    let errorMessage = '비밀번호는'
    // 최소 8글자 이상 16글자 이하인지 확인
    if (value.length < 8 || value.length > 16) {
      errorMessage += '최소 8글자 최대 16글자,\n'
    }

    // 알파벳과 숫자가 하나 이상 포함되었는지 확인
    if (!/[A-Za-z]/.test(value) || !/\d/.test(value)) {
      errorMessage += '알파벳과 숫자 하나 이상,\n'
    }

    // 특수문자(@$!%*#?&)가 하나 이상 포함되었는지 확인
    if (!/[@$!%*#?&]/.test(value)) {
      errorMessage += '특수문자(@$!%*#?&)가 하나 이상,'
    }

    if (errorMessage == '비밀번호는') {
      // 모든 조건을 만족하면 유효한 비밀번호로 간주
      return true
    } else {
      return errorMessage + '이어야 합니다.'
    }
  },
  pw_check: () => password_check.value == password.value || '비밀번호가 일치하지 않습니다.',
  emailform: (value) => {
    if (/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/i.test(value)) return true
    return '이메일 형식에 맞게 입력해주세요.'
  },
  email_check: () => {
    if (email_duplicate.value == true) {
      return '중복된 이메일입니다.'
    } else {
      return true
    }
  }
})
// ---

// 회원가입 폼 내의 변수들
const form = ref(null)
const name = ref(null)
const email = ref(null)
const password = ref(null)
const password_check = ref(null)
// const terms = ref(false)
const email_duplicate = ref(null)
// 알림 권한
// const allowAlarm = ref(false)

const email_icon = computed(() => {
  if (email_duplicate.value == null) {
    return ' mdi-circle-outline'
  } else if (email_duplicate.value == true) {
    return 'mdi-cancel'
  } else {
    return 'mdi-check-circle-outline'
  }
})

const duplicate_check = async () => {
  if (email.value !== null) {
    const res = await Service.email_duplicate_check(email.value)
    console.log('이메일 중복검사', res)
    // 만약 이메일이 중복이라면 결과 값 false 로 반환됨
    if (res.result == false) {
      email_duplicate.value = true
    } else {
      email_duplicate.value = false
    }
  }
}

const CreateAccount = async () => {
  await duplicate_check() // 혹시 모르니까 중복체크 한번 더
  if (email_duplicate.value) {
    alert('이미 가입된 이메일 입니다.')
    return
  }
  // 유효성 검사 통과하면 회원가입 진행
  if (form.value) {
    // 유효성 검사를 통과 하면 회원가입 진행
    try {
      const res = await Service.SignUp({
        name: name.value,
        email: email.value,
        password: password.value,
      })
      // 만약 회원가입이 성공적으로 되었다면
      if (res.result) {
        // 로그인 페이지로
        router.push({ name: 'login' })
      }
    } catch (err) {
      err.value = err.message
      throw err
    }
  }
}
</script>

<style scoped>
/* 회원가입 폼의 배치 설정 */
.signup {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* 회원가입 폼 안의 모든 요소들의 넓이와 레이아웃 설정 */
.signup * {
  width: 80%;
  margin: 10px auto;
}

/* 회원가입 폼 구성 요소 중 span 태그의 텍스트 정렬 속성 추가 */
.signup span {
  text-align: center;
}

/* 이메일 중복체크에 따른 스타일 */
.possible-email {
  color: rgba(27, 114, 44, 0.883);

}

.impossible-email {
  color: rgba(240, 16, 16, 0.839);
}
</style>
