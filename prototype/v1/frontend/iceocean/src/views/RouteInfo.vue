<template>

    <v-container>
        <div class="text-h3 py-6 mx-10 text-left d-flex">Информация о маршруте "{{ this.name }}" <v-card :color=" this.status === 'в процессе' ? 'teal-accent-4' : (this.status === 'завершён' ? 'blue-grey':'orange-accent-4') " class="text-h4 ml-5 px-10 py-1">{{ this.status }}</v-card></div>
        <v-btn  variant="outlined" class="mx-10" :to="{name: 'Routes'}">
            <v-icon icon="mdi-arrow-collapse-left" color="purple-darken-4" class="mr-2"></v-icon>назад
        </v-btn>
        <div class="text-h5 mx-10 mb-3 mt-3"><b>Название судна: </b>{{ this.ship_name }}</div>
        <div class="text-h5 mx-10 mb-3"><b>Ледовый класс судна: </b>{{ this.ice_class }}</div>

        <v-container v-if="stage === 0">
            <div v-if="this.status === 'в процессе' ? true:false" class="text-h5 mx-10 mb-5">1 ШАГ: Вы достигли следущего пункта маршрута?(<v-icon class="mt-1" color="green" icon="mdi-map-marker"></v-icon>)
                
                <v-dialog
                    v-model="dialog_in_progress"
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
                            <v-btn color="red" @click="dialog_in_progress = false">Закрыть</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn color="green" @click="dialog_in_progress = update_point()">Достигнут</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </div>

            <div v-if="this.status === 'завершение' ? true:false" class="text-h5 mx-10 mb-5">1 ШАГ: Вы достигли конечного пункта маршрута?(<v-icon class="mt-1" color="red" icon="mdi-map-marker"></v-icon>)
                
                <v-dialog
                    v-model="dialog_completion"
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
                            <v-btn color="red" @click="dialog_completion = false">Закрыть</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn color="green" @click="update_status">Достигнут</v-btn>
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
                        :marker-id="1"
                    />

                    <ymap-marker 
                        :coords="[end_latitude, end_longitude]" 
                        :marker-id="2" 
                        :icon="{ color: 'red' }"
                    />

                    <ymap-marker v-if="this.status === 'в процессе' ? true:false "
                        :coords="[final_point_latitude, final_point_longitude]"
                        :marker-id="3"
                        :icon="{ color: 'green' }"
                    />

                    <ymap-marker v-for="(point, index) in points" :key="index"
                        :marker-id="index + 100"
                        :icon="{ color: 'black' }"
                        :coords="[point.point_latitude, point.point_longitude]"
                    />



                        <ymap-marker v-for="(polygon, index) in fast_ice" :key="index"
                            :marker-id="index + 100000"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#fffafa', opacity: 0.5}"
                            :marker-stroke="{color: '#fffafa', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in ice_field" :key="index"
                            :marker-id="index + 200000"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#b9b1b1', opacity: 0.5}"
                            :marker-stroke="{color: '#b9b1b1', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in nilas_ice" :key="index"
                            :marker-id="index + 300000"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#0968f5', opacity: 0.5}"
                            :marker-stroke="{color: '#0968f5', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in young_ice" :key="index"
                            :marker-id="index + 400000"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#f708f9', opacity: 0.5}"
                            :marker-stroke="{color: '#f708f9', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in first_year_ice" :key="index"
                            :marker-id="index + 500000"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#00c8a1', opacity: 0.7}"
                            :marker-stroke="{color: '#00c8a1', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in old_ice" :key="index"
                            :marker-id="index + 600000"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#900001', opacity: 0.7}"
                            :marker-stroke="{color: '#900001', opacity: 1}"
                            suppressMapOpenBlock: true
                        ></ymap-marker>

                        <div v-for="(route, index) in routes" :key="index">
                            <ymap-marker 
                            v-if="route.id_itir != this.select_route"
                            :marker-id="index + 1000000"
                            marker-type="Polyline"
                            :coords="route.polyline"
                            :marker-stroke="{ color: '#000000', width: 2, opacity: 1, style: 'shortdash'}"
                        />
                        </div>


                        <div v-for="(route, index) in routes" :key="index">
                            <ymap-marker 
                            v-if="route.id_itir === this.select_route"
                            :marker-id="index + 2000000"
                            marker-type="Polyline"
                            :coords="route.polyline"
                            :marker-stroke="{ color: '#FFFF00', width: 2, opacity: 1, style: 'shortdash'}"
                        />
                        </div>



                    </yandex-map>

                </div>

                <div class="ml-5">
                    <div class="text-h5 mb-3 mt-3"><b>Контрольные точки: </b></div>
                    <v-card class="text-h6 px-5 py-2 d-flex"><v-icon class="mt-1" color="blue" icon="mdi-map-marker"/><b class="mr-1">Начало пути:</b>{{ this.date_start }}</v-card>
                    <v-card v-for="(point, index) in points" :key="index" class="text-h6 px-5 py-2 my-2 d-flex"><v-icon class="mt-1" color="black" icon="mdi-map-marker"/><b class="mr-1">Промежуток:</b>{{ this.format_date(point.date) }}</v-card>
                    <v-card class="text-h6 px-5 py-2 my-2 d-flex"><v-icon class="mt-1" color="red" icon="mdi-map-marker"/><b class="mr-1">Конец пути:</b>{{ this.date_end }}</v-card>
                </div>
            </div>
            

            <div class="text-h5 mx-10 mt-5"><b>Отобразать ледовую обстановку, при которой был построен маршрут: </b> </div>
            <v-row class="mt-3 mx-2" >
                <v-col v-for="route in routes" cols="2">                
                    <v-card
                        color="purple-darken-4"
                        class="text-h6 px-5 py-2 mx-3"
                        @click="func_select_route(route, this.routes)" >
                        маршрут {{ route.id_itir }}
                    </v-card>
                </v-col>

            </v-row>

        </v-container>

        <v-container v-if="stage === 1">
            <div class="text-h5 mx-10 mb-5">2 ШАГ: Настройки для построения маршрута</div>

            <v-btn @click="update_ice_condition" class="mx-10 mb-5" color="purple-darken-4">Сгенирировать ледовую обстановку</v-btn>

            <div class="d-flex ml-10">
                <!-- <div class="map">
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



                        <ymap-marker 
                            :coords="[this.polygon]" 
                            marker-id="500"
                            marker-type="Polygon" 
                            :markerFill="{color: '#4A148C', opacity: 0.7}"
                            :marker-stroke="{color: '#4A148C', opacity: 1}"
                        />

                        <ymap-marker v-for="(polygon, index) in fast_ice" :key="index+1000"
                            :marker-id="index"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#fffafa', opacity: 0.5}"
                            :marker-stroke="{color: '#fffafa', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in ice_field" :key="index+2000"
                            :marker-id="index"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#b9b1b1', opacity: 0.5}"
                            :marker-stroke="{color: '#b9b1b1', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in nilas_ice" :key="index+3000"
                            :marker-id="index"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#0968f5', opacity: 0.5}"
                            :marker-stroke="{color: '#0968f5', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in young_ice" :key="index+4000"
                            :marker-id="index"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#f708f9', opacity: 0.5}"
                            :marker-stroke="{color: '#f708f9', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in first_year_ice" :key="index+5000"
                            :marker-id="index"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#00c8a1', opacity: 0.7}"
                            :marker-stroke="{color: '#00c8a1', opacity: 1}"
                        ></ymap-marker>

                        <ymap-marker v-for="(polygon, index) in old_ice" :key="index+6000"
                            :marker-id="index"
                            marker-type="Polygon"
                            :coords="[polygon]"
                            :markerFill="{color: '#900001', opacity: 0.7}"
                            :marker-stroke="{color: '#900001', opacity: 1}"
                            suppressMapOpenBlock: true
                        ></ymap-marker>

                        <ymap-marker v-for="(route, index) in routes" :key="index + 200"
                        :marker-id="index"
                        marker-type="Polyline"
                        :coords="route.polyline"
                        :marker-stroke="{ color: '#000000', width: 2, opacity: 1, style: 'shortdash'}"
                        />

                        <ymap-marker v-for="(route, index) in routes" :key="index + 200"
                            :marker-id="index"
                            marker-type="Polyline"
                            :coords="route.polyline"
                            :marker-stroke="{ color: '#000000', width: 2, opacity: 1, style: 'shortdash'}"
                        />



            
                    </yandex-map>
                </div> -->

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


    <v-dialog
        v-model="dialog_loading"
        width="auto"
        persistent
      >
        <v-card
            color="purple-darken-4"
        >
            <v-card-text>
            Пожалуйста, подождите
            <v-progress-linear
                indeterminate
                color="white"
                class="mb-0"
            ></v-progress-linear>
            </v-card-text>
        </v-card>
      </v-dialog>

</template>

<script>
import axios from 'axios';


export default{
    data: () => ({
        name: "",
        ship_name: "",
        ice_class: "",
        status: "",

        select_route: "",

        start_longitude: "",
        start_latitude: "",

        end_longitude: "",
        end_latitude: "",

        date_start: "",

        points: [],
        routes: [],

        final_point_longitude: "",
        final_point_latitude: "",

        dialog_in_progress: false,
        dialog_completion: false,
        date_enter: "",
        stage: 0,
        dialog_loading: false,

        min: 0,
        max: 20,
        lenght_left_side: 10,
        lenght_right_side: 10,
        width_top_side: 10,
        width_bottom_side: 10,

        polygon: [],

        fast_ice: [],
        ice_field: [],
        nilas_ice: [],
        young_ice: [],
        first_year_ice: [],
        old_ice: [],
        date_end: ""
    }),

    created(){
        axios.interceptors.request.use( (config)=>{
            this.dialog_loading = true
            return config
        }),

        axios.interceptors.response.use((response) =>{
            this.dialog_loading = false

            // if (response.config.method == 'get'){
            //     this.get_inf()
            //     this.get_fast_ice()
            //     this.get_ice_field()
            //     this.get_nilas_ice()
            //     this.get_young_ice()
            //     this.get_first_year_ice()
            //     this.get_old_ice()
            // }
            if (response.config.method == 'post' && response.config.url == `http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`){
                this.$router.go(0)
            }
            return response
        })
    },

    mounted(){
        this.get_inf()
        this.get_fast_ice()
        this.get_ice_field()
        this.get_nilas_ice()
        this.get_young_ice()
        this.get_first_year_ice()
        this.get_old_ice()
    },

    // updated(){
    //     this.get_inf()
    //     this.get_fast_ice()
    //     this.get_ice_field()
    //     this.get_nilas_ice()
    //     this.get_young_ice()
    //     this.get_first_year_ice()
    //     this.get_old_ice()
    // },

    beforeMount(){

    },

    methods: {
        get_fast_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/fast_ice', {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => this.fast_ice = response.data.polygons)
        },

        get_ice_field(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/ice_field', {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => this.ice_field = response.data.polygons) 
        },

        get_nilas_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/nilas_ice', {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => this.nilas_ice = response.data.polygons) 
        },
        get_young_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/young_ice', {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => this.young_ice = response.data.polygons)
        },

        get_first_year_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/first_year_ice', {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => this.first_year_ice = response.data.polygons)
        },

        get_old_ice(){
            axios.get('http://127.0.0.1:5000/iceocean/api/v1.0/today/old_ice', {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => this.old_ice = response.data.polygons)
        },

        get_inf(){
            axios.get(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
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

                this.status = response.data.status,

                this.final_point_longitude = response.data.final_point_longitude,
                this.final_point_latitude = response.data.final_point_latitude,

                this.date_end = this.format_date(response.data.date_end)

            )).catch(err => {
                this.$router.push("/mistake") 
            })
        },
        format_date(date){

            if (date === '--'){
                return '--'
            }else{
                var d = new Date(date)

                var dd = d.getDate()
                if (dd < 10) dd = '0' + dd

                var mm = d.getMonth() + 1
                if (mm < 10) mm = '0' + mm

                var yy = d.getFullYear()

                return dd + '.' + mm + '.' + yy
            }
        },

        update_point(){

            axios.post("http://127.0.0.1:5000/iceocean/api/v1.0/generate_area", {
                start_longitude: this.final_point_longitude,
                start_latitude: this.final_point_latitude
            }, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
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
                date_enter: this.date_enter,
                id_rt: this.$route.params.id_rt,
                start_point_longitude: this.final_point_longitude,
                start_point_latitude: this.final_point_latitude,

                end_point_longitude: this.end_longitude,
                end_point_latitude: this.end_latitude,

                final_point_longitude: this.final_point_longitude,
                final_point_latitude: this.final_point_latitude,

                iceclass: this.ice_class,
                area_building_route: this.polygon
            }, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            }
            )

        },

        update_status(){
            axios.put(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${this.$route.params.id_rt}`, {
                date_enter: this.date_enter
            }, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            
            this.$router.go(0)

        },

        update_ice_condition(){
            axios.get("http://127.0.0.1:5000/iceocean/api/v1.0/random/ice_conditions", {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => (
                this.first_year_ice = response.data.first_year_ice,
                this.young_ice = response.data.young_ice,
                this.old_ice = response.data.old_ice,
                this.nilas_ice = response.data.nilas_ice,
                this.fast_ice = response.data.fast_ice,
                this.ice_field = response.data.ice_field
            ))
        },

        func_select_route(route, routes){
            this.select_route = route.id_itir
            this.first_year_ice = route.first_year_ice
            this.young_ice = route.young_ice
            this.old_ice = route.old_ice
            this.nilas_ice = route.nilas_ice
            this.fast_ice = route.fast_ice
            this.ice_field = route.ice_field
            this.get_inf()
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