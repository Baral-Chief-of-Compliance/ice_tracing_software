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
    path: '/iceocean',
    component: () => import('@/layouts/default/Default.vue'),
    children:[
      {
        path: 'build-route',
        name: 'BuildRoute',
        component: () => import('@/views/BuildRoute.vue')
      },
      {
        path: 'generate-ice-conditions',
        name: 'GenerateIceConditions',
        component: () => import('@/views/GenerateIceConditions.vue')
      },
      {
        path: 'routes',
        name: 'Routes',
        component: () => import('@/views/Routes.vue')
      },
      {
        path: 'add-route',
        name: 'AddRoute',
        component: () => import('@/views/AddRoute.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
