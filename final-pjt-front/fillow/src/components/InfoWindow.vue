<template>
  <div>

    <!-- 기본 보여주는 폼 -->
    <div v-if="!isUpdating">
      <h1>infowindow</h1>
      {{movieLocationItem}}
      <img :src="movieLocationItem.location_photo_url" alt="" width="200px" height="150px">
      <button @click="goUpdate">수정</button>
    </div>

    <!-- 업데이트 할떄 -->
    <div v-if="isUpdating">
      <p>지역 이름:<input type="text" v-model="updatingData.location_name"></p>
      <p>경?도:<input type="text" v-model="updatingData.latitude"></p>
      <p>위?도:<input type="text" v-model="updatingData.longitude"></p>
      <p>나라<input type="text" v-model="updatingData.location_country"></p>
      <p>유튜브 주소<input type="text" v-model="updatingData.youtube_url"></p>
      <p>사진 주소<input type="text" v-model="updatingData.location_photo_url"></p>
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
      axios({
        method:'put',
        headers:`Token ${this.$store.state.token}`,
        url:`http://127.0.0.1:8000/api/v1/updatelocation/${this.movieLocationItem.id}/`,
        data: this.updatingData
      })
      .then((res)=>{
        console.log(res);
      })
      .catch((err)=>{
        console.log(err);
      })
      .finally(()=>{
        this.isUpdating = false
      })
    }
  }
}
</script>

<style>

</style>