<template>
  <v-app-bar color="purple-darken-4">

    <v-img
    class="ml-15"
    src="@/assets/logo_iceocean.svg"
    max-height="80"
    max-width="80"
    contain
    ></v-img>
    <v-app-bar-title>
      <v-btn :to="{ name: 'Home'}">
        <div class="text-h4">ICEocean</div>
      </v-btn>
      <!-- <v-icon icon="mdi-circle-slice-4" /> -->
    </v-app-bar-title>
    <div>
      {{ this.login }} |
    </div>

    <v-btn class="ml-2" variant="flat" color="red" @click="exitFromAcc">выйти</v-btn>
    <div class="ml-5 mr-15">
      <v-btn :to="{ name: 'Manual'}">
        <v-icon  class="mr-3" icon="mdi-file-document" />
      </v-btn>
      
      <v-btn :to="{ name: 'Report'}">
        <v-icon  icon="mdi-message-alert" />
      </v-btn>

    </div>
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

    methods: {
      exitFromAcc(){
        exitFromApp();
        this.login = "";
        this.$router.push("/login")
      }
    }
  }
</script>
