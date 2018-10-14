import Vue from 'vue';
import Router from 'vue-router';
// import Home from './views/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import (/* webpackChunkName: "customer" */ './views/customer/CustomerHome.vue'),
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import(/* webpackChunkName: "auth" */ './views/Login.vue'),
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import(/* webpackChunkName: "auth" */ './views/Logout.vue'),
    },
    {
      path: '/employee',
      name: 'employee',
      component: () => import(/* webpackChunkName: "employee" */ './views/EmployeeHome.vue'),
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/register',
      name: 'register',
      component: () => import(/* webpackChunkName: "employee" */ './views/Register.vue'),
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/packages',
      name: 'customerPackage',
      component: () => import (/* webpackChunkName: "customer" */ './views/customer/CustomerPackage.vue'),
    },
    {
      path: '/tickets',
      name: 'customerTicket',
      component: () => import (/* webpackChunkName: "customer" */ './views/customer/CustomerTicket.vue'),
    },
    {
      path: '/hotels',
      name: 'customerHotel',
      component: () => import (/* webpackChunkName: "customer" */ './views/customer/CustomerHotel.vue'),
    },
    {
      path: '/inquiries',
      name: 'customerInquiries',
      component: () => import (/* webpackChunkName: "customer" */ './views/customer/CustomerInquiries.vue'),
    },
  ],
});
