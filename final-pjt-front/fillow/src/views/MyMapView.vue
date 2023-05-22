<template>
  <div>
    <div class="flex-box">
      <MovieList class="left" style="overflow-x: hidden; height: calc(100vh - 94px);"/>
      <MovieInfo class="mid" style="overflow-x: hidden; height: calc(100vh - 94px);"/>
      <MapView class="right"/>
    </div>

  </div>
</template>

<script>
import MapView from '@/views/MapView.vue'
import MovieInfo from '@/components/MovieInfo.vue'
import MovieList from '@/components/MovieList.vue'


export default {
  name:'MyMapView',
  components: {
    MapView,
    MovieList,
    MovieInfo,
  },
  methods:{

  },

}
</script>

<style>
/* MovieListView, MovieInfoView, MapView */
.flex-box {
  display: flex;
  margin-top: 61px;
}
.left {
  flex-basis: 25%;
}
.mid {
  flex-basis: 33.33%;
}
.right {
  flex-basis: 41.67%;
}

@media (max-width: 767.98px) {
  .left {
    display: none;
  }
  .col-md-6 {
    flex-basis: 100%;
    max-width: 100%;
    display: none;
  }
  .right {
    display: none;
  }
}
</style>