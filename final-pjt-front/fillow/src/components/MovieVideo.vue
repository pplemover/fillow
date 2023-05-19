<template>
  <div class="video_video" style="height: 100%;">
      <div class="video_ratio" style="height: 100%;">
          <iframe width="100%" height="100%" src="https://www.youtube.com/embed/e9ys-ArvLmk"
              title="YouTube video player" frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen>
          </iframe>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.video_video {
  width: 100%;
}
.video_ratio {
  position: relative;
  height: 0;
  padding-top: 56.25%;
  margin: 5px;
}
</style>