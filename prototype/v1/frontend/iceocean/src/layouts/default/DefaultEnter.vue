<template>
    <v-app class="main">
        <default-bar />

        <default-view />
    </v-app>
</template>
  
<script setup>
    import DefaultBar from './AppBar.vue'
    import DefaultView from './View.vue'
</script>

<style scoped>
.main{
    background-image: url("../../assets/background.svg");
}
</style>