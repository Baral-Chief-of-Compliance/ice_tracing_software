<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left d-flex">История маршрута</div>

        <v-btn  variant="outlined" class="mx-10" :to="{name: 'RouteInfo', params: {id_rt: this.$route.params.id_rt }}">
            <v-icon icon="mdi-arrow-collapse-left" color="purple-darken-4" class="mr-2"></v-icon>назад
        </v-btn>

        {{ this.start_latitude }}
        {{ this.start_longitude }}

        {{ this.end_latitude }}
        {{ this.end_longitude }}

        <div class="d-flex ml-4">
                <div class="map">
                    <yandex-map
                        :coords="[start_latitude, start_longitude]"
                        :zoom="4"
                    >
                        
                        <ymap-marker v-for="(route, index) in routes" :key="index"
                            :marker-id="index"
                            marker-type="Polyline"
                            :coords="route.polyline"
                            :marker-stroke="{ color: '#000000', width: 2, opacity: 1, style: 'shortdash'}"
                        />

                        <ymap-marker 
                            :coords="[start_latitude, start_longitude]" 
                            :marker-id="5000"
                            :icon="{ color: 'blue' }"
                        />

                        <ymap-marker 
                            :coords="[end_latitude, end_longitude]" 
                            :marker-id="5001" 
                            :icon="{ color: 'red' }"
                        />

                        <ymap-marker v-if="this.status === 'в процессе' ? true:false "
                            :coords="[final_point_latitude, final_point_longitude]"
                            :marker-id="5003"
                            :icon="{ color: 'green' }"
                        />


                        <ymap-marker v-for="(point, index) in points" :key="index"
                            :marker-id="index + 6000"
                            :icon="{ color: 'black' }"
                            :coords="[point.point_latitude, point.point_longitude]"
                        />


                    </yandex-map>

                </div>

        </div>
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

            date_end: ""
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
    width: 1400px;
    height: 600px;
}

</style>