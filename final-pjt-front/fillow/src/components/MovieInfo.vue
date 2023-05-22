<template>
  <div>
    <!-- 아래 이거 없으면 데이터 변경 제대로 반영 안됨 -->
    <div v-show="false">{{ selected_movie_id }}</div>
    
    <div class="MovieVideo">
      <MovieVideo :detail_data="detail_data"/>
      <div class="MovieDetail">
        <MovieDetail :detail_data="detail_data"/>
    </div>
    </div>

    

  </div>
</template>

<script>
import axios from 'axios'
import MovieDetail from '@/components/MovieDetail.vue'
import MovieVideo from '@/components/MovieVideo.vue'

export default {
  name: "MovieInfo",
  components: {
    MovieDetail,
    MovieVideo,
  },
  created(){
    this.getMovieDetail(this.$store.getters.selectedmovie)
  },
  computed:{
    selected_movie_id(){
      // const cur_id = this.$store.getters.selectedmovie
      this.getMovieDetail(this.$store.getters.selectedmovie)
      return this.$store.getters.selectedmovie
    }
  },
  methods:{
    getMovieDetail(thisid){
      // const cur_id = this.selected_movie_id
      axios({
        methods:'get',
        url:`http://127.0.0.1:8000/api/v1/movie/${thisid}/`,
      })
      .then((res)=>{
        this.detail_data = res.data
      })
      .catch((err)=>{
        console.log(err);
      })
    },
  },
  data(){
    return{
      detail_data:null,
    }
  }
}
</script>

<style>
.MovieVideo {
  position: fixed;
}
.MovieDetail {
  position: relative;
  top: 5px;
}
</style>