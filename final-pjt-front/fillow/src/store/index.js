import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

const DJANGO_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movieLocations: [

    ],

  },
  getters: {
  },
  mutations: {
    GET_MOVIE_LOCATIONS(state, movieLocations) {
      // console.log('이 왜 됨?')
      console.log('0번 내용', movieLocations[0])
      state.movieLocations = movieLocations
    }
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
    }
  },
  modules: {
  }
})
