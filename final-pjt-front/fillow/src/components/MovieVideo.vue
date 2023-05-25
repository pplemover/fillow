<template>
  <div class="video_wrapper" v-if="detail_data">
    <!-- <div class="video_box" v-if="detail_data.movielocation_set.length !== 0"> -->
    <div class="video_box" v-if="detail_data.movielocation_set.length !== 0">
      <div class="video_ratio">
        <iframe width="100%" height="100%" :src="detail_data.movielocation_set[0].youtube_url"
          title="YouTube video player" 
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen>
        </iframe>
      </div>
    </div>
    <div class="video_ratio" v-else>
      <!-- 미리 지정한 동영상 링크를 사용 -->
        <iframe width="100%" height="100%" src="https://www.youtube.com/embed/RK1RRVR9A2g"
          title="Default video" frameborder="0"
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
  },
  // data(){
  //   return {
  //     detail_data: null
  //   }
  // },
  methods: {
    // YouTube 동영상 URL에서 VIDEO_ID를 추출하여 올바른 YouTube 임베드 URL을 생성
    // getYouTubeEmbedUrl(url) {
    //   const videoId = this.getYouTubeVideoId(url);
    //   return `https://www.youtube.com/embed/${videoId}`;
    // },
    // getYouTubeVideoId(url) {
    //   const regex = /(?:https?:\/\/(?:www\.)?youtube\.com\/(?:watch\?v=|embed\/)|https?:\/\/youtu\.be\/)([^\s&]+)/;
    //   const match = url.match(regex);
    //   if (match && match[1]) {
    //     return match[1];
    //   }
    //   return "";
    // }
  }
}
</script>

<style>
.video_wrapper {
  background-color: black;
  position: relative;
}
.video_ratio {
  width: 100%;
  height: 350px;
  padding: 2px 5px;
}
</style>