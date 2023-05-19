import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from "vuex-persistedstate"

import router from '@/router'

Vue.use(Vuex)

const DJANGO_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movieLocations: [

    ],
    homemovieselect_id: 12,
    // 초기값 12 (스타워즈)
  },
  getters: {
  },
  mutations: {
    GET_MOVIE_LOCATIONS(state, movieLocations) {
      // console.log('이 왜 됨?')
      console.log('0번 내용', movieLocations[0])
      state.movieLocations = movieLocations
    },
    SELECT_THIS_ITEM(state, index){
      state.homemovieselect_id = index
    },

    // =============================인증 시스템 관련 =================================
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({name:'mapView'})  // store/index,js $ router 접근 불가 ->import 해야됨
    },
    DELETE_TOKEN(state){
      state.token = null
    },
    // =============================인증 시스템 관련 =================================
  },
  actions: {
    getMovieLocations(context) {
      // movieLocations이 없으면 load
      // console.log('이게 되네')
      axios({
        method: 'get',
        url: `${DJANGO_URL}/api/v1/movies/`,
      })
      .then((res) => {
        // console.log(res)
        
        context.commit('GET_MOVIE_LOCATIONS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    selectThisItem(context, index){
      // console.log(index,'store');
      context.commit('SELECT_THIS_ITEM', index)
    },

    // =============================인증 시스템 관련 =================================
    login(context, payload){
      const username = payload.username
      const password = payload.password

      axios({
        method:'post',
        url:`${DJANGO_URL}/accounts/login/`,
        data:{
          username, password
        }
      })
      .then((res)=>{
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err);
      })
    },
    logout(context, payload){
      axios({
        method:'post',
        url:`${DJANGO_URL}/accounts/logout/`,
        headers:{
          Authorization: `Token ${payload}`
        }
      })
      .then((res)=>{
        console.log(res);
        context.commit('DELETE_TOKEN')
      })
      .catch((err)=>{
        console.log(err);
      })
    },
    signUp(context, payload){
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method:'post',
        url:`${DJANGO_URL}/accounts/signup/`,
        data: {
          username: username,
          password1: password1,
          password2: password2,
        }
      })
      .then((res)=>{
        console.log(res);
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err);
      })
    },
    // =============================인증 시스템 관련 =================================
  },
  modules: {
  }
})
