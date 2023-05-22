<template>
  <div id="app">
    <!-- HEADER -->
    <header>
      <!-- 홈 화면 routing -->
      <router-link to="/">
        <a href="/" class="logo"><img src="@/assets/images/header_fillow.png" alt="logo" style="width: 100px; height: auto;"></a>
      </router-link>
      
      <!-- 인증 화면 routing -->
      <div class="user" v-if="!isLogin">
        <router-link :to="{name:'LoginView'}" class="user_a">
          로그인
        </router-link>
        <router-link :to="{name:'SignUpView'}" class="user_a">
          회원가입
        </router-link>
      </div>
      <div v-if="isLogin" @click="logout" class="user_a">
        로그아웃
      </div>
    </header>

    <div class="filter-box">
        test
    </div>
    
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
#app {
  font-family: 'Poppins', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  text-decoration: none;
}

/* HEADER */
header {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: #528265;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
  border-bottom: 1px solid #528265;
  z-index: 9;
}
.logo {
  position: relative;
  left: 15px;
}
.user {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  right: 15px;
}
.user_a {
  margin-right: 10px;
  font-size: 25px;
  text-decoration: none;
  color: white;
  font-family: 'Black Han Sans', sans-serif;
}
.user_a:hover {
  color: lightgreen;
}

/* FILTER_BOX */
.filter_box {
  position: fixed;
  top: 61px;
  height: 50px;
  width: 100%;
  background-color: white;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #528265;
  z-index: 9;
}
</style>
