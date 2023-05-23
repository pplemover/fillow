import Vue from 'vue'
import VueRouter from 'vue-router'

import MyMapView from '@/views/MyMapView'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import RecommendView from '@/views/RecommendView'
import AddMovieView from '@/views/AddMovieView'
import ChangePasswordView from '@/views/ChangePasswordView'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'mapView',
  //   component: MapView
  // },
  {
    path: '/RecommendView',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/ChangePasswordView',
    name: 'ChangePasswordView',
    component: ChangePasswordView
  },
  {
    path: '/AddMovieView',
    name: 'AddMovieView',
    component: AddMovieView
  },
  {
    path: '/',
    name: 'MyMapView',
    component: MyMapView,
    meta: {
      ogTitle: 'Fillow, Find Famous Film Locations',
      ogDescription: '내가 좋아하는 영화가 촬영된 장소로 떠나봐요~!',
      ogImage: require('@/assets/images/ogimage.jpg'),
      ogUrl: 'https://starbucks.co.kr',
    },
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
    meta: {
      ogTitle: 'Fillow, Find Famous Film Locations',
      ogDescription: '로그인 페이지',
      ogImage: require('@/assets/images/ogimage.jpg'),
      ogUrl: 'https://starbucks.co.kr',
    },
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
    meta: {
      ogTitle: 'Fillow, Find Famous Film Locations',
      ogDescription: '회원가입 페이지',
      ogImage: require('@/assets/images/ogimage.jpg'),
      ogUrl: 'https://starbucks.co.kr',
    },
  },
  // 404 띄울 곳
  // {
  //   path: '*',
  //   name: '*',
  //   component: MyMapView
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
