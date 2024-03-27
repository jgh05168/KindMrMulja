import { ref} from 'vue'
import { defineStore } from 'pinia'

export const useViewStore = defineStore('view',() => {
    
    const now_value = ref(0) 

  return {now_value}
}, { persist: true })
