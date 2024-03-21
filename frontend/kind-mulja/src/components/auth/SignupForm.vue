<template>
  <div>
    <v-form class="signup" v-model="form" @submit.prevent="CreateAccount">
      <h1>회원가입</h1>

      <v-text-field v-model="name" color="primary" label="Name" variant="underlined"></v-text-field>

      <v-text-field
        v-model="email"
        :rules="[rules.emailMatch]"
        color="primary"
        label="Email"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="password"
        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required, rules.min]"
        :type="show1 ? 'text' : 'password'"
        hint="Enter your password to access this website"
        color="primary"
        label="Password"
        placeholder="Enter your password"
        variant="underlined"
        @click:append="show1 = !show1"
      ></v-text-field>

      <v-text-field
        v-model="password_check"
        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required, rules.min, rules.pw_check]"
        :type="show2 ? 'text' : 'password'"
        color="primary"
        label="Password Check"
        placeholder="Enter your password"
        variant="underlined"
        @click:append="show2 = !show2"
      ></v-text-field>

      <v-checkbox
        v-model="terms"
        color="secondary"
        label="I agree to site terms and conditions"
      ></v-checkbox>

      <v-btn color="#212121" type="submit" variant="elevated"> 회원 가입 </v-btn>
      <span>이미 계정이 있다면, <RouterLink :to="{ name: 'login' }">Login</RouterLink></span>
    </v-form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Service from '@/api/api.js'

const router = useRouter()

// 비밀번호 표시 ox 기능을 위한 변수
const show1 = ref(false)
const show2 = ref(false)
const rules = ref({
  required: (value) => !!value || '값이 입력되어야 합니다.',
  min: (v) => (v.length >= 8 && v.length <= 16) || '최소 8글자 최대 16',
  emailMatch: () => `이메일 형식이 맞지 않습니다.`,
  pw_check: () => password_check.value == password.value || '비밀번호가 일치하지 않습니다.'
})
// ---

// 회원가입 폼 내의 변수들
const form = ref(null)
const name = ref(null)
const email = ref(null)
const password = ref(null)
const password_check = ref(null)
const terms = ref(false)
// ---

const CreateAccount = async () => {
  // 유효성 검사
  const duplicate_check = await Service.email_duplicate_check(email.value)
  console.log('이메일 중복검사', duplicate_check)
  // 조건을 다 만족하면 통과

  // 유효성 검사를 통과 하면 회원가입 진행
  try {
    const res = await Service.SignUp({
      name: name.value,
      email: email.value,
      password: password.value
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
</style>
