// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/DefaultEnter.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
    ],
  },
  {
    path: '/build-route',
    component: () => import('@/layouts/default/Default.vue'),
    children:[
      {
        path: '',
        name: 'BuildRoute',
        component: () => import('@/views/BuildRoute.vue')
      }
    ]
  },
  {
    path: '/generate-ice-conditions',
    component: () => import('@/layouts/default/Default.vue'),
    children:[
      {
        path: '',
        name: 'GenerateIceConditions',
        component: () => import('@/views/GenerateIceConditions.vue')
      }
    ]

  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
