<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Маршруты</div>
        <v-btn  variant="outlined" class="mx-10" :to="{name: 'Home'}">
            <v-icon icon="mdi-arrow-collapse-left" color="purple-darken-4" class="mr-2"></v-icon>назад
        </v-btn>

            <v-container>
                <v-col v-for="route in rotes" class="mx-10">
                    <v-hover v-slot="{ isHovering, props }" >
                        <v-card  class="pa-5 d-flex flex-row"
                            v-bind="props"
                            :color="isHovering ? 'purple-darken-4': undefined"
                            @click="enter_route(route.id_rt)"
                        >
                            <b class="pr-2">Название маршрута:</b>  {{ route.name }} 
                            <v-spacer></v-spacer> 
                            <b class="pr-2">Название судна:</b>  {{ route.name_sh }} 
                            <v-spacer></v-spacer> 
                            <b class="pr-2">Ледовый класс судна:</b>  {{ route.ice_class }}
                            <v-spacer></v-spacer>
                            <b class="pr-2">Дата начала:</b>  {{ this.format_date_v(route.date_enter) }}
                            <v-spacer></v-spacer>
                            <v-card :color=" route.status === 'в процессе' ? 'teal-accent-4' : (route.status === 'завершён' ? 'blue-grey':'orange-accent-4') " class="px-10 py-1">
                                {{ route.status }}
                            </v-card>
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
import { format_date } from '@/tools/views'


export default{
    data: () => ({
        rotes: []
    }),

    mounted(){
        this.get_routes()
        // setInterval(() => {
        //             location.reload();
        //         }, 10000);
    },

    updated(){
        this.get_routes()
    },

    methods: {
        get_routes(){
            axios.get("http://127.0.0.1:5000/iceocean/api/v1.0/route_inf", {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => this.rotes = response.data.routes).catch(err => {
                this.$router.push("/mistake") 
            })
        },

        delete_route(id_rt){
            axios.delete(`http://127.0.0.1:5000/iceocean/api/v1.0/route_inf/${id_rt}`, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then (
                rotes => this.get_routes()
            )
        },

        async enter_route(id_route){
            await this.$router.push({name: 'RouteInfo', params: {id_rt: id_route}}) 
        },

        format_date_v(date){
           date = format_date(date)
           return date
        }
        
    }
}
</script>