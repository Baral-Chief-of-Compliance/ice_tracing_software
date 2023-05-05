<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Сгенирировать ледовую обстановку</div>

        <div class="map">
            <yandex-map
                :coords="[68.970360, 33.074172]"
                :zoom="3"
                :cluster-options="clusterOptions"
            >
                <ymap-marker v-for="(polygon, index) in fast_ice" :key="index"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#fffafa'}"
                ></ymap-marker>

                <ymap-marker v-for="(polygon, index) in ice_field" :key="index"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#b9b1b1'}"
                ></ymap-marker>

                <ymap-marker v-for="(polygon, index) in nilas_ice" :key="index"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#0968f5'}"
                ></ymap-marker>

                <ymap-marker v-for="(polygon, index) in young_ice" :key="index"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#f708f9'}"
                ></ymap-marker>

                <ymap-marker v-for="(polygon, index) in first_year_ice" :key="index"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#00c8a1'}"
                ></ymap-marker>

                <ymap-marker v-for="(polygon, index) in old_ice" :key="index"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#900001'}"
                ></ymap-marker>

                <ymap-marker v-for="(port, index) in ports" :key="index"
                    :marker-id="index"
                    cluster-name="1"
                    :coords="[port.latitude, port.longitude]"
                    :markerFill="{color: '#900001'}"
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
            fast_ice: [],
            ice_field: [],
            nilas_ice: [],
            young_ice: [],
            first_year_ice: [],
            old_ice: [],
            ports: [],

            clusterOptions: {
        1: {
            clusterDisableClickZoom: true,
            clusterOpenBalloonOnClick: true,
            preset: 'islands#redClusterIcons',
            clusterBalloonLayout: [
            '<ul class=list>',
            '{% for geoObject in properties.geoObjects %}',
            '<li><a href=# class="list_item">{{ geoObject.properties.balloonContentHeader|raw }}</a></li>',
            '{% endfor %}',
            '</ul>',
            ].join(''),
        },
        },
        }
    },
    methods: {
        get_fast_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/fast_ice')
            .then(response => this.fast_ice = response.data.polygons)
        },

        get_ice_field(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/ice_field')
            .then(response => this.ice_field = response.data.polygons) 
        },

        get_nilas_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/nilas_ice')
            .then(response => this.nilas_ice = response.data.polygons) 
        },
        get_young_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/young_ice')
            .then(response => this.young_ice = response.data.polygons)
        },

        get_first_year_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/first_year_ice')
            .then(response => this.first_year_ice = response.data.polygons)
        },

        get_old_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/old_ice')
            .then(response => this.old_ice = response.data.polygons)
        },

        get_all_ports(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/ports')
            .then(response => this.ports = response.data.ports)
        }
    },
    mounted(){
        this.get_fast_ice()
        this.get_ice_field()
        this.get_nilas_ice()
        this.get_young_ice()
        this.get_first_year_ice()
        this.get_old_ice()
        this.get_all_ports()
    }
}
</script>

<style scoped>
.ymap-container {
    width: 1770px;
    height: 800px;
}
</style>