import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import LoginView from '@/views/auth/LoginView.vue'
import SignupView from '@/views/auth/SignupView.vue'
import HomeView from '@/views/HomeView.vue'
import DetailView from '@/views/DetailView.vue'
import AddressView from '@/views/AddressView.vue'
import CreateAddress from '@/views/CreateAddress.vue'
import CartView from '@/views/CartView.vue'
import PayView from '@/views/PayView.vue'
import PaidView from '@/views/PaidView.vue'
import OrderView from '@/views/OrderView.vue'
import WishView from '@/views/WishView.vue'
import ProfileView from '@/views/auth/ProfileView.vue'
import MapView from '@/views/MapView.vue'
import RobotStatusView from '@/views/RobotStatusView.vue'
import { useAuthStore } from '@/stores/auth'
import { useOrderStore } from '@/stores/order'
import { useViewStore } from '@/stores/view'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/main',
      name: 'main',
      component: MainView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '/my-address',
      name: 'address',
      component: AddressView,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        if (authStore.user_id == null) {
          // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
          console.log(from.fullPath)
          authStore.redirectUrl = from.fullPath
          alert('로그인이 필요한 서비스 입니다.')
          next('/login')
        } else {
          next()
        }
      }
    },
    {
      path: '/create-address',
      name: 'create-address',
      component: CreateAddress,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        if (authStore.user_id == null) {
          // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
          console.log(from.fullPath)
          authStore.redirectUrl = from.fullPath
          alert('로그인이 필요한 서비스 입니다.')
          next('/login')
        } else {
          next()
        }
      }
    },
    {
      path: '/my-cart',
      name: 'cart',
      component: CartView,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        if (authStore.user_id == null) {
          // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
          console.log(from.fullPath)
          authStore.redirectUrl = from.fullPath
          alert('로그인이 필요한 서비스 입니다.')
          next('/login')
        } else {
          next()
        }
      }
    },
    {
      path: '/pay',
      name: 'pay',
      component: PayView,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        const orderStore = useOrderStore()
        if (authStore.user_id == null) {
          // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
          console.log(from.fullPath)
          authStore.redirectUrl = from.fullPath
          alert('로그인이 필요한 서비스 입니다.')
          next('/login')
        } else if (orderStore.selected_item.length < 1) {
          alert('선택한 상품이 없습니다.')
          next('/my-cart')
        } else {
          next()
        }
        if (!from.name && to.name == 'pay') {
          alert('결제를 실패하였습니다.')
        }
      }
    },
    {
      path: '/paid',
      name: 'paid',
      component: PaidView,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        const orderStore = useOrderStore()
        if (authStore.user_id == null) {
          // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
          console.log(from.fullPath)
          authStore.redirectUrl = from.fullPath
          alert('로그인이 필요한 서비스 입니다.')
          next('/login')
        } else if (orderStore.orderInfo == null) {
          // 주문지가 생성되지 않았으면
          alert('주문한 상품이 없습니다.')
          next('/my-cart')
        } else {
          next()
        }
      }
    },
    {
      path: '/my-order',
      name: 'order',
      component: OrderView,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        if (authStore.user_id == null) {
          // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
          console.log(from.fullPath)
          authStore.redirectUrl = from.fullPath
          alert('로그인이 필요한 서비스 입니다.')
          next('/login')
        } else {
          next()
        }
      }
    },
    {
      path: '/zzim',
      name: 'zzim',
      component: WishView,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        if (authStore.user_id == null) {
          // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
          console.log(from.fullPath)
          authStore.redirectUrl = from.fullPath
          alert('로그인이 필요한 서비스 입니다.')
          next('/login')
        } else {
          next()
        }
      }
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/factory_map',
      name: 'factory_map',
      component: MapView
    },
    {
      path: '/robots_status',
      name: 'robots_status',
      component: RobotStatusView
    }
  ]
})

router.beforeEach((to, from, next) => {
  const viewStore = useViewStore()

  console.log(`이동: ${from.name} -> ${to.name}`)
  // 현재 가는 곳이 탭에 있는 곳이면 탭 value에 맞게 수정
  if (to.name == 'home') {
    viewStore.now_value = 0
  } else if (to.name == 'zzim') {
    viewStore.now_value = 1
  } else if (to.name == 'cart') {
    viewStore.now_value = 2
  } else if (to.name == 'profile') {
    viewStore.now_value = 3
  }
  next()
})

export default router
