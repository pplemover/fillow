<template>
  <div>

    <!-- 기본 보여주는 폼 -->
    <div v-if="!isUpdating" class="info_card">
      <img :src="movieLocationItem.location_photo_url" alt="" width="200px" height="150px">
      <div>
        {{movieLocationItem}}
        <button @click="goUpdate">수정</button>
      </div>
    </div>

    <!-- 업데이트 할떄 -->
    <div v-if="isUpdating">
      <p>지명:<input type="text" v-model="updatingData.location_name"></p>
      <p>경도:<input type="text" v-model="updatingData.longitude"></p>
      <p>위도:<input type="text" v-model="updatingData.latitude"></p>
      <p>국가<input type="text" v-model="updatingData.location_country"></p>
      <p>영화장면 유튜브 URL<input type="text" v-model="updatingData.youtube_url"></p>
      <p>지역 사진 URL<input type="text" v-model="updatingData.location_photo_url"></p>
      <p>지역 설명<input type="text" v-model="updatingData.location_description"></p> 
      <button @click="updateMovieLocation">수정 완료</button>
    </div>


  </div>
</template>

<script>
import axios from 'axios'


export default {
  name:'InfoWindow',
  props: {
    movieLocationItem: Object,
  },
  data(){
    return{
      isUpdating:false,
      updatingData:{
        tmdb_id:               this.movieLocationItem.tmdb_id,
        location_name:         this.movieLocationItem.location_name,
        latitude:              this.movieLocationItem.latitude,
        longitude:             this.movieLocationItem.longitude,
        location_country:      this.movieLocationItem.location_country,
        youtube_url:           this.movieLocationItem.youtube_url,
        location_photo_url:    this.movieLocationItem.location_photo_url,
        location_description:  this.movieLocationItem.location_description,
      }
    }
  },
  methods:{
    goUpdate(){
      this.isUpdating = true
    },
    updateMovieLocation(){
      this.updatingData.user = this.$store.state.user_detail.pk
      axios({
        method:'put',
        headers:`Token ${this.$store.state.token}`,
        url:`http://127.0.0.1:8000/api/v1/updatelocation/${this.movieLocationItem.id}/`,
        data: this.updatingData
      })
      .then((res)=>{
        console.log(res);
        this.isUpdating = false
        this.$store.dispatch('getMovieLocations')
        this.$emit('updatecomplete')
      })
      .catch((err)=>{
        console.log(err);
      })
      .finally(()=>{
      })
    }
  }
}
</script>

<style>
.info_card {
  position: relative;
  font-family: 'Black Han Sans', sans-serif;
  padding: 0px;
  background-color: #282828;
  color: white;
  
  display: flex;
}
</style>