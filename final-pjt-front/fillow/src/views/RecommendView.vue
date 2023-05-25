<template>
  <div class="recommend_bg">
    <div class="recommend_container">
      <!-- 첫 화면의 요소 (showInitialContent 데이터 속성을 사용하여 초기 컨텐츠 표시하거나 숨기기)-->
      <div class="black-box"></div>
      <div v-if="showInitialContent" @click="toggleContent" class="recommend__front"> 
        <div class="recommend_loader">
          <span></span>
        </div>
        <div class="recommend_select">
          <h1>내 위치를 기반으로 추천받기</h1>
          <span>당신의 위치 기준으로 가장 가까운 3개의 촬영지와 그 영화들을 추천합니다.</span>
          <span></span>
        </div>
      </div>

      <!-- 진짜 보여줄 내용 -->
      <div v-if="!showInitialContent" class="recommend__back"> 
        <div class="black-box"></div>
        <div v-for="(recommend_item, index) in my_recommend_lst" :key="index">
          <RecommendItem
          :item="recommend_item"
          />
          <hr>
        </div>
      </div>

    </div>

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
      showInitialContent: true,
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
    
    // 클릭 이벤트 발생 시 'showInitialContent'를 false로 설정하여 초기 컨텐츠를 숨김.
    toggleContent() {
      this.showInitialContent = false;
    }
    // 
  }
}
</script>

<style>
.recommend_bg {
  background-color: #1f1f1f;
  min-height: 100vh; 
  display: flex;
  justify-content: center;
  align-items: center;
}

.recommend_container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.recommend_select {
  color: white;
  font-family: 'Black Han Sans', sans-serif;
  cursor: pointer;
}

.recommend_loader {
  position: relative;
  width: 200px;
  height: 200px;
  background: transparent;
  border-radius: 50%;
  box-shadow: 25px 25px 75px rgba(0,0,0,0.55);
  border: 1px solid #333;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  margin: 50px auto;
}

.recommend_loader::before {
  content: '';
  position: absolute;
  inset: 20px;
  background: transparent;
  border: 1px dashed#444;
  border-radius: 50%;
  box-shadow: inset -5px -5px 25px rgba(0,0,0,0.25),
  inset 5px 5px 35px rgba(0,0,0,0.25);
}

.recommend_loader::after {
  content: '';
  position: absolute;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 1px dashed#444;
  box-shadow: inset -5px -5px 25px rgba(0,0,0,0.25),
  inset 5px 5px 35px rgba(0,0,0,0.25);
}

.recommend_loader span {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 50%;
  height: 100%;
  background: transparent;
  transform-origin: top left;
  animation: radar81 2s linear infinite;
  border-top: 1px dashed #fff;
}

.recommend_loader span::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: seagreen;
  transform-origin: top left;
  transform: rotate(-55deg);
  filter: blur(30px) drop-shadow(20px 20px 20px seagreen);
}

@keyframes radar81 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>