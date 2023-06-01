<template>
    <v-container>
        <div class="text-red">{{ errorTextMsg }}</div>
        <form @submit.prevent="submit">
            <v-text-field label="Почта" v-model="email.value.value" :error-messages="email.errorMessage.value"></v-text-field>
            <v-text-field label="Логин" v-model="login.value.value" :error-messages="login.errorMessage.value"></v-text-field>

            <v-text-field 
                :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                :type="visible ? 'text' : 'password'"
                label="Пароль" 
                v-model="password.value.value" 
                :error-messages="password.errorMessage.value"
                @click:append-inner="visible = !visible"
            >
            </v-text-field>

            <v-text-field
                :append-inner-icon="visible_check ? 'mdi-eye-off' : 'mdi-eye'" 
                :type="visible_check ? 'text' : 'password'"
                label="Повторение пароля" 
                v-model="password_check.value.value"
                :error-messages="password_check.errorMessage.value"
                @click:append-inner="visible_check = !visible_check"
            > 
            </v-text-field>

            <v-btn type="submit" block class="mt-2">Зарегестрироваться</v-btn>
        </form>
        <v-btn block class="mt-10" :to="{name: 'Login'}">У меня уже есть учетная запись</v-btn>
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
</template>

<script>
import axios from "axios"
import { setJWT } from "@/store/TokenStore";
import { useField, useForm } from 'vee-validate'
import router from "@/router";
import { ref } from 'vue'


export default{
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
            axios.post("http://127.0.0.1:5000/registration", {
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
        dialog_loading: false
    }),

    methods: {
        registration(email, login, password){
            axios.post("http://127.0.0.1:5000/registration", {
                email: email,
                login: login,
                password: password
            }).then((response) => {
                setJWT(response.data.token, response.data.login, response.data.email)
                this.$router.push("/records")
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
        })
    }
}
</script>