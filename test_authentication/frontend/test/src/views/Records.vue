<template>
    <v-container>
        <div class="text-h1">Записи</div>

        {{  this.records }}
    </v-container>
</template>

<script>
import axios from 'axios';

  export default{
    data () {
        return{
            records: null
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
        }
    },

    mounted(){
        this.get_records()
    }

  }
</script>