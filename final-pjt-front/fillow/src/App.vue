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
        <router-link :to="{name:'LoginView'}">
          <button class="btn_custom btn_custom--darkgreen login">로그인</button>
        </router-link>
        <router-link :to="{name:'SignUpView'}">
          <button class="btn_custom btn_custom--darkgreen">회원가입</button>
        </router-link>
      </div>
      <div v-if="isLogin" @click="logout">로그아웃</div>
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
#app {
  font-family: 'Poppins', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  text-decoration: none;
}

header {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: #528265;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
  border-bottom: 1px solid #c8c8c8;
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

.login {
  margin-right: 5px;
}

router-view {
  margin-top: 61px;
}
</style>
