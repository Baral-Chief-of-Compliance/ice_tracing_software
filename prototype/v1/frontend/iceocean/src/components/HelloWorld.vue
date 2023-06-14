<template>
  <v-container
    class="d-flex justify-center mb-10"
  >
    <v-card 
      width="400"
      height="350"
      class="mt-15"
    >
      <v-card-title class="text-h4">
        Меню
      </v-card-title>
      <v-card-subtitle>
        Выберите пункт
      </v-card-subtitle>
      <v-card-text>
        <v-btn class="mb-3 pa-5" color="purple-darken-4" block :to="{ name: 'Routes'}"  >Маршруты</v-btn>
        <v-btn class="mb-3 mt-3 pa-5" color="purple-darken-4" block :to="{ name: 'GenerateIceConditions'}">Ледовая обстановка</v-btn>
        <v-btn class="mb-3 mt-3 pa-5" color="purple-darken-4" block :to="{ name: 'Manual'}">Руководоство</v-btn>
        <v-btn class="mb-3 mt-3 pa-5" color="purple-darken-4" block  >Материал</v-btn>
        <v-btn class="mb-3 mt-3 pa-5" color="purple-darken-4" block>Сообщить об ошибке</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios"

export default {
  methods: {
    chek_authorization(){
      axios.get('http://127.0.0.1:5000/', {
                headers: {
                    Authorization: `Bearer: ${localStorage.jwt}`  
                } 
            })
            .then(response => this.rotes = response.data.routes).catch(err => {
                this.$router.push("/mistake") 
            })
    }
  },

  mounted(){
    this.chek_authorization()
  }
}
</script>
