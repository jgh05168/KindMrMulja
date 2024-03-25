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
import { useAuthStore } from '@/stores/auth'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/home',
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
          authStore.redirectUrl = from.fullPath;
          alert('로그인이 필요한 서비스 입니다.')
          next('/login');
        } else {
          next();
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
        authStore.redirectUrl = from.fullPath;
        alert('로그인이 필요한 서비스 입니다.')
        next('/login');
      } else {
        next();
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
        authStore.redirectUrl = from.fullPath;
        alert('로그인이 필요한 서비스 입니다.')
        next('/login');
      } else {
        next();
      }
    }
  },
  {
    path: '/pay',
    name: 'pay',
    component: PayView,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (authStore.user_id == null) {
        // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
        console.log(from.fullPath)
        authStore.redirectUrl = from.fullPath;
        alert('로그인이 필요한 서비스 입니다.')
        next('/login');
      } else {
        next();
      }
    }
  },
  {
    path: '/paid',
    name: 'paid',
    component: PaidView,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (authStore.user_id == null) {
        // 로그인되어 있지 않으면 로그인 페이지로 이동하기 전에 이전 URL 저장
        console.log(from.fullPath)
        authStore.redirectUrl = from.fullPath;
        alert('로그인이 필요한 서비스 입니다.')
        next('/login');
      } else {
        next();
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
        authStore.redirectUrl = from.fullPath;
        alert('로그인이 필요한 서비스 입니다.')
        next('/login');
      } else {
        next();
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
        authStore.redirectUrl = from.fullPath;
        alert('로그인이 필요한 서비스 입니다.')
        next('/login');
      } else {
        next();
      }
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    
  },
  {
    path: '/tosspay',
    name: 'tosspay',
    component: () => import('../views/CheckoutView.vue')
  },
  {
    path: '/success',
    name: 'success',
    component: () => import('../views/SuccessView.vue')
  },
  {
    path: '/fail',
    name: 'fail',
    component: () => import('../views/FailView.vue')
  }
  ]
})


export default router
