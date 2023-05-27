<template>
  <v-container>
    <v-form>
      <v-text-field label="Логин" v-model="login"/>
      <v-text-field label="Пароль" v-model="pass"/>
      <v-btn type="submit" block class="mt-2" @click="authenticate">Войти</v-btn>
    </v-form>
    <div color="red">{{  this.errorMsg }}</div>
    <v-btn block class="mt-10" :to="{name: 'Registration'}">Хотите зарегистрироваться</v-btn>
    {{ this.login }}
    {{ this.password }}
  </v-container>

</template>

<script>
import axios from "axios"

  export default {
    data: () => ({
      login: "",
      pass: "",
      errorMsg: ""
    }),

    methods: {
      authenticate (){
        this.$store.dispatch('login', this.login, this.password)
          .then(() => this.$router.push('/records'))
      }
    },

    mounted(){
        EventBus.$on('failedAuthentication', (msg) => {
        this.errorMsg = msg
      })
    },

    beforeDestroy () {
      EventBus.$off('failedAuthentication')
    }
  }
</script>
