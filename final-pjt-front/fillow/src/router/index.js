import Vue from 'vue'
import VueRouter from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import MyMapView from '@/views/MyMapView'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'mapView',
  //   component: MapView
  // },
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
    path: '/',
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
    path: '/',
    name: 'SignUpView',
    component: SignUpView,
    meta: {
      ogTitle: 'Fillow, Find Famous Film Locations',
      ogDescription: '회원가입 페이지',
      ogImage: require('@/assets/images/ogimage.jpg'),
      ogUrl: 'https://starbucks.co.kr',
    },
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
