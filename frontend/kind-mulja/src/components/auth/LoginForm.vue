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

      <v-btn :loading="loading" color="#212121" type="submit" variant="elevated"> 로그인 </v-btn>

      <span>회원가입 하기</span>
    </v-form>
  </div>
</template>

<script setup></script>

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
