<template>
  <div>

    <div class="black-box"></div>
    <!-- selected movie id 가 없으면 데이터 변경 제대로 반영 안됨 -->
    <div v-show="false">{{ selected_movie_id }}</div>
    
    <div class="MovieInfo">
      <div class="MovieVideo">
          <MovieVideo :detail_data="detail_data"/>
      </div>
      <div class="MovieDetail">
          <MovieDetail :detail_data="detail_data" 
          @createData = "createLocationData"/>
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
  props:{
    infowindow_changed:Boolean,
  },
  watch:{
    // 변경 감지되면 get 실행함
    infowindow_changed(){
      this.getMovieDetail(this.$store.getters.selectedmovie)
      console.log(1234);
    },
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
    createLocationData(){
      this.getMovieDetail(this.$store.getters.selectedmovie)
    },
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
  position: relative;
}
.MovieDetail {
  margin-top: 0px;
}
</style>