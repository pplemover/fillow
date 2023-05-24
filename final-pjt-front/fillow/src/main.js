import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import "bootstrap";
import"bootstrap/dist/css/bootstrap.min.css"
import '@mdi/font/css/materialdesignicons.css'
import VueStarRating from 'vue-star-rating';

import * as VueGoogleMaps from "vue2-google-maps" // Import package

import '@/styles/global.css' // scrollbar customizing css


Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: `${process.env.VUE_APP_GOOGLE_MAP_API_KEY}`,
    libraries: "places",
    region: "KR" 
  }
});

Vue.use(VueStarRating);


// movieitem.original_language 변수의 값에 따라 영어, 인도어, 이탈리어 또는 "알 수 없는 언어"를 출력
Vue.filter('languageFilter', function(value) {
  const languageMapping = {
    en: '영어', 
    hi: '인도어',
    it: '이탈리어',
    es: '스페인어',
    er: '프랑스어',
    il: '히브리어',
    kr: '한국어',
    pl: '폴란드어',
    ja: '일본어',
    tr: '터키어',
  }

  if (value in languageMapping) {
    return languageMapping[value];
  } else {
    return '알 수 없는 언어';
  }
  // 주어진 언어 코드에 대한 변환된 언어를 반환한다.

})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
