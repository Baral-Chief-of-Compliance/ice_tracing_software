<template>
  <v-container>
      <v-text-field label="Логин" v-model="login"/>
      <v-text-field label="Пароль" v-model="pass"/>
      <v-btn type="submit" block class="mt-2" @click="authenticate">Войти</v-btn>
    <v-btn block class="mt-10" :to="{name: 'Registration'}">Хотите зарегистрироваться</v-btn>
    {{ this.login }}
    {{ this.password }}
    {{ this.jwt }}
  </v-container>

</template>

<script>
import axios from "axios"
import { useAppStore } from '@/store/app'
import { mapActions } from 'pinia'


export default {
  data:() => ({
    login: "",
    pass: "",
    jwt: ""
  }),

  methods: {

    ...mapActions(useAppStore, ['addJWT']),

    authenticate(){
      axios.post("http://127.0.0.1:5000/enter", {
        login: this.login,
        password: this.pass
      }).then ((response) => {
        this.jwt = response.data.token
        this.addJWT(response.data.token)
      })
    }
  }
}
</script>
