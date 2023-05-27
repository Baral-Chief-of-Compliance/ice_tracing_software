// Composables
import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'


const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
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
        beforeEnter (to, from, next) {
          if (!store.getters.isAuthenticated) {
            next('/login')
          } else {
            next()
          }
        }
      },
      {
        path: '/add_records',
        name: 'AddRecords',

      }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
