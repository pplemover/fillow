<template>
  <div id="app">
    <nav>
      <router-link to="/">Map</router-link> |
      <router-link :to="{name:'LoginView'}">LoginView</router-link>|
      <router-link :to="{name:'SignUpView'}">SignUpView</router-link>|
      <!-- <router-link to="/about">About</router-link> -->
    </nav>
    <div class="d-flex">
      <MovieList/>
      <MovieInfo/>
      <div class="d-inline-block" style="width: 60%; height: 100%">
        <router-view/>
      </div>
    </div>
    

    <!-- <MapView/> -->
  </div>
</template>

<script>
// import MapView from '@/views/MapView.vue'
import MovieInfo from '@/components/MovieInfo.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'App',
  components: {
    // MapView,
    MovieList,
    MovieInfo,
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
