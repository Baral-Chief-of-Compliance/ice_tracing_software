<template>
  <v-container>
    <v-form>
      <v-text-field label="Логин" v-model="login"/>
      <v-text-field label="Пароль" v-model="pass"/>
      <v-btn type="submit" block class="mt-2" @click="send_login_pass">Войти</v-btn>
    </v-form>
    {{ this.login }}
    {{ this.password }}
  </v-container>

</template>

<script>
import axios from "axios"

  export default {
    data: () => ({
      login: "",
      pass: ""
    }),

    methods: {
      send_login_pass(){
        axios.post("http://127.0.0.1:5000/enter", {
            login: this.login,
            password: this.pass
          } 
        )
      }
    }
  }
</script>
