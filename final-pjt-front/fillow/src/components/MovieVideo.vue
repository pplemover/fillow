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
  /* position: fixed; */
  background-color: black;
}
.video_ratio {
  width: 640px;
  height: 400px;
  padding: 2px 5px;
}
</style>