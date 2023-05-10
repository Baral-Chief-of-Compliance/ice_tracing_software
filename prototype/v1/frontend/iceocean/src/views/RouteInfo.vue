<template>
                    <div class="map">
                    <yandex-map
                        :coords="[start_latitude, start_longitude]"
                        :zoom="4"
                    >

                        <ymap-marker 
                            :coords="[start_latitude, start_longitude]" 
                            marker-id="1" 
                        />

                        <ymap-marker 
                            :coords="[end_latitude, end_longitude]" 
                            marker-id="3" 
                            :icon="{ color: 'red' }"
                        />

                        <ymap-marker v-for="(point, index) in points" :key="index"
                            :marker-id="index"
                            :icon="{ color: 'green' }"
                            :coords="[point.point_latitude, point.point_longitude]"
                         />

                         <ymap-marker 
                            :marker-id="index"
                            marker-type="Polyline"
                            :coords="[[71.33352, 168.66318], [71.00019, 168.99651], [70.66686, 169.32984], [70.66686, 169.66317000000004], [70.66686, 169.99650000000003]
, [70.66686, 170.32983000000002]]"
                         />

                         <!-- <ymap-marker v-if="!show_ports" v-for="(port, index) in ports" :key="index"
                            :marker-id="show_ports"
                            :balloon="{header: port.name }"
                            cluster-name="1"
                            :coords="[port.latitude, port.longitude]"
                            :icon="{ color: 'green' }"
                            @balloonopen="clik_baloon"
                            @balloonclose="clik_baloon"
                    ></ymap-marker> -->

            
                    </yandex-map>
                </div>

</template>

<script>
import axios from 'axios';


export default{
    data: () => ({
        name: "",
        ship_name: "",
        ice_class: "",

        start_longitude: "",
        start_latitude: "",

        end_longitude: "",
        end_latitude: "",

        points: [],
        routes: []
    }),

    mounted(){
        this.get_inf()
    },

    methods: {
        get_inf(){
            axios.get(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`)
            .then(response => (
                this.name = response.data.name,
                this.ship_name = response.data.ship_name,
                this.ice_class = response.data.ice_class,

                this.start_longitude = response.data.start_longitude,
                this.start_latitude = response.data.start_latitude,

                this.end_longitude = response.data.end_longitude,
                this.end_latitude = response.data.end_latitude,

                this.points = response.data.points,
                this.routes = response.data.routes
            ))
        }
    }
}
</script>

<style scoped>
.ymap-container {
    width: 1400px;
    height: 700px;
}

</style>