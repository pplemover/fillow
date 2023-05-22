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
          <button class="log_btn">로그인</button>
        </router-link>

        <router-link :to="{name:'SignUpView'}" class="user_a">
          <button class="log_btn">회원가입</button>
        </router-link>
      </div>
      <div v-if="isLogin" @click="logout" class="user_a">
        <button class="log_btn">로그아웃</button>
      </div>
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
    // 내 위치 알아내기=========================================================================
    navigator.geolocation.getCurrentPosition(success, error);
    let payload = {
      lat:null,
      lng:null,
    }
    function success(pos) {
      var crd = pos.coords;
      
      // console.log('Your current position is:');
      // console.log(`Latitude : ${crd.latitude}`);
      // console.log(`Longitude: ${crd.longitude}`);
      // console.log(`More or less ${crd.accuracy} meters.`);
      payload.lat = crd.latitude
      payload.lng = crd.longitude
    }
    
    function error(err) {
      console.warn(`ERROR(${err.code}): ${err.message}`);
    }
    
    this.$store.dispatch('getMyLocation', payload)
    // 내 위치 알아내기=====================================================================
    
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
  font-family: 'Do Hyeon', sans-serif;
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
  height: 60px;
  background-color: #528265;
  display: flex;
  justify-content: space-between;
  align-items: center;
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
  font-family: 'Do Hyeon', sans-serif;
  font-weight: 400;
  cursor: pointer;
}
.user_a:hover {
  color: lightgreen;
}

.log_btn {
  --bg: #528265;
  --hover-bg: #0fca66;
  --hover-text: black;
  height: 100%;
  color: #fff;
  border: 1px solid var(--bg);
  border-radius: 4px;
  padding: 0.1em 0.2em;
  background: var(--bg);
  transition: 0.2s;
}

.log_btn:hover {
  color: var(--hover-text);
  transform: translate(-0.25rem,-0.25rem);
  background: var(--hover-bg);
  box-shadow: 0.25rem 0.25rem var(--bg);
}

.log_btn:active {
  transform: translate(0);
  box-shadow: none;
}
</style>
