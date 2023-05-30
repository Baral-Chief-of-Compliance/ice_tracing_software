<template>
  <v-container>
      <v-text-field label="Логин" v-model="login"/>
      <v-text-field label="Пароль" v-model="pass"/>
      <v-btn type="submit" block class="mt-2" @click="authenticate">Войти</v-btn>
    <v-btn block class="mt-10" :to="{name: 'Registration'}">Хотите зарегистрироваться</v-btn>
    {{ this.login }}
    {{ this.password }}
    {{ this.jwt }}

    <v-btn block class="mt-10" @click="check_authorized">Проверка авторизации</v-btn>

  </v-container>

</template>

<script>
import axios from "axios"
import { setJWT, isAuthorized, exitFromApp } from "@/store/TokenStore.js"


export default {
  data:() => ({
    login: "",
    pass: "",
    jwt: "",
    statusAuthorized: false
  }),

  methods: {

    authenticate(){
      axios.post("http://127.0.0.1:5000/enter", {
        login: this.login,
        password: this.pass
      }).then ((response) => {
        this.jwt = response.data.token
        setJWT(this.jwt, response.data.login, response.data.email)
        this.statusAuthorized = true
      })
    },

    check_authorized(){
      if (isAuthorized()){
        console.log("пользователь авторизован")
      } else{
        console.log("пользователь не авторизован")
      }
    }
  }
}
</script>
