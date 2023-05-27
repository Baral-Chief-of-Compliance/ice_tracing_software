import Vue from 'vue'
import Vuex from 'vuex'


import {authenticate, register, postNewRecord} from '@/api'
import { isValidJwt } from '@/utils'
// import { EventBus } from '@/utils'


Vue.use(Vuex)

const state = {
  // single source of data
  record: '',
  email: '',
  login: '',
  password: '',
  jwt: ''
}

const actions = {
    // asynchronous operations
  
    //
    // omitting the other action methods...
    //
  
    login (context, login, password) {
      context.commit('setLoginPassword', { login, password })
      return authenticate(login, password)
        .then(response => context.commit('setJwtToken', { jwt: response.data }))
        .catch(error => {
          console.log('Error Authenticating: ', error)
        //   EventBus.$emit('failedAuthentication', error)
        })
    },
    register (context, email, login, password) {
      context.commit('setEmailLoginPassword', { login, password, email })
      return register(email, login, password)
        .then(context.dispatch('login', login, password))
        .catch(error => {
          console.log('Error Registering: ', error)
        //   EventBus.$emit('failedRegistering: ', error)
        })
    },
    submitNewSurvey (context, survey) {
      return postNewSurvey(survey, context.state.jwt.token)
    }
  }


  const mutations = {
    // isolated data mutations
  
    //
    // omitting the other mutation methods...
    //
  
    setLoginPassword (state, payload) {
      console.log('setLoginPassword payload = ', payload)
      state.login = payload.login
      state.password = payload.password
    },


    setEmailLoginPassword (state, payload){
        console.log('setEmailLoginPassword payload = ', payload)
        state.email = payload.email
        state.login = payload.login
        state.password = payload.password

    },
    setJwtToken (state, payload) {
      console.log('setJwtToken payload = ', payload)
      localStorage.token = payload.jwt.token
      state.jwt = payload.jwt
    }
}


const getters = {
    // reusable data accessors
    isAuthenticated (state) {
      return isValidJwt(state.jwt.token)
    }
}