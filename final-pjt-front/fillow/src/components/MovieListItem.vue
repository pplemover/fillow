<template>
  <div>

    <div class="item-box" @click="selectThisItem">
      <div>
        <!-- 영화제목 -->
        <div class="movie_title">{{movieitem.title}}</div>
        <!-- Tagline -->
        <div class="movie_tagline">{{movieitem.tagline}}</div>
        <!-- TMDB Score · 개봉년월일 · 언어 -->
        <div class="movie_bitinfo">{{movieitem.vote_avg}} · {{ movieitem.release_date }} · {{ movieitem.original_language }}</div>
      </div>

      <div class="movie_poster_container">
        <!-- 영화 포스터 -->
        <img :src="`https://image.tmdb.org/t/p/original/${movieitem.poster_path}`" alt="" class="movie_poster">
      </div>
    </div>

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
  position: relative;
  width: 100%;
  height: 140px;
  border-bottom: 0.5px solid black;
  padding: 10px;

  line-height: 30px;
  text-align: left;
  color: #78797a;

  background-color: white;
  border-radius: 2px;
  cursor: pointer;

  display: flex;
  align-items: space-between;
}

.movie_title {
  font-size: 20px;
  font-weight: 600;
  color: black;
}
.movie_tagline {
  font-size: 14px;
  font-weight: 100;
}

.movie_poster_container {
  position: absolute;
  right: 5px;
}
.movie_poster {
  border-radius: 5px;
  width: 80px;
  background-size: cover;
}
</style>