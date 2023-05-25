<template>
  <div>
    <div class="flex-box">
      <MovieList class="left" style="overflow-x: hidden; height: 100vh;"/>
      <MovieInfo class="mid" 
      style="overflow-x: hidden; height: 100vh;"
      :infowindow_changed="infowindow_changed"
      />
      <MapView class="right" 
      @infoWindoUpdateComplete="infoWindoUpdateComplete"
      style="overflow-y: hidden; height: 100vh;"
      />
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
    infoWindoUpdateComplete(){
      this.infowindow_changed = !this.infowindow_changed
    },
  },
  data(){
    return{
      infowindow_changed:false,
    }
  }
}
</script>

<style>
/* MovieListView, MovieInfoView, MapView */
.flex-box {
  display: flex;
  flex-wrap: wrap;
}
.left {
  flex-basis: 25%;
}
.mid {
  flex-basis: 33.33%;
  background-color: #1f1f1f;
}
.right {
  flex-basis: 41.67%;
}

@media (max-width: 900.98px) {
  .left,
  .mid,
  .right {
    flex-basis: 100%;
  }

  .left {
    height: 10vh;
    order: 1;
  }

  .mid {
    height: 80vh;
    order: 2;
  }

  .right {
    height: 10vh;
    order: 3;
  }
}
</style>