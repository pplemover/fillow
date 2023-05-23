<template>
  <div>
    <div @click="goRecommend" class="recommend_btn">내 위치를 기반으로 추천받기</div>

    <MovieListItem
    v-for="homemovieitem in homemovielist"
    :key="homemovieitem.movie_id"
    :movieitem="homemovieitem"
    />
    <!-- v-for을 사용하여 MovieListItem 컴포넌트를 여러번 렌더링. -->
    <!-- movieitem를 사용하여 해당 요소를 MovieListItem 컴포넌트에 전달  -->
  </div>
</template>

<script>
import axios from 'axios';
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  created() {
    this.getMovieList()
  },
  methods:{
    getMovieList(){
      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/api/v1/movies/"
      })
      .then((res)=>{
        // console.log(res.data);
        this.homemovielist = res.data
      })
    },
    goRecommend(){
      this.$router.push({name:'RecommendView'})
    }
  },
  data(){
    return{
      homemovielist:null,
    }
  }
}
</script>

<style>
.recommend_btn {
  --bg: #3B9E83;
  --hover-bg: #0fca66;
  --hover-text: black;
  margin: 5px 10px 5px;
  height: 40px;
  color: #fff;
  border: 1px solid var(--bg);
  border-radius: 5px;
  padding: 0.5em 0.1em;
  background: var(--bg);
  transition: 0.1s;
}

.recommend_btn:hover {
  color: var(--hover-text);
  transform: translate(-0.25rem,-0.25rem);
  background: var(--hover-bg);
  box-shadow: 0.25rem 0.25rem var(--bg);
}

.recommend_btn:active {
  transform: translate(0);
  box-shadow: none;
}
</style>