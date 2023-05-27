<template>
    <v-container>
        <span class="text-h1">Добавить запись</span>
        <v-form>
            <v-text-field label="Запись" v-model="record"></v-text-field>
            <v-btn type="submit" block class="mt-2" @click="add_record(jwt)">Добавить</v-btn>
        </v-form>
    </v-container>
</template>

<script>
import axios from 'axios';

export default{
    data: () => ({
    record: ""
    }),

    methods: {
        add_record(jwt){
            axios.post('http://127.0.0.1:5000/add_record', {
                record: this.record
            },
            {
                headers: {
                    Authorization: `Bearer: ${jwt}`  
                }
            })
        }
    }
}
</script>