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
      <div @click="calculate" class="recommend_btn">내 위치를 기반으로 추천받기</div>
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
    // 내 위치 알아내기=========================================================================
    console.log(navigator.geolocation.getCurrentPosition(success, error));
    let payload = {
      lat:null,
      lng:null,
    }
    function success(pos) {
      var crd = pos.coords;
      
      console.log('Your current position is:');
      console.log(`Latitude : ${crd.latitude}`);
      console.log(`Longitude: ${crd.longitude}`);
      console.log(`More or less ${crd.accuracy} meters.`);
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
    // 거리 계산 ================================================================================================
    calculate(){
      // 필요 함수 ==================================
      var rad = function(x) {
        return x * Math.PI / 180;
      };

      var getDistance = function(p1, p2) {
        var R = 6378137; // Earth’s mean radius in meter
        var dLat = rad(p2.latitude - p1.lat);
        var dLong = rad(p2.longitude - p1.lng);
        var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
          Math.cos(rad(p1.lat)) * Math.cos(rad(p2.latitude)) *
          Math.sin(dLong / 2) * Math.sin(dLong / 2);
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        var d = R * c;
        return d; // returns the distance in meter
      };
      // 필요 함수 ==================================
      const lst = this.$store.getters.currentLocations
      const position = this.$store.state.my_location
      const calculate_lst = []
      console.log(position.lng);
      console.log(position.lat);
      for (const item of lst) {
        const newdata = {
          data:item,
          distance_from_me : getDistance(position, item)
        }
        calculate_lst.push(newdata)
      }
      const newlst = calculate_lst.sort(function(a, b){
        return a.distance_from_me - b.distance_from_me
      })

      console.log(newlst);

      const recommend_lst = []
      for (const item of newlst) {
        recommend_lst
        item
      }
      
    },
    // 거리 계산 ================================================================================================
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
  font-family: 'Black Han Sans', sans-serif;
  font-weight: 400;
  cursor: pointer;
}
.user_a:hover {
  color: lightgreen;
}

/* FILTER_BOX */
.filter-box {
  margin-top: 61px;
  height: 50px;
  background-color: white;
  display: flex;
}

.recommend_btn {
  width: 180px;
  height: 30px;
  margin: 7px 10px 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #528265;
  background-color: white;
  border-radius: 10px;

  font-family: 'Do Hyeon', sans-serif;
  font-size: 15px;
  color: #528265;
  font-weight: 100;
  cursor: pointer;
  transition: .3s;
}
.recommend_btn:hover {
  background-color: gold;
  color: #528265;
}
</style>
