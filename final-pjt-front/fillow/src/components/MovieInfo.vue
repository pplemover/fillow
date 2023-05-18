<template>
  <div class="about">
    <div style="height: 50%;">
      <MovieVideo />
    </div>
    <div style="height: 50%;">
      <MovieDetail/>
    </div>
  </div>
</template>

<script>
import MovieDetail from '@/components/MovieDetail.vue'
import MovieVideo from '@/components/MovieVideo.vue'

export default {
  name: "MovieInfo",
  components: {
    MovieDetail,
    MovieVideo,
  }
}
</script>

<style>
.about {
  background-color: black;
}
</style>