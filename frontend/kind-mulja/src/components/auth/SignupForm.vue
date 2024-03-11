<template>
  <div>
    <v-form class="login" v-model="form" @submit.prevent>
      <h1>회원가입</h1>

      <v-text-field v-model="name" color="primary" label="Name" variant="underlined"></v-text-field>

      <v-text-field
        v-model="email"
        color="primary"
        label="Email"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="password"
        hint="Enter your password to access this website"
        color="primary"
        label="Password"
        placeholder="Enter your password"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="password_check"
        color="primary"
        label="Password Check"
        placeholder="Enter your password"
        variant="underlined"
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
import { RouterLink } from 'vue-router'

const form = ref(null)
const name = ref(null)
const email = ref(null)
const password = ref(null)
const password_check = ref(null)
const terms = ref(false)
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
