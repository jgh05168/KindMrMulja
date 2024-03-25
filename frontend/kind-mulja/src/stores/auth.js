import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const user_id = ref(null)
  const redirectUrl = ref(null)


  return { user_id , redirectUrl }
}, { persist: true })
