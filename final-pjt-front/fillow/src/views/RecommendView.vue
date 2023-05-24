<template>
  <div>

    <h1>recommendview</h1>
    <div v-for="(recommend_item, index) in my_recommend_lst" :key="index">
      <RecommendItem
      :item="recommend_item"
      />
      <hr>
    </div>
    <!-- <RecommendItem/> -->


  </div>
</template>

<script>
import RecommendItem from "@/components/RecommendItem.vue";

export default {
  name:'RecommendView',
  created(){
    // this.$store.dispatch('getMovieLocations')
    // 타이밍 때문에 시간 걸어줌
    setTimeout(() => {
      this.calculate()
    }, 100);
  },
  components:{
    RecommendItem,
  },
  data(){
    return{
      my_recommend_lst : null,
    }
  },
  methods:{
    // 거리 계산 ================================================================================================
    calculate(){
      // 필요 함수 ==================================
      var rad = function(x) {
        return x * Math.PI / 180;
      };

      var getDistance = function(p1, p2) {
        var R = 6378137; // Earth’s mean radius in meter
        var dLat = rad(p2.latitude - p1.lat);
        var dLong = rad(p2.longitude - p1.lng);
        var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
          Math.cos(rad(p1.lat)) * Math.cos(rad(p2.latitude)) *
          Math.sin(dLong / 2) * Math.sin(dLong / 2);
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        var d = R * c;
        return d; // returns the distance in meter
      };
      // 필요 함수 ==================================
      const lst = this.$store.getters.currentLocations
      const position = this.$store.state.my_location
      const calculate_lst = []
      // console.log(position.lng);
      // console.log(position.lat);
      for (const item of lst) {
        const newdata = {
          data:item,
          distance_from_me : getDistance(position, item)
        }
        calculate_lst.push(newdata)
      }
      const newlst = calculate_lst.sort(function(a, b){
        return a.distance_from_me - b.distance_from_me
      })

      // 동일한 객체 넣지 않는 함수
      function pushUniqueObject(list, object) {
        const isDuplicate = list.some((cur) => {
          // Check for equality based on specific properties
          return cur.data.tmdb_id === object.data.tmdb_id
        });

        if (!isDuplicate) {
          list.push(object);
          console.log(object.data.tmdb_id);
        }
      }

      pushUniqueObject
      const recommend_lst = []
      for (const item of newlst) {
        if (recommend_lst.length < 3 ) {
          // recommend_lst.push(item)
          pushUniqueObject(recommend_lst, item)
        }
      }
      this.my_recommend_lst = recommend_lst
    },
    // 거리 계산 ================================================================================================

  }
}
</script>

<style>

</style>