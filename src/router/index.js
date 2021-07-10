import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from '../views/LandingPage.vue'

Vue.use(VueRouter)

const routes = [
  
  {
    path: '/',
    mode: 'history',
    name: 'LandingPage',
    redirect: '/Signin',
    component: LandingPage,
    children:[
      {
        path: '/Signin',
        component: () => import(/* webpackChunkName: "demo" */ '../views/LoginView'),
        meta: { title: 'Sign In' }
        },
      {
        path: '/Signup',
        component: () => import(/* webpackChunkName: "demo" */ '../views/SignUpView'),
        meta: { title: 'Create Your Account' }
        },
    ]
    
  },
 
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  base: process.env.BASE_URL,
  mode: 'history',
  routes
})

export default router
