<template>
  <div>

    <div class="black-box"></div>
    
    <gmap-map
    :zoom="5"
    :center="center"
    style="width:100%;  height: 100%;"
    @click="getCoordinate"
    ref="map"
    >

    <div
    v-for="m in locationMarkers"
    :key="m.id"
    >
      <gmap-marker
      v-if="$store.getters.selectedmovie === m.data.tmdb_id"
      :position="m.position"
      @click="openMarker(m.id)"
      >
        <gmap-info-window
        :closeclick="true"
        @closeclick="openMarker(null)"
        @keyup.esc="openMarker(null)"
        :opened="openedMarkerID === m.id"
        :options="{ disableAutoPan: true }"
        >
        
          <InfoWindowVue
          @updatecomplete="infoWindoUpdateComplete"
          :movie-location-item="m.data"
          />
          
        </gmap-info-window>
      </gmap-marker>
    </div>


    </gmap-map>
  </div>
</template>

<script>
// InfoWindow 수정중...............................................
import InfoWindowVue from '@/components/InfoWindow.vue';
import { mapState } from "vuex";

export default {
  name: "MapView",
  // InfoWindow 수정중...............................................
  components:{
    InfoWindowVue,
  },
  methods:{
    infoWindoUpdateComplete(){
      this.$emit('infoWindoUpdateComplete')
    },
    moveTo(data){
      console.log('move to activate');
      const targetCoordinates = {
        lat:parseFloat(data.lat),
        lng:parseFloat(data.lng),
      }
      const targetzoom = 5

      // Access the map instance and pan to the new coordinates
      const map = this.$refs.map.$mapPromise;
      map.then((mapInstance) => {
        mapInstance.setZoom(targetzoom);
        mapInstance.panTo(targetCoordinates);
      });

      // Update the center and zoom values for smooth transition
      // this.center = targetCoordinates;
    },
    openMarker(id) {
      console.log(id);
      this.openedMarkerID = id
    },
    getCoordinate(event){
      console.log(event.latLng.lat());
      console.log(event.latLng.lng());
    },
  },
  // InfoWindow 수정중...............................................
  data() {
    return {
      openedMarkerID: null,
      center: { lat: 37.5642135, lng: 127.0016985 },
      locPlaces: [],
      existingPlace: null
    };
  },
  watch:{
    moveto(data){
      // console.log('move');
      this.moveTo(data)
    }
  },
  computed: {
    ...mapState(['moveto']),
    locationMarkers() {
      const MovieLocations = this.$store.getters.currentLocations
      // console.log(MovieLocations)
      // console.log(MovieLocations[0].latitude)

      let latlngs = [] 

      for (const MovieLocation of MovieLocations) {
        // console.log('MovieLocation', MovieLocation)
        latlngs.push({
          position: { lat: parseFloat(MovieLocation.latitude) ,lng: parseFloat(MovieLocation.longitude) },
          id : MovieLocation.id,
          data:MovieLocation,
          })
      }
      
      return latlngs
    }
  },
  created() {
    console.log(this.locationMarkers)
  }
};
</script>

<style scoped>

</style>