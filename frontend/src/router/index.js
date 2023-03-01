import Vue from 'vue'
import Router from 'vue-router'
import Section from '@/components/Section'
import Login from '../components/Login.vue'
import Register from "../components/Register.vue";
import Topic from "../components/Topic.vue";
import PostListPage from "../components/PostListPage";
import createTopic from "../components/CreateTopic";
import SectionPostListPage from "../components/SectionPostListPage";
import User from "../components/User";
import UserTiezi from "../components/UserTiezi";
import UserReply from "../components/UserReply";
import UserCollect from "../components/UserCollect";
import AdminThreadMngr from "../components/AdminThreadMngr";
import AdminUserMngr from "../components/AdminUserMngr";
import AdminLogin from "../components/AdminLogin";


Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Section',
      component: Section
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    {
      path: '/topic',
      name: 'Topic',
      component: Topic
    },
    {
      path: '/PostListPage',
      name: 'PostListPage',
      component: PostListPage
    },
    {
      path: '/createTopic',
      name: 'createTopc',
      component: createTopic
    },
    {
      path: '/SectionPostListPage',
      name: '/SectionPostListPage',
      component: SectionPostListPage
    },
    {
      path: '/User',
      name: '/User',
      component: User
    },
    {
      path: '/UserTiezi',
      name: '/UserTiezi',
      component: UserTiezi
    },
    {
      path: '/UserReply',
      name: '/UserReply',
      component: UserReply
    },
    {
      path: '/UserCollect',
      name: '/UserCollect',
      component: UserCollect
    },
    {
      path: '/AdminThreadMngr',
      name: '/AdminThreadMngr',
      component: AdminThreadMngr
    },
    {
      path: '/AdminUserMngr',
      name: '/AdminUserMngr',
      component: AdminUserMngr
    },
    {
      path: '/AdminLogin',
      name: '/AdminLogin',
      component: AdminLogin
    }
  ]
})

router.beforeEach((to, from, next) => {//beforeEach是router的钩子函数，在进入路由前执行
  // if (to.meta.title) {//判断是否有标题
  //   document.title = to.meta.title
  // }
  document.title = 'BUAAHUB - 大学生交流论坛'
  next()//执行进入路由，如果不写就不会进入目标页
})

export default router
