<template>
  <div>
    <v-form class="login" v-model="form" @submit.prevent>
      <h1>로그인하기</h1>

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

      <span>비밀번호 찾기</span>

      <v-btn color="#212121" type="submit" variant="elevated" @click="Login"> 로그인 </v-btn>

      <span><RouterLink :to="{ name: 'signup' }">회원가입 하기</RouterLink></span>
    </v-form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()

const form = ref(null)
const email = ref(null)
const password = ref(null)

// 로그인 하면 로그인 요청을 서버에 보내고
// 서버 응답이 OK 이면 로그인 되며
// Home 페이지로 이동
const Login = () => {
  router.push({ name: 'home' })
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
