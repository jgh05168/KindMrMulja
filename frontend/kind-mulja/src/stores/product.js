import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  const category = ref([
    {id:'popular',title:'인기', icon:'mdi-star-outline'},
    {id:'desk',title:'책상', icon:'mdi-desk'},
    {id:'drawer',title:'서랍장', icon:'mdi-inbox-multiple-outline'},
    {id:'mattress',title:'매트리스', icon:'mdi-bed-outline'},
    {id:'closet',title:'옷장', icon:'mdi-wardrobe-outline'},
    {id:'sofa',title:'소파', icon:'mdi-sofa-single-outline'},
  ])
  
  const now_category = ref('popular')

  const now_product_id = ref(null)

  const product_list = ref([])

  // 상세 페이지로 들어가는 버튼 클릭하면 보여줄 상품
  const item = ref({})


  return {product_list, category, now_category, item,
  now_product_id, }
}, { persist: true })
