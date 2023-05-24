<template>
  <div>

    <div class="item-box" @click="selectThisItem">

        <div class="movie_info_container">
          <div class="movie_title">{{movieitem.title}}</div>
          <div class="movie_release_year">{{movieitem.release_date.slice(0, 4)}}</div>

          <div class="movie_tagline">{{movieitem.tagline}}</div>

          <span v-for="index in 5" :key="index" :class="{'filled': index <= rating}" @click="setRating(index)">&#9733;</span>
          <div class="tmdb_score smlet">({{((movieitem.vote_avg)/2).toFixed(1)}})</div>

          <div class="smlet">{{movieitem.original_language | languageFilter }}</div>
          <!-- movieitem.original_language 변수를 languageFilter 필터를 통해 변환한 결과를 출력 -->
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
    },
    setRating(index) {
      this.rating = index;
    }
  },
  data() {
    return {
      rating: (this.movieitem.vote_avg) / 2
    }
  },
}
</script>

<style>
.item-box {
  position: relative;
  width: 100%;
  border-bottom: 0.1px solid grey;
  padding: 10px;

  line-height: 30px;
  text-align: left;
  color: #78797a;

  border-radius: 2px;
  cursor: pointer;

  display: flex;
  justify-content: space-between;
  align-items: center;
}
.item-box:hover {
  background-color: #f8f4f4;
}

.movie_title {
  font-size: 20px;
  font-weight: 600;
  color: black;
}
.movie_title, .movie_release_year, .tmdb_score {
  display: inline-block;
  margin-right: 8px;
}
.movie_tagline {
  font-size: 14px;
  font-weight: 200;
}
.smlet {
  font-size: 13px;
  margin-left: 1px;
  margin-right: 1px;
}

.movie_poster_container {
  /* position: absolute; */
  right: 5px;
}
.movie_poster {
  border-radius: 5px;
  width: 85px;
  background-size: cover;
}

.filled {
  color: gold; 
}
</style>