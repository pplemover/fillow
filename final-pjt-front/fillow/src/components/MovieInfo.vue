<template>
  <div class="about">
    <div style="height: 30%;">
      <MovieVideo />
    </div>
    <div style="height: 70%;">
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