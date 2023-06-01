<template>
    <v-app class="main">
        <v-container>
            <div>
                <div class="d-flex justify-center mb-3 mt-10">
                    <v-img
                        max-width="120"
                        src="@/assets/logo_iceocean.svg"
                    ></v-img>
                    <div class="text-h4 pt-7 pl-2" >ICEocean</div>
                </div>

            <v-card
            class="mx-auto pa-12 pb-8"
            elevation="8"
            max-width="448"
            rounded="lg"
            >

            <v-card-title>Вход в приложение</v-card-title>

            <v-text-field
                density="compact"
                placeholder="Логин"
                prepend-inner-icon="mdi-account"
                variant="outlined"
                color="purple-darken-4"
                v-model="login"
            ></v-text-field>

            <v-text-field
                :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                :type="visible ? 'text' : 'password'"
                density="compact"
                placeholder="Пароль"
                prepend-inner-icon="mdi-lock-outline"
                variant="outlined"
                color="purple-darken-4"
                @click:append-inner="visible = !visible"
                class="mb-5"
                v-model="pass"
            ></v-text-field>

            <div class="text-red">{{ this.errorTextMsg }}</div>


            <v-btn
                width="320"
                class="mb-8 mt-5"
                color="purple-darken-4"
                size="large"
                @click="authenticate"
            >
                Войти
            </v-btn>

            <v-card-text class="text-center">
                <router-link
                class="text-purple-darken-4 text-decoration-none"
                rel="noopener noreferrer"
                :to="{ name: 'Registration'}"
                >
                Зарегистрироваться <v-icon icon="mdi-chevron-right" class="pt-2"></v-icon>
                </router-link>
            </v-card-text>
            </v-card>
        </div>
        </v-container>

        <v-dialog
            v-model="dialog_loading"
            width="auto"
            persistent
        >
            <v-card
                color="purple-darken-4"
            >
                <v-card-text>
                    Просиходит вход, подождите
                    <v-progress-linear
                        indeterminate
                        color="white"
                        class="mb-0"
                    ></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>
    </v-app>
</template>
  
<script>
import axios from "axios"
import { setJWT } from "@/store/TokenStore.js"

  export default {
    data: () => ({
      visible: false,
      login: "",
      pass: "",
      jwt: "",
      errorTextMsg: "",
      dialog_loading: false
    }),

    methods: {
        authenticate(){
            axios.post("http://127.0.0.1:5000/iceocean/api/v1.0/enter", {
                login: this.login,
                password: this.pass
            }).then ((response) => {
                this.jwt = response.data.token
                setJWT(this.jwt, response.data.login, response.data.email)
                this.$router.push("/")
            }).catch(err => {
                this.password = ""

            })
        }
    },

    created(){
        axios.interceptors.request.use( (config)=>{
            this.dialog_loading = true
            return config
        }),

        axios.interceptors.response.use((response) =>{
            this.dialog_loading = false
            // if (response.config.method == 'post' && response.config.url == 'http://127.0.0.1:4000/iceocean/api/v1.0/microservice/build_route'){
            //     this.$router.go(0)
            // }
            return response
        },
        error => {
            this.dialog_loading = false
            this.errorTextMsg = error.response.data.error
            return error
        }
        )
    }
  }
</script>


<style scoped>
.main{
    background-image: url("../assets/background.svg");
}
</style>