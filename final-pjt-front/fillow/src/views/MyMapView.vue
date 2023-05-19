<template>
  <div>

    <div class="d-flex">
      <MovieList class="col-2"/>
      <MovieInfo class="col-2"/>
      <MapView class="col-8"/>
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

}
</script>

<style>

</style>