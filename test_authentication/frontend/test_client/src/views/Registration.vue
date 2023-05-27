<template>
    <v-container>
        <v-form>
            <v-text-field label="Почта" v-model="email"></v-text-field>
            <v-text-field label="Логин" v-model="login"></v-text-field>
            <v-text-field label="Пароль" v-model="password"></v-text-field>
            <v-btn type="submit" block class="mt-2" @click="register">Зарегестрироваться</v-btn>
        </v-form>
        <div color="red">{{  this.errorMsg }}</div>
    </v-container>
</template>

<script>
import axios from "axios"

    export default{
        data: () => ({
            email: "",
            login: "",
            password: "",
            errorMsg: ""
        }),

        methods: {
            register () {
                this.$store.dispatch('register', this.email, this.login, thes.password)
                    .then(() => this.$router.push('/'))
            }
        },

        mounted() {
            EventBus.$on('failedRegistering', (msg) => {
                this.errorMsg = msg
            })
        },

        beforeDestroy () {
            EventBus.$off('failedRegistering')
        }
    }
</script>