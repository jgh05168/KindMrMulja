<template>
  <div class="login-view">
    <AuthHeader />

    <div class="register-form">
      <SignupForm />
    </div>
  </div>
</template>

<script setup>
import AuthHeader from '@/layouts/AuthHeader.vue'
import SignupForm from '@/components/auth/SignupForm.vue'
</script>

<style scoped>
.login-view {
  width: 100%;
  height: 100%;
}
</style>
