<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Маршруты</div>

            <v-container>
                <v-col v-for="route in rotes" class="mx-10">
                    <v-hover v-slot="{ isHovering, props }" >
                        <v-card  class="pa-5 d-flex flex-row"
                            v-bind="props"
                            :color="isHovering ? 'purple-darken-4': undefined"
                            :to = "{name: 'RouteInfo', params: {id_rt: route.id_rt}}"
                        >
                            <b class="pr-2">Название маршрута:</b>  {{ route.name }} 
                            <v-spacer></v-spacer> 
                            <b class="pr-2">Название судна:</b>  {{ route.name_sh }} 
                            <v-spacer></v-spacer> 
                            <b class="pr-2">Ледовый класс судна:</b>  {{ route.ice_class }}
                            <v-spacer></v-spacer>
                            <b class="pr-2">Дата начала:</b>  --
                            <v-spacer></v-spacer>
                            <b class="pr-2">Дата окончания:</b>  --
                        </v-card>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn @click="delete_route(route.id_rt)" color="red">
                                Удалить
                            </v-btn>
                        </v-card-actions>
                    </v-hover>
                </v-col>
            </v-container>


        <v-btn block class="mx-8 pa-5 text-h6" color="purple-darken-4" :to="{ name: 'AddRoute'}">
                Добавить маршрут
        </v-btn>
    </v-container>
</template>

<script>
import axios from 'axios';


export default{
    data: () => ({
        rotes: []
    }),

    mounted(){
        this.get_routes()
    },

    updated(){
        this.get_routes()
    },

    methods: {
        get_routes(){
            axios.get("http://127.0.0.1:5000/iceocean/api/v1.0/route_inf")
            .then(response => this.rotes = response.data.routes)
        },

        delete_route(id_rt){
            axios.delete(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${id_rt}`)
            .then (
                rotes => this.get_routes()
            )
        }
    }
}
</script>