<template>
  <div class="login-view">
    <AuthHeader />

    <div class="login-form">
      <LoginForm />
    </div>
  </div>
</template>

<script setup>
import AuthHeader from '@/layouts/AuthHeader.vue'
import LoginForm from '@/components/auth/LoginForm.vue'
</script>

<style scoped>
.login-view {
  width: 100%;
  height: 100%;
}
</style>
