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
            ></v-text-field>


            <v-btn
                width="320"
                class="mb-8 mt-5"
                color="purple-darken-4"
                size="large"
            >
                Войти
            </v-btn>

            <v-card-text class="text-center">
                <a
                class="text-purple-darken-4 text-decoration-none"
                href="#"
                rel="noopener noreferrer"
                target="_blank"
                >
                Зарегистрироваться <v-icon icon="mdi-chevron-right" class="pt-2"></v-icon>
                </a>
            </v-card-text>
            </v-card>
        </div>
        </v-container>
    </v-app>
</template>
  
<script>
  export default {
    data: () => ({
      visible: false,
    }),
  }
</script>

<style scoped>
.main{
    background-image: url("../assets/background.svg");
}
</style>