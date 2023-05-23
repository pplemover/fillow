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
  margin-top: 60px;
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
  .mid {
    flex-basis: auto; /* 유연한 너비로 설정하여 감소하지 않도록 유지 */
    max-width: none; /* 최대 너비 제한 해제 */
    display: block; /* 블록 레벨 요소로 변경 */
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