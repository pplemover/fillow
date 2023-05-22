<template>
  <div class="video_box" v-if="detail_data">
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
.video_box {
  background-color: black;
  position: relative;
  height: 350px; /* 동영상의 높이에 맞춰 조정 */
}
.video_ratio {
  position: relative;
  width: 500px;
  height: 350px;
  padding: 15px auto;
  margin: 7px;
}
</style>