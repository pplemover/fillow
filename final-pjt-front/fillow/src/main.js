import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import "bootstrap";
import"bootstrap/dist/css/bootstrap.min.css";

import * as VueGoogleMaps from "vue2-google-maps" // Import package

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: `${process.env.VUE_APP_GOOGLE_MAP_API_KEY}`,
    libraries: "places",
    region: "KR" 
  }
});

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
