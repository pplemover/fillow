<template>
  <div class="video_wrapper">
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
.video_wrapper {
  position: relative;
  background-color: black;
  height: 100%;
  width: 100%;
}

.video_box {
  position: absolute;
  height: 600px;
  width: 100%;
}
.video_ratio {
  padding: 2px 5px;
  margin: 4px 10px;
}
</style>