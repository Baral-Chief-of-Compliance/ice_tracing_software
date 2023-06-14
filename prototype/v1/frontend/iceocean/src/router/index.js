// Composables
import { createRouter, createWebHistory } from 'vue-router'
import RouteInfo from '@/views/RouteInfo.vue'
import Routes from '@/views/Routes.vue'
import Home from '@/views/Home.vue'
import AddRoute from '@/views/AddRoute.vue'
import Login from '@/views/Login.vue'
import Registration from '@/views/Registration.vue'
import { isAuthorizedRouter } from '@/store/TokenStore'
import Mistake from '@/views/Mistake.vue'
import HistoryOfRoute from '@/views/HistoryOfRoute.vue'
import Manual from '@/views/Manual.vue'


const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/registration',
    name: 'Registration',
    component: Registration
  },
  {
    path: '/mistake',
    name: 'Mistake',
    component: Mistake
  },
  {
    path: '/',
    component: () => import('@/layouts/default/DefaultEnter.vue'),
    beforeEnter(to) {
      // redirect back home
      if (isAuthorizedRouter()) {
        return '/login'
      }
    },
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: Home
      }
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
        component: Routes
      },
      {
        path: 'add-route',
        name: 'AddRoute',
        component: AddRoute
      },
      {
        path:'routes/:id_rt',
        name: 'RouteInfo',
        component: RouteInfo
      },
      {
        path: 'routes/:id_rt/history_of_route',
        name: 'HistoryOfRoute',
        component: HistoryOfRoute
      },
      {
        path: 'manual',
        name: 'Manual',
        component: Manual
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
