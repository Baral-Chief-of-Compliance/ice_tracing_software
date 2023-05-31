// Composables
import { createRouter, createWebHistory } from 'vue-router'
import { isAuthorizedRouter } from '@/store/TokenStore'
import Home from '@/views/Home.vue'
import Registration from '@/views/Registration.vue'


const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Home
  },
  {
    path: '/registration',
    name: 'Registration',
    component: Registration
  },
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    beforeEnter(to) {
      // redirect back home
      if (isAuthorizedRouter()) {
        return '/login'
      }
    },
    children: [
      {
        path: '/records',
        name: 'Records',
        component: () => import('@/views/Records.vue'),
      }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})


export default router
