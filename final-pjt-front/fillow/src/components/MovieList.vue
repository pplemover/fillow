<template>
  <div>
    <hr>
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

</style>