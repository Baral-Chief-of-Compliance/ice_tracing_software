<template>
    <v-container>
        <v-form>
            <v-text-field label="Почта" v-model="email"></v-text-field>
            <v-text-field label="Логин" v-model="login"></v-text-field>
            <v-text-field label="Пароль" v-model="password"></v-text-field>
            <v-btn type="submit" block class="mt-2" @click="send_data_for_registration">Зарегестрироваться</v-btn>
        </v-form>
    </v-container>
</template>

<script>
import axios from "axios"

    export default{
        data: () => ({
            email: "",
            login: "",
            password: ""
        }),

        methods: {
            send_data_for_registration(){
                axios.post("http://127.0.0.1:5000/registration", {
                    email: this.email,
                    login: this.login,
                    password: this.password
                })
            }
        }
    }
</script>