<template>
  <div class="video_video" v-if="detail_data">
      <div class="video_ratio">
          <iframe width="100%" height="100%" :src="detail_data.movielocation_set[0].youtube_url"
              title="YouTube video player" 
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen>
          </iframe>
      </div>

  </div>
</template>

<script>
export default {
  name:'MovieVideo',
  props:{
    detail_data:Object,
  }
}
</script>

<style>
.video_video {
  background-color: black;
  position: relative;
}
.video_ratio {
  position: fixed;
  width: 600px;
  height: 350px;
  padding: 15px auto;
  margin: 7px;
}
</style>