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
      <div class="text-h4">ICEocean</div>
      <!-- <v-icon icon="mdi-circle-slice-4" /> -->
    </v-app-bar-title>
    <div>
      {{ this.login }} |
    </div>

    <v-btn class="ml-2" variant="flat" color="red" @click="exitFromAcc">выйти</v-btn>
    <div class="ml-5 mr-15">
      <v-icon  class="mr-3" icon="mdi-file-document" />
      <v-icon  icon="mdi-message-alert" />
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
