<template>
    <v-container>
        <div class="text-h1">Записи</div>

        {{  this.records }}

        <v-card>
            <v-card-title>Добавить запись</v-card-title>
            <v-text-field label="Текст записи" v-model="record"></v-text-field>
            <v-btn @click="add_record">Добавить запись</v-btn>
        </v-card>
    </v-container>
</template>

<script>
import axios from 'axios';

  export default{
    data () {
        return{
            records: null,
            record: ""
        }
    },

    methods: {
        get_records(){
            axios.get("http://127.0.0.1:5000/records", {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                }
            })
            .then(response => (
                console.log(response),
                this.records = response.data
            ))
        },

        add_record(){
            axios.post("http://127.0.0.1:5000/add_record", {
                record: this.record
            }, {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                }
            })
        }
    },

    mounted(){
        this.get_records()
    }

  }
</script>