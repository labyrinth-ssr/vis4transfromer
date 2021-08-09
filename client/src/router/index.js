import Vue from 'vue'
import VueRouter from 'vue-router'
import Ping from '../components/ping.vue';
import Books from '../components/Books.vue';
import HelloWorld from '../components/HelloWorld.vue';
import AttrTree from '../components/AttrTree.vue'

Vue.use(VueRouter)

// const routes = [
//   {
//     path: '/',
//     name: 'Home',
//     component: Home
//   },
//   {
//     path: '/about',
//     name: 'About',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
//   }
// ]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/helloWorld',
      name: 'helloWorld',
      component: HelloWorld,
    },
    {
      path: '/attrTree',
      name: 'attrTree',
      component: AttrTree,
    }
  ],
})

export default router
