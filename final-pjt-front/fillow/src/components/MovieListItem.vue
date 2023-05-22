<template>
  <div>
    
    <!-- 개봉년월일 -->
    <!-- 장르, 상영시간 -->
    <!-- 촬영장소 -->
    <div class="item-box">
      <div @click="selectThisItem">
        <!-- 영화제목 -->
        <div>{{movieitem.title}}</div>
        <!-- Tagline -->
        <div>{{movieitem.tagline}}</div>
        <!-- TMDB Score · 개봉년월일 · 언어 -->
        <div>{{movieitem.vote_avg}}·{{ movieitem.release_date }}·{{ movieitem.original_language }}</div>
      </div>
      <div>
        <!-- 영화 포스터 -->
        <img :src="`https://image.tmdb.org/t/p/original/${movieitem.poster_path}`" alt="" width="100px" height="150px">
      </div>
    </div>
    <hr>

  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movieitem: Object,
  },
  methods: {
    selectThisItem(){
      // console.log(this.movieitem.movie_id);
      this.$store.dispatch('selectThisItem', this.movieitem.movie_id)
    } 
  }
}
</script>

<style>
.item-box {
  width: 100%;
  height: 140px;
  margin: 10px;
  line-height: 30px;
  text-align: center;

  background-color: green;

  display: flex;
  align-items: space-between;
}
</style>