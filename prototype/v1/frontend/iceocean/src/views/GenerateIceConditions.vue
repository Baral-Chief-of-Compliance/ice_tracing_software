<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Сгенирировать ледовую обстановку</div>

        <div class="map">
            <yandex-map
                :coords="[68.970360, 33.074172]"
                :zoom="3"
            >
                <ymap-marker v-for="(polygon, index) in polygons" :key="index"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    markerFill="red"
                ></ymap-marker>

                </yandex-map>

        </div>
    </v-container>

</template>

<script>
import axios from 'axios'

export default{
    data(){
        return{
            polygons: []
        }
    },
    methods: {
        get_young_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/young_ice')
            .then(response => this.polygons = response.data.polygons)
        }
    },
    mounted(){
        this.get_young_ice()
    }
}
</script>

<style scoped>
.ymap-container {
    width: 1770px;
    height: 800px;
}
</style>