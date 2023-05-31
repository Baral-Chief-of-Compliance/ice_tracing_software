<template>
  <v-container>
      <div class="text-red">{{ this.errorTextMsg }}</div>
      <v-text-field label="Логин" v-model="login"/>
      <v-text-field
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        label="Пароль" 
        v-model="pass"
        @click:append-inner="visible = !visible"
      />
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
    errorTextMsg: "",
    visible: false,
  }),

  methods: {

    authenticate(){
      axios.post("http://127.0.0.1:5000/enter", {
        login: this.login,
        password: this.pass
      }).then ((response) => {
        this.jwt = response.data.token
        setJWT(this.jwt, response.data.login, response.data.email)
        this.$router.push("/records")
      }).catch(err => {
        console.log(err.response.data.error)
        this.password = ""
        this.errorTextMsg = err.response.data.error

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
