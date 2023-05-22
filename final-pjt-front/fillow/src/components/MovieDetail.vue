<template>
  <div>

    
    <h1>Detail</h1>
    {{ selected_movie_id }}
    
    {{ detail_data }}
    <button @click="goAdd">지역 추가</button>

    <!-- 지역 추가 폼 -->
    <div v-if="isCreate">
      <p>지역 이름:<input type="text" v-model="addLocationData.location_name"></p>
      <p>경?도:<input type="text" v-model="addLocationData.latitude"></p>
      <p>위?도:<input type="text" v-model="addLocationData.longitude"></p>
      <p>나라<input type="text" v-model="addLocationData.location_country"></p>
      <p>유튜브 주소<input type="text" v-model="addLocationData.youtube_url"></p>
      <p>사진 주소<input type="text" v-model="addLocationData.location_photo_url"></p>
      <p>지역 설명<input type="text" v-model="addLocationData.location_description"></p> 
      <button @click="createMovieLocation">수정 완료</button>
    </div>


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
    },
    goAdd(){
      this.isCreate = true
    },
    createMovieLocation(){
      axios({
        method:'post',
        headers:`Token ${this.$store.state.token}`,
        url:`http://127.0.0.1:8000/api/v1/location/`,
        data: this.addLocationData
      })
      .then((res)=>{
        console.log(res);
      })
      .catch((err)=>{
        console.log(err);
        alert('폼을 정확히 입력해 주세요')
      })
      .finally(()=>{
        this.isCreate = false
        this.$store.dispatch('getMovieLocations')
      })
    },
  },
  data(){
    return{
      detail_data : null,
      isCreate:false,
      addLocationData:{
        tmdb_id:               this.$store.getters.selectedmovie,
        location_name:         null,
        latitude:              null,
        longitude:             null,
        location_country:      null,
        youtube_url:           null,
        location_photo_url:    null,
        location_description:  null,
      }
    }
  },

}
</script>

<style>

</style>