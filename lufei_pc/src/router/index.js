import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
//      name: 'HelloWorld',
//      component: HelloWorld
      name:'Home',
      component:Home,
    },
//    {
//      path:'/home',
//      name:'Home',
//      component:Home,
//    }
  ]
})
