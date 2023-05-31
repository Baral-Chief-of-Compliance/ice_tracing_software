<template>
    <v-container>
        <v-form>
            <v-text-field label="Почта" v-model="email"></v-text-field>
            <v-text-field label="Логин" v-model="login"></v-text-field>
            <v-text-field label="Пароль" v-model="password"></v-text-field>
            <v-btn type="submit" block class="mt-2" @click="register">Зарегестрироваться</v-btn>
        </v-form>
        <v-btn block class="mt-10" :to="{name: 'Login'}">У меня уже есть учетная запись</v-btn>
    </v-container>
</template>

<script>
import axios from "axios"


export default{
    data: () => ({
        email: "",
        login: "",
        password: "",
    })
}
</script>