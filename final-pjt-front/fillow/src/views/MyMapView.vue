<template>
  <div>

    <div class="d-flex">
      <MovieList class="col-3" style="overflow-x: hidden; height: 855px;"/>
      <MovieInfo class="col-3" style="overflow-x: hidden; height: 855px;"/>
      <MapView class="col-6"/>
    </div>
    <button>asdfasdfsdf</button>

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

}
</script>

<style>

</style>