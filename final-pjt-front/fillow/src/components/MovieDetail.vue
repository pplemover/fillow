<template>
  <div>

    <!-- {{ selected_movie_id }} -->
    <!-- 기본 데이터들 -->
    <div v-if="detail_data">
      {{ detail_data }}
      {{ detail_data.movie_id}}
    </div>
    


    <button @click="goAdd">지역 추가</button>

    <!-- 지역 추가 폼 -->
    <div v-if="isCreate">
      <p>지명<input type="text" v-model="addLocationData.location_name"></p>
      <p>경도<input type="text" v-model="addLocationData.latitude"></p>
      <p>위도<input type="text" v-model="addLocationData.longitude"></p>
      <p>국가<input type="text" v-model="addLocationData.location_country"></p>
      <p>영화장면 유튜브 URL<input type="text" v-model="addLocationData.youtube_url"></p>
      <p>지역 사진 URL<input type="text" v-model="addLocationData.location_photo_url"></p>
      <p>지역 설명<input type="text" v-model="addLocationData.location_description"></p> 
      <button @click="createMovieLocation(detail_data.movie_id)">수정 완료</button>
    </div>


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'MovieDetail',
  computed:{
    // selected_movie_id(){
    //   // const cur_id = this.$store.getters.selectedmovie
    //   this.getMovieDetail(this.$store.getters.selectedmovie)
    //   return this.$store.getters.selectedmovie
    // }
  },
  props:{
    detail_data:Object,
  },
  methods:{
    // getMovieDetail(thisid){
    //   // const cur_id = this.selected_movie_id
    //   axios({
    //     methods:'get',
    //     url:`http://127.0.0.1:8000/api/v1/movie/${thisid}/`,
    //   })
    //   .then((res)=>{
    //     this.detail_data = res.data
    //   })
    //   .catch((err)=>{
    //     console.log(err);
    //   })
    // },
    goAdd(){
      this.isCreate = !this.isCreate
    },
    createMovieLocation(movie_id){
      console.log(movie_id);
      this.addLocationData.tmdb_id = movie_id
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
      backdrop_path: '{{}}',
      isCreate:false,
      addLocationData:{
        tmdb_id:               null,
        location_name:         null,
        latitude:              null,
        longitude:             null,
        location_country:      null,
        youtube_url:           null,
        location_photo_url:    null,
        location_description:  null,
      },
    }
  },

}
</script>

<style>

</style>