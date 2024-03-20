import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  const category = ref([
    {id:'O',title:'인기', icon:'mdi-star'},
    {id:'C',title:'책상', icon:'mdi-desk'},
    {id:'E',title:'서랍장', icon:'mdi-inbox-multiple-outline'},
    {id:'D',title:'매트리스', icon:'mdi-bed-outline'},
    {id:'A',title:'옷장', icon:'mdi-wardrobe-outline'},
    {id:'B',title:'소파', icon:'mdi-wardrobe-outline'},
  ])
  
  const now_category = ref('O')

  const product_list = ref([])

  return {product_list, category, now_category }
})
