<template>
  <div>

    <div v-if="movie">
      {{movie}}
      <hr>
      <p>distance {{item.distance_from_me}}</p>
      <p>location id {{item.data.id}}</p>
    </div>


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'RecommendItem',
  props:{
    item:Object,
  },
  data(){
    return{
      movie:null,
    }
  },
  methods:{
    getMovie(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movie/${this.item.data.tmdb_id}/`
      })
      .then((res)=>{
        console.log(res);
        this.movie = res.data
      })
      .catch((err)=>{
        console.log(err);
      })
    },
  },
  created(){
    this.getMovie()
  }
}
</script>

<style>

</style>