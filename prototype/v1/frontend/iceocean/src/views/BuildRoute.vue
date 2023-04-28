<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Построить маршрут</div>

        <v-container v-if="stage === 0">
            <div class="text-h5 mx-10">1 ШАГ: Выбрать ледовый класс судна</div>
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
                                    <v-expansion-panels>
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
            <div class="text-h5 mx-10">2 ШАГ: Выбрать начало и конец маршрута</div>
            <v-form>
                <v-container>
                    <v-row>
                        <v-col
                            cols="12"
                            md="4"
                        >
                            <div class="d-flex justify-center pt-7">
                                <v-icon color="blue" icon="mdi-map-marker" class="mr-2 mt-1"></v-icon>
                                <span class="text-h6">Исходный пункт:</span>
                            </div>
                        </v-col>

                        <v-col
                            cols="12"
                            md="4"
                        >
                            <v-text-field v-model="start_longitude" color="blue" label="Долгота"></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            md="4"
                        >
                            <v-text-field v-model="start_latitude" color="blue" label="Широта"></v-text-field>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col
                            cols="12"
                            md="4"
                        >
                            <div class="d-flex justify-center pt-7">
                                <v-icon color="red" icon="mdi-map-marker" class="mr-2 mt-1"></v-icon>
                                <span class="text-h6">Пункт назначения:</span>
                            </div>
                        </v-col>

                        <v-col
                            cols="12"
                            md="4"
                        >
                            <v-text-field v-model="end_longitude" color="red" label="Долгота"></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            md="4"
                        >
                            <v-text-field v-model="end_latitude" color="red" label="Широта"></v-text-field>
                        </v-col>
                    </v-row>
                </v-container>
            </v-form>
            <v-btn block class="mx-8 pa-5 text-h6" color="purple-darken-4" @click="send_data">
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
import axios from 'axios'


export default{

    data: () => ({
        stage: 0,

        iceclass: "",
        start_longitude: "",
        start_latitude: "",
        end_longitude: "",
        end_latitude: "",

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
        getIceClass(iceclass){
            alert(iceclass)
        },
        send_data(){
            axios.post("http://127.0.0.1:5000/iceocean/api/v1.0/generate_route", 
            {
                iceclass: this.iceclass,
                start_longitude: this.start_longitude,
                start_latitude: this.start_latitude,
                end_longitude: this.end_longitude,
                end_latitude: this.end_latitude
            }
            )
        }
    }
}
</script>
