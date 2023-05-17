<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Сгенирировать ледовую обстановку 

        <v-tooltip
          v-model="show_tooltip_random"
          location="end"
        >
            <template v-slot:activator="{ props }">
                <v-btn
                    color="purple-darken-4"
                    icon="mdi-reload"
                    v-bind="props"
                >
                </v-btn>
            </template>
            <span>Сгенирировать случайнукю ледовую обстановку</span>
        </v-tooltip>
        
        </div> 

        <v-btn  variant="outlined" class="mx-10" :to="{name: 'Home'}">
            <v-icon icon="mdi-arrow-collapse-left" color="purple-darken-4" class="mr-2"></v-icon>назад
        </v-btn>

        <div class="text-h4 py-6 mx-10 mb-5 text-left">Ледовая обстановка на сегодня</div>

        <div class="map">
            <yandex-map
                :coords="[68.970360, 33.074172]"
                :zoom="3"
                :cluster-options="clusterOptions"
            >
                <ymap-marker v-if="!show_fast_ice" v-for="(polygon, index) in fast_ice" :key="index+1000"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#fffafa', opacity: 0.5}"
                    :marker-stroke="{color: '#fffafa', opacity: 1}"
                ></ymap-marker>

                <ymap-marker v-if="!show_ice_field" v-for="(polygon, index) in ice_field" :key="index+1000"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#b9b1b1', opacity: 0.5}"
                    :marker-stroke="{color: '#b9b1b1', opacity: 1}"
                ></ymap-marker>

                <ymap-marker v-if="!show_nilas_ice" v-for="(polygon, index) in nilas_ice" :key="index+1000"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#0968f5', opacity: 0.5}"
                    :marker-stroke="{color: '#0968f5', opacity: 1}"
                ></ymap-marker>

                <ymap-marker v-if="!show_young_ice" v-for="(polygon, index) in young_ice" :key="index+1000"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#f708f9', opacity: 0.5}"
                    :marker-stroke="{color: '#f708f9', opacity: 1}"
                ></ymap-marker>

                <ymap-marker v-if="!show_first_year_ice" v-for="(polygon, index) in first_year_ice" :key="index+1000"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#00c8a1', opacity: 0.7}"
                    :marker-stroke="{color: '#00c8a1', opacity: 1}"
                ></ymap-marker>

                <ymap-marker v-if="!show_old_ice" v-for="(polygon, index) in old_ice" :key="index+1000"
                    :marker-id="index"
                    marker-type="Polygon"
                    :coords="[polygon]"
                    :markerFill="{color: '#900001', opacity: 0.7}"
                    :marker-stroke="{color: '#900001', opacity: 1}"
                    suppressMapOpenBlock: true
                ></ymap-marker>

                <ymap-marker v-if="!show_ports" v-for="(port, index) in ports" :key="index+10000"
                    :marker-id="show_ports"
                    :balloon="{header: port.name }"
                    cluster-name="1"
                    :coords="[port.latitude, port.longitude]"
                    :icon="{ color: 'green' }"
                    @balloonopen="clik_baloon"
                    @balloonclose="clik_baloon"
                ></ymap-marker>

                </yandex-map>
                
        </div>


        <div class="text-h3 py-6 mx-10 text-left">Легенда карты</div>

        <div class="text-h4 py-6 mx-10 mb-5 text-left">Ледовая обстановка</div>
        
        <v-row>
            <v-col
                cols="12"
                md="4"
            >
                <v-row>
                    <v-card width="60" height="40" color="#0968f5">
                    </v-card>
                    <div class="pl-3 text-h5">нилас/nilas</div>
                </v-row>

                <v-row>
                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-switch v-model="show_nilas_ice" color="purple-darken-4" label="Скрыть"></v-switch>
                    </v-col>

                    <v-col
                        cols="12"
                        md="4"
                    >  
                        <v-dialog
                            v-model="dialog_nilas_ice"
                            width="auto"
                        >
                                <template v-slot:activator="{ props }">
                                    <v-btn
                                    color="purple-darken-4"
                                    icon="mdi-information-outline"
                                    v-bind="props"
                                    >
                                    </v-btn>
                                </template>

                            <v-card>
                                <v-card-text>
                                    Нилас — тонкий (до 10 см) эластичный сплош­ной лед, изгибающийся на волне и разламывающийся ветром.
                                </v-card-text>
                                <v-card-actions>
                                <v-btn color="purple-darken-4" block @click="dialog_nilas_ice = false">Закрыть</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-col>
                    
                </v-row>
                
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
                <v-row>
                    <v-card width="60" height="40" color="#f708f9">
                    </v-card>
                    <div class="pl-3 text-h5">молодой/young</div>
                </v-row>

                <v-row>
                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-switch v-model="show_young_ice" color="purple-darken-4" label="Скрыть"></v-switch>
                    </v-col>

                    <v-col
                        cols="12"
                        md="4"
                    >  
                        <v-dialog
                            v-model="dialog_young_ice"
                            width="auto"
                        >
                            <template v-slot:activator="{ props }">
                                <v-btn
                                color="purple-darken-4"
                                icon="mdi-information-outline"
                                v-bind="props"
                                >
                                </v-btn>
                            </template>

                            <v-card>
                                <v-card-text>
                                    Белый лед, толщиной от 30 до 70 см, в неарк­тических морях является предельной возрастной стадией.
                                </v-card-text>
                                <v-card-actions>
                                <v-btn color="purple-darken-4" block @click="dialog_young_ice = false">Закрыть</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-col>
                </v-row>
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
                <v-row>
                    <v-card width="60" height="40" color="#00c8a1">
                    </v-card>
                    <div class="pl-3 text-h5">однолетний/first-year</div>
                </v-row>

                <v-row>
                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-switch v-model="show_first_year_ice" color="purple-darken-4" label="Скрыть"></v-switch>
                    </v-col>
                    
                    <v-col
                        cols="12"
                        md="4"
                    >  
                        <v-dialog
                            v-model="dialog_first_year_ice"
                            width="auto"
                        >
                            <template v-slot:activator="{ props }">
                                <v-btn
                                color="purple-darken-4"
                                icon="mdi-information-outline"
                                v-bind="props"
                                >
                                </v-btn>
                            </template>

                            <v-card>
                                <v-card-text>
                                    Однолетний лед — к концу весны достигает толщины 1,5 м, в период летнего таяния обычно пол­ностью не исчезает.
                                </v-card-text>
                                <v-card-actions>
                                <v-btn color="purple-darken-4" block @click="dialog_first_year_ice = false">Закрыть</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-col>

                </v-row>
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
                <v-row class="mt-5">
                    <v-card width="60" height="40" color="#900001">
                    </v-card>
                    <div class="pl-3 text-h5">старый/old</div>
                </v-row>

                <v-row>

                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-switch v-model="show_old_ice" color="purple-darken-4" label="Скрыть"></v-switch>
                    </v-col>

                    <v-col
                        cols="12"
                        md="4"
                    >  
                        <v-dialog
                            v-model="dialog_old_ice"
                            width="auto"
                        >
                            <template v-slot:activator="{ props }">
                                <v-btn
                                color="purple-darken-4"
                                icon="mdi-information-outline"
                                v-bind="props"
                                >
                                </v-btn>
                            </template>

                            <v-card>
                                <v-card-text>
                                    Многолетний (паковый) лед толщиной от 2,5 м и более, поверхность обычно холмистая.
                                </v-card-text>
                                <v-card-actions>
                                <v-btn color="purple-darken-4" block @click="dialog_old_ice = false">Закрыть</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-col>
                </v-row>
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
                <v-row class="mt-5">
                    <v-card width="60" height="40" color="#b9b1b1">
                    </v-card>
                    <div class="pl-3 text-h5">отд. поле/ice floe</div>
                </v-row>

                <v-row>

                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-switch v-model="show_ice_field" color="purple-darken-4" label="Скрыть"></v-switch>

                    </v-col>

                    <v-col
                        cols="12"
                        md="4"
                    >  
                        <v-dialog
                            v-model="dialog_ice_field"
                            width="auto"
                        >
                            <template v-slot:activator="{ props }">
                                <v-btn
                                color="purple-darken-4"
                                icon="mdi-information-outline"
                                v-bind="props"
                                >
                                </v-btn>
                            </template>

                            <v-card>
                                <v-card-text>
                                    Льдина — отдельный кусок льда, дрейфующий на поверхности воды. Льдины бывают совершенно разных размеров.
                                </v-card-text>
                                <v-card-actions>
                                <v-btn color="purple-darken-4" block @click="dialog_ice_field = false">Закрыть</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-col>
                </v-row>
            </v-col>


            <v-col
                cols="12"
                md="4"
            >
                <v-row class="mt-5">
                    <v-card width="60" height="40" color="#fffafa">
                    </v-card>
                    <div class="pl-3 text-h5">припай/fast ice</div>
                </v-row>

                <v-row>

                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-switch v-model="show_fast_ice" color="purple-darken-4" label="Скрыть"></v-switch>
                    </v-col>

                    <v-col
                        cols="12"
                        md="4"
                    >  
                        <v-dialog
                            v-model="dialog_fast_ice"
                            width="auto"
                        >
                            <template v-slot:activator="{ props }">
                                <v-btn
                                color="purple-darken-4"
                                icon="mdi-information-outline"
                                v-bind="props"
                                >
                                </v-btn>
                            </template>

                            <v-card>
                                <v-card-text>
                                    Припай — обширный ледяной покров, связанный с берегом, от которого может простираться на десятки и сотни миль.
                                </v-card-text>
                                <v-card-actions>
                                <v-btn color="purple-darken-4" block @click="dialog_fast_ice = false">Закрыть</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-col>


                </v-row>
            </v-col>

        </v-row>

        <div class="text-h4 py-6 mx-10 mb-5 text-left">Другие объекты на карте</div>

        <v-row>
            <v-col
                cols="12"
                md="4"
            >
                <v-row>
                    <v-icon class="mt-1" color="green" icon="mdi-map-marker"></v-icon>
                    <div class="pl-3 text-h5">порт</div>
                </v-row>

                <v-row>
                    <v-switch v-model="show_ports" color="purple-darken-4" label="Скрыть"></v-switch>
                </v-row>
                
            </v-col>
        </v-row>
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

            show_fast_ice: false,
            show_ice_field: false,
            show_nilas_ice: false,
            show_young_ice: false,
            show_first_year_ice: false,
            show_old_ice: false,
            show_ports: true,

            dialog_nilas_ice: false,
            dialog_young_ice: false,
            dialog_first_year_ice: false,
            dialog_old_ice: false,
            dialog_ice_field: false,
            dialog_fast_ice: false,

            show_tooltip_random: false,

            clusterOptions: {
                1: {
                    clusterDisableClickZoom: true,
                    clusterOpenBalloonOnClick: true,
                    preset: 'islands#greenClusterIcons',
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
    },
    updated(){
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
    height: 700px;
}
</style>