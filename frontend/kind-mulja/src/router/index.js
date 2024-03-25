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
      component: LoginView
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
      component: AddressView
    },
    {
    path: '/create-address',
    name: 'create-address',
    component: CreateAddress
  },
  {
    path: '/my-cart',
    name: 'cart',
    component: CartView
  },
  {
    path: '/pay',
    name: 'pay',
    component: PayView
  },
  {
    path: '/paid',
    name: 'paid',
    component: PaidView
  },
  {
    path: '/my-order',
    name: 'order',
    component: OrderView
  },
  {
    path: '/zzim',
    name: 'zzim',
    component: WishView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  ]
})

export default router
