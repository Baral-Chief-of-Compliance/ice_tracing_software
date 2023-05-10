<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Добавить маршрут</div>

        <v-container v-if="stage === 0">
            <div class="text-h5 mx-10">1.1 ШАГ: Введите имя судна</div>

            <v-row class="ml-5 my-5">
                <v-col
                    cols="12"
                    md="4"
                >
                    <v-text-field label="Название судна" color="purple-darken-4" v-model="ship_name" variant="underlined">

                    </v-text-field>
                </v-col>
            </v-row>

            <div class="text-h5 mx-10 my-5">1.2 ШАГ: Выбрать ледовый класс судна</div>

            <v-container>
                <v-radio-group v-model="iceclass">
                    <v-table>
                        <thead>
                            <tr>
                                <th class="text-h6">
                                    Выбран
                                </th>
                                <th class="text-h6" >
                                    Новое обозначение
                                </th>
                                <th class="text-h6">
                                    Прежнее обозначение 
                                </th>
                                <th class="text-h6">
                                    Описание
                                </th>
                            </tr>
                        </thead>
                        
                        <tbody>
                            <tr v-for="([new_title, old_title, description], i) in iceclasses" height="80">
                                <td>
                                    <v-radio :value="new_title" color="purple-darken-4" @click="sendiceclass"></v-radio>
                                </td>
                                <td>
                                    {{ new_title }} 
                                </td>
                                <td>
                                    {{ old_title }}
                                </td>
                                <td width="400">
                                    <v-expansion-panels >
                                        <v-expansion-panel>
                                            <v-expansion-panel-title>Подробно</v-expansion-panel-title>
                                            <v-expansion-panel-text >{{ description }}</v-expansion-panel-text>
                                        </v-expansion-panel>
                                    </v-expansion-panels>
                                </td>
                            </tr>
                        </tbody>
                    </v-table>
                </v-radio-group>
            </v-container>
        </v-container>

        <v-container v-if="stage === 1">
            <div class="text-h5 mx-10 mb-5">2 ШАГ: Выбрать начало и конец маршрута</div>
           
            <div class="d-flex ml-10">
                <div class="map">
                    <yandex-map
                        :coords="[71.10679806433585, 126.47064037736162]"
                        :zoom="3"
                        @click="onClick"
                    >

                    <ymap-marker 
                        :coords="start_coords" 
                        marker-id="1" 
                    />

                    <ymap-marker 
                        :coords="end_coords" 
                        marker-id="2" 
                        :icon="{ color: 'red' }"
                    />

                    </yandex-map>
                </div>

                <v-form class="ml-10">

                    <div class="d-flex justify-center pt-7">
                        <v-icon color="blue" icon="mdi-map-marker" class="mr-2 mt-1"></v-icon>
                        <span class="text-h6">Исходный пункт:</span>
                    </div>
                    

                    <v-text-field v-model="start_longitude" color="blue" label="Долгота" variant="underlined"></v-text-field>

                    <v-text-field v-model="start_latitude" color="blue" label="Широта" variant="underlined"></v-text-field>

                    <div class="d-flex justify-center pt-7">
                        <v-icon color="red" icon="mdi-map-marker" class="mr-2 mt-1"></v-icon>
                        <span class="text-h6">Пункт назначения:</span>
                    </div>

                    <v-text-field v-model="end_longitude" color="red" label="Долгота" variant="underlined"></v-text-field>
         
                    <v-text-field v-model="end_latitude" color="red" label="Широта" variant="underlined"></v-text-field>

                    <div class="d-flex justify-center pt-7">
                        <span class="text-h6">Отметить на карте:</span>
                    </div>

                    <v-radio-group v-model="points" class="mt-2">
                        <v-radio value="start" color="purple-darken-4">
                            <template v-slot:label>
                                    <v-icon color="blue" icon="mdi-map-marker" class="mr-2"></v-icon>
                                    <span class="text-h6">Исходный пункт</span>
                            </template>
                        </v-radio>

                        <v-radio value="end" color="purple-darken-4">
                            <template v-slot:label>
                                    <v-icon color="red" icon="mdi-map-marker" class="mr-2"></v-icon>
                                    <span class="text-h6">Пункт назначения</span>
                            </template>
                        </v-radio>
                    </v-radio-group>
                </v-form>
            </div>

        </v-container>

        <v-container v-if="stage === 2">
            <div class="text-h5 mx-10 mb-5">3 ШАГ: Настройки для построения маршрута</div>
            
            <div class="d-flex ml-10">
                <div class="map">
                    <yandex-map
                        :coords="start_coords"
                        :zoom="4"
                    >

                        <!-- <ymap-marker 
                            :coords="start_coords" 
                            marker-id="2" 
                            marker-type="Circle"
                            :circle-radius="radius"

                        /> -->

                        <ymap-marker 
                            :coords="start_coords" 
                            marker-id="1" 
                        />

                        <ymap-marker 
                            :coords="end_coords" 
                            marker-id="3" 
                            :icon="{ color: 'red' }"
                        />

                        <ymap-marker 
                            :coords="[this.polygon]" 
                            marker-id="2"
                            marker-type="Polygon" 
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


                    <div class="d-flex justify-center pt-7">
                        <span class="text-h6">Дата отправления:</span>
                    </div>

                    <v-text-field type="date" color="purple-darken-4" v-model="date_start"></v-text-field>
                    

                </v-form>
            </div>
            <v-dialog
                v-model="dialog"
                width="auto"
            >
                <template v-slot:activator="{ props }">
                    <v-btn block class="mx-8 pa-5 mt-8 text-h6" 
                        color="purple-darken-4" 
                        v-bind="props">
                        Построить маршрут
                    </v-btn>
                </template>

                <v-card width="500">
                    <v-card-title>
                        Добавить маршрут
                    </v-card-title>
                    <v-card-text>
                        <v-text-field v-model="route_name" label="Название маршрута" color="purple-darken-4" variant="underlined">

                        </v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="red" @click="dialog = false">Закрыть</v-btn>
                        <v-spacer></v-spacer>
                        <v-btn color="green" @click="add_route()">Добавить</v-btn>
                    </v-card-actions>
                </v-card>

            </v-dialog>

        </v-container>

        <v-row class="ma-10">
            <v-btn  @click="back" color="gray" v-if="stage != 0">
                Предыдущий шаг
            </v-btn>
            <v-spacer></v-spacer>

            <v-btn @click="next" color="purple-darken-4"  v-if="stage != 2">
                Следующий шаг
            </v-btn>
        </v-row>
        {{ this.polygon }}
    </v-container>


</template>

<script>
import axios from 'axios';


export default{
    data: () => ({
        stage: 0,

        iceclass: "",
        start_longitude: 170.39220116469363,
        start_latitude: 70.63562822509428,
        end_longitude: 60.76615063298328,
        end_latitude: 71.34638528176734,

        start_coords: [],
        end_coords: [],

        ship_name: "",
        points: "start",

        min: 0,
        max: 20,
        lenght_left_side: 10,
        lenght_right_side: 10,
        width_top_side: 10,
        width_bottom_side: 10,

        polygon: [                [
                    [55.75, 37.80],
                    [55.80, 37.90],
                    [55.75, 38.00],
                    [55.70, 38.00],
                    [55.70, 37.80]
                ]],

        date_start: "",
        route_name: "",

        dialog: false,

        iceclasses: [
            ['Ice1', 'ЛУ1', 'Самостоятельное эпизодическое плавание в мелкобитом разреженном льду неарктических морей и в сплошном льду в канале за ледоколом при толщине льда до 0,4 м'],
            ['Ice2', 'ЛУ2', 'Самостоятельное плавание в мелкобитом разреженном льду неарктических морей и в сплошном льду в канале за ледоколом при толщине льда до 0,55 м'],
            ['Ice3', 'Лу3', 'Самостоятельное плавание в мелкобитом разреженном льду неарктических морей и в сплошном льду в канале за ледоколом при толщине льда до 0,7 м'],
            ['Arc4', 'ЛУ4', 'Самостоятельное плавание в разреженных однолетних арктических льдах толщиной до 0,6 м в зимне-весеннюю навигацию и до 0,8 м в летне-осеннюю навигацию. Плавание в канале за ледоколом в однолетних арктических льдах толщиной до 0,7 м в зимне-весеннюю навигацию и до 1,0 м в летне-осеннюю навигацию'],
            ['Arc5', 'ЛУ5', 'Самостоятельное плавание в разреженных однолетних арктических льдах толщиной до 0,8 м в зимне-весеннюю навигацию и до 1,0 м в летне-осеннюю навигацию. Плавание в канале за ледоколом в однолетних арктических льдах толщиной до 0,9 м в зимне-весеннюю навигацию и до 1,2 м в летне-осеннюю навигацию'],
            ['Arc6', 'ЛУ6', 'Самостоятельное плавание в разреженных однолетних арктических льдах толщиной до 1,1 м в зимне-весеннюю навигацию и до 1,3 м в летне-осеннюю навигацию. Плавание в канале за ледоколом в однолетних арктических льдах толщиной до 1,2 м в зимне-весеннюю навигацию и до 1,7 м в летне-осеннюю навигацию'],
            ['Arc7', 'ЛУ7', 'Самостоятельное плавание в сплоченных однолетних арктических льдах толщиной до 1,4 м в зимне-весеннюю навигацию и до 1,7 м в летне-осеннюю навигацию при эпизодическом преодолении ледовых перемычек с помощью работы набегами. Плавание в канале за ледоколом в однолетних арктических льдах толщиной до 2,0 м в зимне-весеннюю навигацию и в двухлетних арктических льдах толщиной до 3,2 м в летне-осеннюю навигацию'],
            ['Arc8', 'ЛУ8', 'Самостоятельное плавание в сплоченных однолетних и двухлетних арктических льдах толщиной до 2,1 м в зимне-весеннюю навигацию и до 3,1 м в летне-осеннюю навигацию. Преодоление ледовых перемычек с помощью работы набегами. Плавание в канале за ледоколом в двухлетних арктических льдах толщиной до 3,4 м в зимне-весеннюю навигацию и в многолетних льдах в летне-осеннюю навигацию без ограничений'],
            ['Arc9', 'ЛУ9', 'Самостоятельное плавание в сплоченных многолетних арктических льдах толщиной до 3,5 м в зимне-весеннюю навигацию и до 4,0 м в летне-осеннюю навигацию. Преодоление ледовых перемычек с помощью работы набегами. Эпизодическое преодоление участков однолетних и двухлетних сплошных льдов с помощью работы набегами']
        ]
    }),

    methods: {
        next(){
            this.stage++

            if(this.stage === 2){
                axios.post("http://127.0.0.1:5000/iceocean/api/v1.0/generate_area", 
                {
                    start_longitude: this.start_longitude,
                    start_latitude: this.start_latitude
                }
                ).then(response => this.polygon = response.data.polygon)
            }
        },

        back(){
            this.stage--
        },
        onClick(e) {

            if (this.points === 'start'){
                this.start_coords = e.get('coords');
                this.start_latitude = this.start_coords[0]
                this.start_longitude = this.start_coords[1]
            }
            else if (this.points === 'end'){
                this.end_coords = e.get('coords');
                this.end_latitude = this.end_coords[0]
                this.end_longitude = this.end_coords[1]
            }

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

        add_route(){
            axios.post("http://127.0.0.1:5000/iceocean/api/v1.0/add_route", 
                {
                    ship_name: this.ship_name,
                    iceclass: this.iceclass,

                    start_longitude: this.start_longitude,
                    start_latitude: this.start_latitude,

                    end_longitude: this.end_longitude,
                    end_latitude: this.end_latitude,

                    area_building_route: this.polygon,

                    date_start: this.date_start,

                    route_name: this.route_name
                }
            )

            this.$router.push({ path: 'Routes'})
        }


    },

    mounted(){
        this.start_coords = [this.start_latitude, this.start_longitude]
        this.end_coords = [this.end_latitude, this.end_longitude]
    }   
}
</script>

<style scoped>
.ymap-container {
    width: 1400px;
    height: 700px;
}

</style>