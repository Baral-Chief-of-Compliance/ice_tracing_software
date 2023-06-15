<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left d-flex">История ледовой обстановки маршрута</div>

        <v-btn  variant="outlined" class="mx-10" :to="{name: 'RouteInfo', params: {id_rt: this.$route.params.id_rt }}">
            <v-icon icon="mdi-arrow-collapse-left" color="purple-darken-4" class="mr-2"></v-icon>назад
        </v-btn>

        <v-container>
            <div class="d-flex ml-4">
                    <div class="map">
                        <yandex-map
                            :coords="[start_latitude, start_longitude]"
                            :controls="['zoomControl', 'typeSelector']"
                            :zoom="4"
                        >   

                            <ymap-marker v-for="(polygon, index) in fast_ice" :key="index"
                                :marker-id="index"
                                marker-type="Polygon"
                                :coords="[polygon]"
                                :markerFill="{color: '#fffafa', opacity: 0.5}"
                                :marker-stroke="{color: '#fffafa', opacity: 1}"
                            ></ymap-marker>

                            <ymap-marker v-for="(polygon, index) in ice_field" :key="index"
                                :marker-id="index + 100000"
                                marker-type="Polygon"
                                :coords="[polygon]"
                                :markerFill="{color: '#b9b1b1', opacity: 0.5}"
                                :marker-stroke="{color: '#b9b1b1', opacity: 1}"
                            ></ymap-marker>

                            <ymap-marker v-for="(polygon, index) in nilas_ice" :key="index"
                                :marker-id="index + 200000"
                                marker-type="Polygon"
                                :coords="[polygon]"
                                :markerFill="{color: '#0968f5', opacity: 0.5}"
                                :marker-stroke="{color: '#0968f5', opacity: 1}"
                            ></ymap-marker>

                            <ymap-marker v-for="(polygon, index) in young_ice" :key="index"
                                :marker-id="index + 300000"
                                marker-type="Polygon"
                                :coords="[polygon]"
                                :markerFill="{color: '#f708f9', opacity: 0.5}"
                                :marker-stroke="{color: '#f708f9', opacity: 1}"
                            ></ymap-marker>

                            <ymap-marker v-for="(polygon, index) in first_year_ice" :key="index"
                                :marker-id="index + 400000"
                                marker-type="Polygon"
                                :coords="[polygon]"
                                :markerFill="{color: '#00c8a1', opacity: 0.5}"
                                :marker-stroke="{color: '#00c8a1', opacity: 1}"
                            ></ymap-marker>

                            <ymap-marker v-for="(polygon, index) in old_ice" :key="index"
                                :marker-id="index + 500000"
                                marker-type="Polygon"
                                :coords="[polygon]"
                                :markerFill="{color: '#900001', opacity: 0.5}"
                                :marker-stroke="{color: '#900001', opacity: 1}"
                                suppressMapOpenBlock: true
                            ></ymap-marker> 
                            
                            <div v-for="(route, index) in routes" :key="index">
                                <ymap-marker 
                                    v-if="this.selected_route != route.id_itir"
                                    :marker-id="index + 600000"
                                    marker-type="Polyline"
                                    :coords="route.polyline"
                                    :marker-stroke="{ color: '#000000', width: 2, opacity: 1, style: 'shortdash'}"
                                />
                            </div>

                            <div v-for="(route, index) in routes" :key="index">
                                <ymap-marker 
                                    v-if="this.selected_route === route.id_itir"
                                    :marker-id="index + 700000"
                                    marker-type="Polyline"
                                    :coords="route.polyline"
                                    :marker-stroke="{ color: '#FFFF00', width: 2, opacity: 1, style: 'shortdash'}"
                                />
                            </div>


                            <ymap-marker 
                                :coords="[start_latitude, start_longitude]" 
                                :marker-id="1000000"
                                :icon="{ color: 'blue' }"
                            />

                            <ymap-marker 
                                :coords="[end_latitude, end_longitude]" 
                                :marker-id="1000001" 
                                :icon="{ color: 'red' }"
                            />

                            <ymap-marker v-if="this.status === 'в процессе' ? true:false "
                                :coords="[final_point_latitude, final_point_longitude]"
                                :marker-id="1000003"
                                :icon="{ color: 'green' }"
                            />


                            <ymap-marker v-for="(point, index) in points" :key="index"
                                :marker-id="index + 1100000"
                                :icon="{ color: 'black' }"
                                :coords="[point.point_latitude, point.point_longitude]"
                            />


                        </yandex-map>

                    </div>

            </div>

            <div class="text-h5 mx-10 mt-5"><b>Отобразить ледовую обстановку за маршрут: </b> </div>

            <v-row class="mt-3 mx-2" >
                <v-col v-for="(route, index) in routes" cols="2">                
                    <v-card
                        :color="this.selected_route === route.id_itir ? 'purple-darken-4': 'white'"
                        class="text-h6 px-5 py-2 mx-3"
                        @click="get_ice_condition_for_route(route.id_itir)"
                    >
                        маршрут {{ index + 1 }}
                    </v-card>
                </v-col>

            </v-row>

        </v-container>
    </v-container>
</template>

<script>
import axios from 'axios';
import { format_date } from '@/tools/views'


export default{
    data(){

        return {
            routes: [],
            name: "",
            ship_name: "",
            ice_class: "",

            date_start: "",
            start_longitude: 33.09251,
            start_latitude: 68.9791,

            end_longitude: "",
            end_latitude: "",

            final_point_longitude: "",
            final_point_latitude: "",

            points: [],

            status: "",

            date_end: "",
            
            selected_route: null,

            fast_ice: [],
            ice_field: [],
            nilas_ice: [],
            young_ice: [],
            first_year_ice: [],
            old_ice: []
        }


    },

    methods: {

        get_routes(){
            axios.get(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(respnose => this.routes = respnose.data.routes)
        },


        get_end_and_start(){
            axios.get(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(respnose => (
                
                this.start_latitude = respnose.data.start_latitude,
                this.start_longitude = respnose.data.start_longitude,

                this.end_latitude = respnose.data.end_latitude,
                this.end_longitude = respnose.data.end_longitude
            )) 
        },

        get_final_point(){
            axios.get(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(respnose => (
                this.status = respnose.data.status,
                this.final_point_latitude = respnose.data.final_point_latitude,
                this.final_point_longitude = respnose.data.final_point_longitude
            ))

        },

        get_points(){
            axios.get(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(respnose => (
                this.points = respnose.data.points

            ))   
        },

        get_ice_condition_for_route(id_itir){
            this.selected_route = id_itir
            this.fast_ice = []
            this.ice_field = []
            this.nilas_ice = []
            this.young_ice = []
            this.first_year_ice = []
            this.old_ice = []

            axios.get(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}/ice_conditions/${id_itir}`, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then( respnose => (
                this.fast_ice = respnose.data.fast_ice,
                this.ice_field = respnose.data.ice_field,
                this.nilas_ice = respnose.data.nilas_ice,
                this.young_ice = respnose.data.young_ice,
                this.first_year_ice = respnose.data.first_year_ice,
                this.old_ice = respnose.data.old_ice,
                this.routes = respnose.data.routes
                
            ))


            this.get_routes()

        }

    },

    mounted(){
        this.get_routes()
        this.get_end_and_start()
        this.get_points()
        this.get_final_point()
    },

    updated(){
        this.get_routes()
        this.get_end_and_start()
        this.get_points()
        this.get_final_point()
    },
}

</script>


<style scoped>
.ymap-container {
    width: 1700px;
    height: 600px;
}

</style>