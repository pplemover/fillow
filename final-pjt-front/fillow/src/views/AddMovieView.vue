<template>
  <div @keyup.enter="CheckMovie">

    <h1 style="margin-top: 61px;">addmovie</h1>
    <input type="text" v-model="query"><button @click="CheckMovie">확인</button>

    <div v-if="search_reslult">
      {{ search_reslult }}
      <br>
      <button @click="addMovietoDB(search_reslult.id)">영화 추가!</button>
    </div>
    

  </div>
</template>

<script>
import axios from 'axios';
const TMDB_API_KEY = '6aee34be99bb1d1b3fa358b709332b7e'

export default {
  name:'AddMovieView',
  data(){
    return{
      query: null,
      search_reslult:null,
    }
  },
  methods:{
    CheckMovie(){
      this.search_reslult = null
      axios({
        method:'get',
        url:`https://api.themoviedb.org/3/search/movie`,
        params:{
          api_key:TMDB_API_KEY,
          query:this.query,
          language:'ko',
        },
      })
      .then((res)=>{
        // console.log(res.data.results);
        if (res.data.results) {
          this.search_reslult = res.data.results[0]
        } else{
          alert('제대로 입력해')
        }
        this.query = null
      })
      .catch((err)=>{
        console.log(err);
      })
    },
    addMovietoDB(movie_id){
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/api/v1/movies/?id=${movie_id}`
      })
      .then((res)=>{
        console.log(res);
      })
      .catch((err)=>{
        console.log(err);
      })

    }
  }
}
</script>

<style>

</style>