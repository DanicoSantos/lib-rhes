import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import Home from '../views/Home.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import Books from '../views/dashboard/Books.vue'
import BookInstances from '../views/dashboard/BookInstances.vue'
import BookDetail from '../views/dashboard/BookDetail.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/log-in',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/books',
    name: 'Books',
    component: Books,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/books/book/:id',
    name: 'BookInstances',
    component: BookInstances,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/books/book/book-detail/:id',
    name: 'BookDetail',
    component: BookDetail,
    meta: {
      requireLogin: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})
export default router
