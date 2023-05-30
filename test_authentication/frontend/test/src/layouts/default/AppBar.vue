<template>
  <v-app-bar flat>
    <v-app-bar-title>
      <v-icon icon="mdi-circle-slice-6" />

      Essentials Preset
    </v-app-bar-title>

    <v-btn variant="elevated" color="red" @click="exitFromAcc">Выйти</v-btn>

    <div>{{ this.login }}</div>
  </v-app-bar>
</template>

<script>
import { exitFromApp } from "@/store/TokenStore.js"


  export default{
    data: () => ({
        login: ""
    }),

    mounted() {
     if (localStorage.login) this.login = localStorage.login 
    },

    updated(){
      if (localStorage.login) this.login = localStorage.login 
    },

    methods: {
      exitFromAcc(){
        exitFromApp();
        this.login = ""
      }
    }
}
</script>
