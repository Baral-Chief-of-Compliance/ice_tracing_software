<template>

    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Информация о маршруте "{{ this.name }}"</div>
        <div class="text-h5 mx-10 mb-3"><b>Название судна: </b>{{ this.ship_name }}</div>
        <div class="text-h5 mx-10 mb-3"><b>Ледовый класс судна: </b>{{ this.ice_class }}</div>
        <v-container v-if="stage === 0">
            <div class="text-h5 mx-10 mb-5">1 ШАГ: Вы достигли следущего пункта маршрута?(<v-icon class="mt-1" color="green" icon="mdi-map-marker"></v-icon>)
                <v-dialog
                    v-model="dialog_yes"
                    width="auto"
                >  
                    <template v-slot:activator="{ props }">
                        <v-btn v-bind="props" color="purple-darken-4" class="px-10">да</v-btn>
                    </template>

                    <v-card>
                        <v-card-title>
                            Выберите дату достижения маршрута
                        </v-card-title>
                        <v-card-text>
                            <v-text-field type="date" v-model="date_enter">

                            </v-text-field>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn color="red" @click="dialog_yes = false">Закрыть</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn color="green" @click="dialog_yes = update_point()">Достигнут</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </div>

            <div class="d-flex ml-4">
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
                        marker-id="2" 
                        :icon="{ color: 'red' }"
                    />

                    <ymap-marker
                        :coords="[final_point_latitude, final_point_longitude]"
                        marker-id="3"
                        :icon="{ color: 'green' }"
                    />

                    <ymap-marker v-for="(point, index) in points" :key="index + 100"
                        :marker-id="index"
                        :icon="{ color: 'black' }"
                        :coords="[point.point_latitude, point.point_longitude]"
                    />

                    <ymap-marker v-for="(route, index) in routes" :key="index + 200"
                        :marker-id="index"
                        marker-type="Polyline"
                        :coords="route.polyline"
                        :marker-stroke="{ color: '#000000', width: 2, opacity: 1, style: 'shortdash'}"
                        />

                    </yandex-map>
                </div>
                
                <div class="ml-5">
                    <v-card class="text-h6 px-5 py-2 d-flex"><v-icon class="mt-1" color="blue" icon="mdi-map-marker"/><b class="mr-1">Начало пути:</b>{{ this.date_start }}</v-card>
                    <v-card v-for="(point, index) in points" :key="index" class="text-h6 px-5 py-2 my-2 d-flex"><v-icon class="mt-1" color="black" icon="mdi-map-marker"/><b class="mr-1">Промежуток:</b>{{ this.format_date(point.date) }}</v-card>
                </div>
            </div>
        </v-container>

        <v-container v-if="stage === 1">
            <div class="text-h5 mx-10 mb-5">2 ШАГ: Настройки для построения маршрута</div>

            <div class="d-flex ml-10">
                <div class="map">
                    <yandex-map
                        :coords="[final_point_latitude, final_point_longitude]"
                        :zoom="4"
                    >

                        <ymap-marker 
                            :coords="[start_latitude, start_longitude]" 
                            marker-id="1" 
                        />

                        <ymap-marker 
                            :coords="[end_latitude, end_longitude]" 
                            marker-id="2" 
                            :icon="{ color: 'red' }"
                        />

                        <ymap-marker 
                            :coords="[final_point_latitude, final_point_longitude]" 
                            marker-id="3" 
                            :icon="{ color: 'green' }"
                        />

                        <ymap-marker v-for="(point, index) in points" :key="index + 100"
                            :marker-id="index"
                            :icon="{ color: 'black' }"
                            :coords="[point.point_latitude, point.point_longitude]"
                        />

                        <ymap-marker v-for="(route, index) in routes" :key="index + 200"
                            :marker-id="index"
                            marker-type="Polyline"
                            :coords="route.polyline"
                            :marker-stroke="{ color: '#000000', width: 2, opacity: 1, style: 'shortdash'}"
                        />

                        <ymap-marker 
                            :coords="[this.polygon]" 
                            marker-id="500"
                            marker-type="Polygon" 
                            :markerFill="{color: '#4A148C', opacity: 0.7}"
                            :marker-stroke="{color: '#4A148C', opacity: 1}"
                        />



            
                    </yandex-map>
                </div>

                <v-form class="ml-10">
                    <div class="d-flex justify-center pt-7">
                        <span class="text-h6">Радиус зоны для построения маршрута:</span>
                    </div>

                    <div class="d-flex justify-center pt-7">
                        <span class="text-h6">Левая сторона квадрата:</span>
                    </div>

                    <v-slider
                        v-model="lenght_left_side"
                        class="align-center"
                        :max="max"
                        :min="min"
                        hide-details
                        color="purple-darken-4"
                    >
                        <template v-slot:prepend>
                        <v-btn
                            size="small"
                            variant="text"
                            icon="mdi-minus"
                            color="purple-darken-4"
                            @click="decrement_left_side"
                        ></v-btn>
                        </template>
                        <template v-slot:append>
                            <v-btn
                                size="small"
                                variant="text"
                                icon="mdi-plus"
                                color="purple-darken-4"
                                @click="increment_left_side"
                            ></v-btn>
                        </template>
                    </v-slider>

                    <div class="d-flex justify-center pt-7">
                        <span class="text-h6">Правая сторона квадрата:</span>
                    </div>

                    <v-slider
                        v-model="lenght_right_side"
                        class="align-center"
                        :max="max"
                        :min="min"
                        hide-details
                        color="purple-darken-4"
                    >
                        <template v-slot:prepend>
                        <v-btn
                            size="small"
                            variant="text"
                            icon="mdi-minus"
                            color="purple-darken-4"
                            @click="decrement_right_side"
                        ></v-btn>
                        </template>
                        <template v-slot:append>
                            <v-btn
                                size="small"
                                variant="text"
                                icon="mdi-plus"
                                color="purple-darken-4"
                                @click="increment_right_side"
                            ></v-btn>
                        </template>
                    </v-slider>


                    <div class="d-flex justify-center pt-7">
                        <span class="text-h6">Верхняя сторона квадрата:</span>
                    </div>

                    <v-slider
                        v-model="width_top_side"
                        class="align-center"
                        :max="max"
                        :min="min"
                        hide-details
                        color="purple-darken-4"
                    >
                        <template v-slot:prepend>
                        <v-btn
                            size="small"
                            variant="text"
                            icon="mdi-minus"
                            color="purple-darken-4"
                            @click="decrement_width_top_side"
                        ></v-btn>
                        </template>
                        <template v-slot:append>
                            <v-btn
                                size="small"
                                variant="text"
                                icon="mdi-plus"
                                color="purple-darken-4"
                                @click="increment_width_top_side"
                            ></v-btn>
                        </template>
                    </v-slider>

                    <div class="d-flex justify-center pt-7">
                        <span class="text-h6">Нижняя сторона квадрата:</span>
                    </div>

                    <v-slider
                        v-model="width_bottom_side"
                        class="align-center"
                        :max="max"
                        :min="min"
                        hide-details
                        color="purple-darken-4"
                    >
                        <template v-slot:prepend>
                        <v-btn
                            size="small"
                            variant="text"
                            icon="mdi-minus"
                            color="purple-darken-4"
                            @click="decrement_width_bottom_side"
                        ></v-btn>
                        </template>
                        <template v-slot:append>
                            <v-btn
                                size="small"
                                variant="text"
                                icon="mdi-plus"
                                color="purple-darken-4"
                                @click="increment_width_bottom_side"
                            ></v-btn>
                        </template>
                    </v-slider>
                    
                </v-form>

            </div>

            <v-btn block class="mx-8 pa-5 mt-8 text-h6" color="purple-darken-4" @click="update_route()">
                Построить маршрут
            </v-btn>
        </v-container>
    </v-container>

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

        date_start: "",

        points: [],
        routes: [],

        final_point_longitude: "",
        final_point_latitude: "",

        dialog_yes: false,
        date_enter: "",
        stage: 0,

        min: 0,
        max: 20,
        lenght_left_side: 10,
        lenght_right_side: 10,
        width_top_side: 10,
        width_bottom_side: 10,

        polygon: []
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
                this.date_start = this.format_date(response.data.date_start),

                this.start_longitude = response.data.start_longitude,
                this.start_latitude = response.data.start_latitude,

                this.end_longitude = response.data.end_longitude,
                this.end_latitude = response.data.end_latitude,

                this.points = response.data.points,
                this.routes = response.data.routes,

                this.final_point_longitude = response.data.final_point_longitude,
                this.final_point_latitude = response.data.final_point_latitude
            ))
        },
        format_date(date){
                var d = new Date(date)

                var dd = d.getDate()
                if (dd < 10) dd = '0' + dd

                var mm = d.getMonth() + 1
                if (mm < 10) mm = '0' + mm

                var yy = d.getFullYear()

                return dd + '.' + mm + '.' + yy
        },

        update_point(){
            axios.put(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`, 
            {
                date_enter: this.date_enter  
            })

            axios.post("http://127.0.0.1:5000/iceocean/api/v1.0/generate_area", {
                start_longitude: this.final_point_longitude,
                start_latitude: this.final_point_latitude
            }).then(response => this.polygon = response.data.polygon)

            this.stage++
        },
        increment_left_side(){
            this.lenght_left_side++
            let right_top_area = this.polygon[0]
            let left_top_area = this.polygon[1]
            let left_bottom_area = this.polygon[2]
            let right_bottom_area = this.polygon[3]

            this.polygon = [
                [right_top_area[0], right_top_area[1] - 1], left_top_area, left_bottom_area, [right_bottom_area[0], right_bottom_area[1] - 1], [right_top_area[0], right_top_area[1] - 1]
            ]        
        },
        decrement_left_side(){
            this.lenght_left_side--
            let right_top_area = this.polygon[0]
            let left_top_area = this.polygon[1]
            let left_bottom_area = this.polygon[2]
            let right_bottom_area = this.polygon[3]

            this.polygon = [
                [right_top_area[0], right_top_area[1] + 1], 
                left_top_area, 
                left_bottom_area, 
                [right_bottom_area[0], right_bottom_area[1] + 1], 
                [right_top_area[0], right_top_area[1] + 1]
            ]   
        },

        increment_right_side(){
            this.lenght_right_side++
            let right_top_area = this.polygon[0]
            let left_top_area = this.polygon[1]
            let left_bottom_area = this.polygon[2]
            let right_bottom_area = this.polygon[3]

            this.polygon = [
                right_top_area, 
                [left_top_area[0], left_top_area[1] + 1], 
                [left_bottom_area[0], left_bottom_area[1] + 1], 
                right_bottom_area, 
                right_top_area
            ]        
        },

        decrement_right_side(){
            this.lenght_right_side--
            let right_top_area = this.polygon[0]
            let left_top_area = this.polygon[1]
            let left_bottom_area = this.polygon[2]
            let right_bottom_area = this.polygon[3]

            this.polygon = [
                right_top_area, 
                [left_top_area[0], left_top_area[1] - 1], 
                [left_bottom_area[0], left_bottom_area[1] - 1], 
                right_bottom_area, 
                right_top_area
            ]        
        },

        decrement_width_top_side(){
            this.width_top_side--
            let right_top_area = this.polygon[0]
            let left_top_area = this.polygon[1]
            let left_bottom_area = this.polygon[2]
            let right_bottom_area = this.polygon[3]

            this.polygon = [
                [right_top_area[0] - 1,  right_top_area[1]], 
                [left_top_area[0] - 1, left_top_area[1]], 
                left_bottom_area, 
                right_bottom_area, 
                [right_top_area[0] - 1,  right_top_area[1]]
            ]   
        },

        increment_width_top_side(){
            this.width_top_side++
            let right_top_area = this.polygon[0]
            let left_top_area = this.polygon[1]
            let left_bottom_area = this.polygon[2]
            let right_bottom_area = this.polygon[3]

            this.polygon = [
                [right_top_area[0] + 1,  right_top_area[1]], 
                [left_top_area[0] + 1, left_top_area[1]], 
                left_bottom_area, 
                right_bottom_area, 
                [right_top_area[0] + 1,  right_top_area[1]]
            ]   
        },


        decrement_width_bottom_side(){
            this.width_bottom_side--
            let right_top_area = this.polygon[0]
            let left_top_area = this.polygon[1]
            let left_bottom_area = this.polygon[2]
            let right_bottom_area = this.polygon[3]

            this.polygon = [
                right_top_area, 
                left_top_area, 
                [left_bottom_area[0] + 1, left_bottom_area[1]],
                [right_bottom_area[0] + 1, right_bottom_area[1]], 
                right_top_area
            ]   
        },

        increment_width_bottom_side(){
            this.width_bottom_side++
            let right_top_area = this.polygon[0]
            let left_top_area = this.polygon[1]
            let left_bottom_area = this.polygon[2]
            let right_bottom_area = this.polygon[3]

            this.polygon = [
                right_top_area, 
                left_top_area, 
                [left_bottom_area[0] - 1, left_bottom_area[1]],
                [right_bottom_area[0] - 1, right_bottom_area[1]], 
                right_top_area
            ]  
        },

        update_route(){
            axios.post(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`,
            {
                final_point_longitude: this.final_point_longitude,
                final_point_latitude: this.final_point_latitude,

                end_longitude: this.end_longitude,
                end_latitude: this.end_latitude,

                iceclass: this.ice_class,
                area_building_route: this.polygon
            }
            )

            this.$router.push({ name: 'Routes'})
        }
    }
}
</script>

<style scoped>
.ymap-container {
    width: 1400px;
    height: 600px;
}

</style>