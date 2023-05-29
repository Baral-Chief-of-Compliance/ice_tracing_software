// Utilities
import { defineStore } from 'pinia'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'


const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

export const useAppStore =  defineStore('app', {
  state: () => ({
    jwt: ''
  }),


  actions: {
    addJWT(token){
      this.jwt = token
    }
  },
  persist: true
})
