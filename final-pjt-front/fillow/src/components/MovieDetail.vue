<template>
  <div>

    
    <h1>Detail</h1>
    {{ selected_movie_id }}
    
    {{ detail_data }}


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'MovieDetail',
  computed:{
    selected_movie_id(){
      // const cur_id = this.$store.getters.selectedmovie
      this.getMovieDetail(this.$store.getters.selectedmovie)
      return this.$store.getters.selectedmovie
    }
  },
  // created() {
  //     const cur_id = this.$store.state.homemovieselect_id
  //     this.getMovieDetail(cur_id)
  //     return cur_id
    
  // },
  methods:{
    getMovieDetail(thisid){
      // const cur_id = this.selected_movie_id
      axios({
        methods:'get',
        url:`http://127.0.0.1:8000/api/v1/movie/${thisid}/`,
      })
      .then((res)=>{
        console.log(res.data);
        this.detail_data = res.data
      })
      .catch((err)=>{
        console.log(err);
      })
    }
  },
  data(){
    return{
      detail_data : null,
    }
  }

}
</script>

<style>

</style>