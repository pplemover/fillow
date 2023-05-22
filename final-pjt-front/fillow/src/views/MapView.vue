<template>
  <div>
    <gmap-map
    :zoom="5"
    :center="center"
    style="width:100%;  height: 100%;"
    >

    <div
    :key="index"
    v-for="(m, index) in locationMarkers"
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
        >
        
          <InfoWindowVue
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

export default {
  name: "MapView",
  // InfoWindow 수정중...............................................
  components:{
    InfoWindowVue,
  },
  methods:{
    openMarker(id) {
      console.log(id);
      this.openedMarkerID = id
    }
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
  computed: {
    locationMarkers() {
      const MovieLocations = this.$store.getters.currentLocations
      console.log(MovieLocations)
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