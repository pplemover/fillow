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
/* .card {
  color: #036635;
  background-color: whitesmoke;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 250px;
  height: 300px;
  margin: 5px;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3), 
              0 0 5px rgba(0, 0, 0, 0.3), 
              0 0 15px rgba(0, 0, 0, 0.3), 
              0 0 20px rgba(0, 0, 0, 0.3);
} */
</style>