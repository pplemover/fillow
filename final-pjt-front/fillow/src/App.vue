<template>
  <div id="app" class="inner">
    <header>
      <!-- 로고 -->
      <a href="/" class="logo">
        <img src="/assets/images/header_fillow.png" alt="logo" />
      </a>

      <!-- 네비게이션 -->
      <router-link to="/">Map</router-link>
      
      <!-- 인증 관련 -->
      <div class="user" v-if="!isLogin">
        <router-link :to="{name:'LoginView'}">LoginView</router-link>|
        <router-link :to="{name:'SignUpView'}">SignUpView</router-link>|
      </div>
      <div v-if="isLogin" @click="logout">logout</div>
      <!-- 인증 관련 -->
    </header>


    <router-view/>

  </div>
</template>

<script>
// import MapView from '@/views/MapView.vue'
// import MovieInfo from '@/components/MovieInfo.vue'
// import MovieList from '@/components/MovieList.vue'

export default {
  name: 'App',
  components: {
    // MapView,
    // MovieList,
    // MovieInfo,
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovieLocations()
  },
  methods: {
    getMovieLocations() {
      // console.log(this.$store.state.movieLocations.length)
      if (!this.$store.state.movieLocations.length){
        // console.log('데이터 불러오기')
        this.$store.dispatch('getMovieLocations')
      }
    },
    logout(){
      if (this.$store.state.token) {
        const token = JSON.parse(localStorage.vuex)
        this.$store.dispatch('logout', token.token)
      }
    },
  },  
}
</script>

<style>
#inner {
  margin: 0 auto;
  width: 800px;
}

#app {
  font-family: 'Poppins', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

header {
  background-color: #528265;
}

.user {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  margin: 10px;
  padding: 30px;
  border-radius: 10px;
  height: 15px;
}

.user a {
  font-weight: bold;
  color: #2c3e50;
  top: 0; /* 상단에 위치하도록 함 */
  right: 0; /* 우측에 위치하도록 함 */
}

.user a.router-link-exact-active {
  color: #42b983;
  font-weight: bold;
  color: #2c3e50;
  top: 0; /* 상단에 위치하도록 함 */
  right: 0; /* 우측에 위치하도록 함 */
}
</style>
