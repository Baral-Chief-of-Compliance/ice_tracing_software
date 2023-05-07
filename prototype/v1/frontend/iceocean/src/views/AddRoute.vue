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
                    <v-text-field label="Название судна" color="purple-darken-4" v-model="ship_name">

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
                        :coords="[68.970360, 33.074172]"
                        :zoom="3"
                        @click="onClick"
                    >

                    <ymap-marker 
                        :coords="start_coords" 
                        marker-id="1" 
                        hint-content="some hint" 
                    />

                    <ymap-marker 
                        :coords="end_coords" 
                        marker-id="2" 
                        hint-content="some hint" 
                        :icon="{ color: 'red' }"
                    />

                    </yandex-map>
                </div>

                <v-form class="ml-10">

                    <div class="d-flex justify-center pt-7">
                        <v-icon color="blue" icon="mdi-map-marker" class="mr-2 mt-1"></v-icon>
                        <span class="text-h6">Исходный пункт:</span>
                    </div>
                    

                    <v-text-field v-model="start_longitude" color="blue" label="Долгота"></v-text-field>

                    <v-text-field v-model="start_latitude" color="blue" label="Широта"></v-text-field>

                    <div class="d-flex justify-center pt-7">
                        <v-icon color="red" icon="mdi-map-marker" class="mr-2 mt-1"></v-icon>
                        <span class="text-h6">Пункт назначения:</span>
                    </div>

                    <v-text-field v-model="end_longitude" color="red" label="Долгота"></v-text-field>
         
                    <v-text-field v-model="end_latitude" color="red" label="Широта"></v-text-field>

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

            <v-btn block class="mx-8 pa-5 mt-8 text-h6" color="purple-darken-4" @click="send_data">
                Построить маршрут
            </v-btn>
        </v-container>

        <v-row class="ma-10">
            <v-btn  @click="back" color="gray" v-if="stage != 0">
                Предыдущий шаг
            </v-btn>

            <v-btn @click="next" color="purple-darken-4"  v-if="stage != 1">
                Следующий шаг
            </v-btn>
        </v-row>
    </v-container>


</template>

<script>

export default{
    data: () => ({
        stage: 0,

        iceclass: "",
        start_longitude: -168.39220116469363,
        start_latitude: 70.63562822509428,
        end_longitude: 60.76615063298328,
        end_latitude: 71.34638528176734,

        start_coords: [],
        end_coords: [],

        ship_name: "",
        points: "start",

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