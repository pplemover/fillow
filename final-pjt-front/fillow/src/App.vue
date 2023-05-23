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

    <footer>
      <ul class="menu">
        <li><a href="javascript:void(0)" class="green">개인정보처리방침</a></li>
        <li><a href="javascript:void(0)">위치정보 이용약관</a></li>
      </ul>

      <div class="info">
        <span>최종 프로젝트 [임휘진, 김동욱]</span>
        <span>개인정보 책임자 : 임휘진</span>
      </div>

      <p class="copyright">
        &copy; <span class="this-year"></span> Fillow. All Rights Reserved.
      </p>
      <img src="@/assets/images/header_fillow.png" alt="logo" class="logo" />
    </footer>

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
  height: 100%;
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
  border-top: 1px solid #032c16;
  border-bottom: 2px solid #032c16;
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

/* SIGN CARD */
.sign {
  position: relative;
  font-family: 'Do Hyeon', sans-serif;
  padding: 93px;
  background-image: url("https://source.unsplash.com/random/?movies");
  background-position: center;
  background-attachment: fixed;
  background-size: cover;
  margin-top: 60px;
}
.sign h1 {
  color: white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  font-size: 30px;
  font-weight: 400;
  text-align: left;
  margin-bottom: 10px;
}
.sign__card {
  width: 500px;
  left: 0;
  border-radius: 10px;
  background-color: #F6F5F0;
  box-shadow: 2px 2px 20px rgba(0, 0, 0, .3);
  color: #555;
}
.sign__card h2 {
  padding: 30px;
  font-size: 18px;
  text-align: center;
  border-bottom: 1px solid #ddd;
}

.sign__card h2 strong {
  font-weight: 400;
  color: #006633;
}

.sign__card form {
  padding: 30px 22px;
  margin-bottom: 25px;
}
.sign__card form input {
  width: 100%;
  margin-bottom: 12px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  outline: none;
  box-sizing: border-box;
  font-size: 14px;
}
.sign__card form [type="submit"] {
  background-color: #528265;
  border: none;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
}
.sign__card form p {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  color: grey;
  text-align: center;
}
.sign__card .actions {
  display: flex;
  border-top: 1px solid #ddd;
}
.sign__card .actions a {
  flex-grow: 1;
  flex-basis: 0;
  text-align: center;
  padding: 20px;
  color: #555;
  font-size: 14px;
  border-right: 1px solid #ddd; 
}
.sign__card .actions a:last-child {
  border-right: none;
}
.sign__card .actions a:hover {
  text-decoration: underline;
}

/*FOOTER*/
footer {
  position: fixed;
  width: 100%;
  background-color: #272727;
  border-top: 1px solid #032c16;
}
footer .menu {
  display: flex;
  justify-content: center;
}
footer .menu li {
  position: relative;
}
footer .menu li::before {
  content: "";
  width: 3px;
  height: 3px;
  background-color: #555;
  position: absolute;
  top: 0;
  bottom: 0;
  right: -1px;
  margin: auto;
}
footer .menu li:last-child::before {
  display: none;
}
footer .menu li a {
  display: block;
  color: #CCC;
  font-size: 12px;
  font-weight: 700;
  padding: 15px;
}
footer .menu li a.green {
  color: #528265;
}
footer .info {
  margin-top: 10px;
  text-align: center;
}
footer .info span {
  margin-right: 20px;
  color: #999;
  font-size: 12px;
}
footer .info span:last-child {
  margin-right: 0;
}
footer .copyright {
  color: #999;
  font-size: 12px;
  text-align: center;
  margin-top: 5px;
}
footer .logo {
  margin: 5px;
}
</style>
