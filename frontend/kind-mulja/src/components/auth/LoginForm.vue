<template>
  <div>
    <v-form class="login" v-model="form" @submit.prevent="Login">
      <h1>로그인하기</h1>

      <v-text-field
        v-model="email"
        color="primary"
        label="Email"
        variant="underlined"
        :rules="[rules.emailform]"
      ></v-text-field>

      <v-text-field
        v-model="password"
        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show1 ? 'text' : 'password'"
        :rules="[rules.required]"
        color="primary"
        label="Password"
        placeholder="Enter your password"
        variant="underlined"
        @click:append="show1 = !show1"
      ></v-text-field>

      <!-- <span>비밀번호 찾기</span> -->

      <v-btn color="#212121" type="submit" variant="elevated"> 로그인 </v-btn>

      <span><RouterLink :to="{ name: 'signup' }">회원가입 하기</RouterLink></span>
    </v-form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Service from '@/api/api.js'
import { useAuthStore } from '@/stores/auth'
import { useOrderStore } from '@/stores/order'
import { useProductStore } from '@/stores/product'

const productStore = useProductStore()
const orderStore = useOrderStore()
const authStore = useAuthStore()
const router = useRouter()

const show1 = ref(false)
const rules = ref({
  required: (value) => !!value || '값을 입력해주세요.',
  emailform: (value) => {
    if (/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/i.test(value)) return true
    return '이메일 형식에 맞게 입력해주세요.'
  }
})

const form = ref(null)
const email = ref(null)
const password = ref(null)

const check_zzim = () => {
  productStore.product_list.forEach(async (product) => {
    const check_res = await Service.checkProductWish(authStore.user_id, product.product_id)
    console.log('상품 찜 여부 : ', check_res.result)
    product.is_zzim = check_res.result
  })
}

const Login = async () => {
  // 로그인 요청 보내기 전에 form 유효성 검사
  console.log('로그인 유효성 검사', form.value)
  if (form.value) {
    // 로그인 하면 로그인 요청을 서버에 보내고
    const login_res = await Service.SignIn(email.value, password.value)
    // 서버 응답이 OK 이면 로그인 되며
    if (login_res.result) {
      authStore.user_id = login_res.user_id
      orderStore.address_list = await Service.getAddress(login_res.user_id)
      // 로그인 요청 완료 되면 사용자별로 상품들을 찜 했는지 안헀는지 체크해줘야 함
      await check_zzim()
      // Home 페이지로 이동
      router.push({ name: 'home' })
    } else {
      // 로그인 실패했다고 문구 띄어주기
      alert('아이디가 일치하지 않거나, 비밀번호가 틀렸습니다.')
    }
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
