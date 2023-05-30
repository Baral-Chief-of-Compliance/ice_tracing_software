// Composables
import { createRouter, createWebHistory } from 'vue-router'
import { isAuthorized } from '@/store/TokenStore'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    beforeEnter(to) {
      // redirect back home
      if (isAuthorized) {
        return '/'
      }
    },
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
      {
        path: '/registration',
        name: 'Registration',
        component: () => import('@/views/Registration.vue'),
      },
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
