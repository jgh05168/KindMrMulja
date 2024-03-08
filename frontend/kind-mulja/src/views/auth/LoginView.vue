<template>
  <div class="login-view">
    <AuthHeader />

    <div class="login-form">
      <LoginForm />
    </div>

    <div class="register-form">
      <SignupForm />
    </div>
  </div>
</template>

<script setup>
import AuthHeader from '@/components/auth/AuthHeader.vue'
import LoginForm from '@/components/auth/LoginForm.vue'
import SignupForm from '@/components/auth/SignupForm.vue'
</script>

<style scoped>
.login-view {
  width: 100%;
  height: 100%;
}
</style>
