import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const user_id = ref(null)


  return { user_id  }
}, { persist: true })
