import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from '../views/LandingPage.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    name: 'LandingPage',
    redirect: '/Signin',
    component: LandingPage,
    children: [
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
      {
        path: '/Home',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Home'),
        meta: { title: 'Home' }
      },
    ]

  },

]

const router = new VueRouter({
  base: process.env.BASE_URL,
  // mode: 'history',
  routes
})

function getCookie(name) {
  if (!document.cookie) {
    return null;
  }

  const xsrfCookies = document.cookie.split(';')
    .map(c => c.trim())
    .filter(c => c.startsWith(name + '='));

  if (xsrfCookies.length === 0) {
    return null;
  }
  return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

router.beforeEach((to, from, next) => {

  if(getCookie('login')){
    if (to.path !== '/Home'){
      router.push({ path: '/Home' })
    }
    else{
      next()
    }
      
  }
  else{
    if (to.path !== '/Signin'){
      router.push({ path: '/Signin' })
    }
    else{
      next()
    }
  }
  
})
export default router
