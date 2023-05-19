<template>
  <div id="app">
    <header>
      <!-- 로고 -->

      <!-- 네비게이션 -->
      <router-link to="/">Map</router-link>
      
      <!-- 회원가입 -->
      <div class="user">
        <router-link :to="{name:'LoginView'}">LoginView</router-link>|
        <router-link :to="{name:'SignUpView'}">SignUpView</router-link>|
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
