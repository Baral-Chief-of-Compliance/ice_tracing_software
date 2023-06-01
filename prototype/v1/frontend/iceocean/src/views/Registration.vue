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

            <v-card-title>Регистрация</v-card-title>
            
            <form @submit.prevent="submit">
                <v-text-field
                    density="compact"
                    placeholder="Почта"
                    prepend-inner-icon="mdi-email"
                    variant="outlined"
                    color="purple-darken-4"
                    v-model="email.value.value" :error-messages="email.errorMessage.value"
                ></v-text-field>

                <v-text-field
                    density="compact"
                    placeholder="Логин"
                    prepend-inner-icon="mdi-account"
                    variant="outlined"
                    color="purple-darken-4"
                    v-model="login.value.value" :error-messages="login.errorMessage.value"
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
                    v-model="password.value.value" 
                    :error-messages="password.errorMessage.value"
                ></v-text-field>

                <v-text-field
                    :append-inner-icon="visible_check  ? 'mdi-eye-off' : 'mdi-eye'"
                    :type="visible_check  ? 'text' : 'password'"
                    density="compact"
                    placeholder="Повтор пароля"
                    prepend-inner-icon="mdi-lock-outline"
                    variant="outlined"
                    color="purple-darken-4"
                    @click:append-inner="visible_check  = !visible_check"
                    v-model="password_check.value.value"
                    :error-messages="password_check.errorMessage.value"
                    class="mb-5"
                ></v-text-field>

                <div class="text-red">{{ this.errorTextMsg }}</div>

                <v-btn
                    width="320"
                    class="mb-8 mt-5"
                    color="purple-darken-4"
                    size="large"
                    type="submit"
                >
                    Зарегистрироваться
                </v-btn>
            </form>
            <v-card-text class="text-center">
                <router-link
                class="text-purple-darken-4 text-decoration-none"
                rel="noopener noreferrer"
                :to="{ name: 'Login'}"
                >
                У меня уже есть учетная запись <v-icon icon="mdi-chevron-right" class="pt-2"></v-icon>
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
                    Просиходит регистрация, подождите
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
import { setJWT } from "@/store/TokenStore";
import { useField, useForm } from 'vee-validate'
import router from "@/router";
import { ref } from 'vue'

  export default {
    setup(){
        const { handleSubmit, handleReset } = useForm({
            validationSchema: {
                login (value) {
                    if (value?.length >= 4) return true

                        return 'Не меньше 4-х символов'
                },

                password (value){
                    if (value?.length >= 8) return true

                        return 'Не меньше 8-и символов'
                },

                email (value) {
                    if (/^[a-z0-9.-]+@[a-z.-]+\.[a-z]+$/i.test(value)) return true

                    return 'Неправильно написана почта'
                },

                password_check (value){
                    if (value === password.value.value) return true

                    return 'Пароли не совпадают'
                }
            }
        })

        const login = useField('login')
        const email = useField('email')
        const password = useField('password')
        const password_check = useField('password_check')
        const errorTextMsg = ref("")

        function registration(email, login, password, errorTextMsg){
            axios.post("http://127.0.0.1:5000/iceocean/api/v1.0/registration", {
                email: email,
                login: login,
                password: password
            }).then((response) => {
                setJWT(response.data.token, response.data.login, response.data.email)
                router.push({name: 'Records'})
            }).catch(err => {
                errorTextMsg.value = err.response.data.error
            })
        }

        const submit = handleSubmit(values => {
            registration(email.value.value, login.value.value, password.value.value, errorTextMsg)
        })



        return { login, email, password, password_check, submit, errorTextMsg }
    },

    data: () => ({
        visible: false,
        visible_check: false,
        dialog_loading: false,
        errorTextMsg: ""
    }),

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