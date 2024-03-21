<template>
  <div>
    <v-form class="login" v-model="form" @submit.prevent="Login">
      <h1>로그인하기</h1>

      <v-text-field
        v-model="email"
        color="primary"
        label="Email"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="password"
        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show1 ? 'text' : 'password'"
        :rules="[rules.required, rules.min]"
        hint="Enter your password to access this website"
        color="primary"
        label="Password"
        placeholder="Enter your password"
        variant="underlined"
        @click:append="show1 = !show1"
      ></v-text-field>

      <span>비밀번호 찾기</span>

      <v-btn color="#212121" type="submit" variant="elevated"> 로그인 </v-btn>

      <span><RouterLink :to="{ name: 'signup' }">회원가입 하기</RouterLink></span>
    </v-form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Service from '@/api/api.js'
import { useAuthStore } from '@/stores/auth';
import { useOrderStore } from '@/stores/order'

const orderStore = useOrderStore()
const authStore = useAuthStore()
const router = useRouter()

const show1 = ref(false)
const rules = ref({
  required: (value) => !!value || 'Required.',
  min: (v) => v.length >= 8 || 'Min 8 characters',
  emailMatch: () => `The email and password you entered don't match`
})

const form = ref(null)
const email = ref(null)
const password = ref(null)

// 로그인 하면 로그인 요청을 서버에 보내고
// 서버 응답이 OK 이면 로그인 되며
// Home 페이지로 이동
const Login = async () => {
  const login_res = await Service.SignIn(email.value, password.value)
  if (login_res.result) {
    // login_res.user_id
    authStore.user_id = login_res.user_id
    console.log('store 에 저장 확인',authStore.user_id)
    orderStore.address_list = await Service.getAddress(login_res.user_id)
    router.push({ name: 'home' })
  }
}
</script>

<style scoped>
/* 로그인 폼의 배치 설정 */
.login {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* 로그인 폼 안의 모든 요소들의 넓이와 레이아웃 설정 */
.login * {
  width: 80%;
  margin: 10px auto;
}

/* 로그인 폼 구성 요소 중 span 태그의 텍스트 정렬 속성 추가 */
.login span {
  text-align: center;
}
</style>
