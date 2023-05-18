<template>
  <div id="app">
    <nav>
      <router-link to="/">Map</router-link> |
      <!-- <router-link to="/about">About</router-link> -->
    </nav>
    <div class="d-flex">
      <div class="d-inline-block" style="width: 40%;">
        <MovieInfo style="height: 100%"/>
      </div>
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

export default {
  name: 'App',
  components: {
    // MapView,
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
