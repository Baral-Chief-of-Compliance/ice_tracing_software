<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Сообщить об ошибке</div>

        <v-btn  variant="outlined" class="mx-10" :to="{name: 'Home'}">
            <v-icon icon="mdi-arrow-collapse-left" color="purple-darken-4" class="mr-2"></v-icon>назад
        </v-btn>

        <v-container class="px-15">
            <v-textarea v-model="problem" label="Опишите суть проблемы"></v-textarea>
        </v-container>
        
        <v-btn @click="send_problem" block class="mx-8 pa-5 mt-8 text-h6" v-if="problem != ''" color="purple-darken-4">
            Сообщить о проблеме
        </v-btn>
    </v-container>
</template>


<script>
    export default {
        data: () => ({
            problem: ""
        }),

        methods: {
            send_problem(){
                this.$router.push({name: 'Home'})
            }
        }
    }
</script>