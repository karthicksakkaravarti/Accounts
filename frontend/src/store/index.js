import appConfigStoreModule from '@core/@app-config/appConfigStoreModule'
import Vue from 'vue'
import Vuex from 'vuex'
import app from './app'
import axiosIns from '@/plugins/axios.js'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {
    signup({commit}, payload){
      return new Promise((resolve, reject) => {
        axiosIns.post('/api/signup/', payload)
        .then(data => {
          resolve(data)
        })
        .catch(err => {
          reject(err)
        })
      })
    }
  },
  modules: {
    appConfig: appConfigStoreModule,
    app,
  },
})
