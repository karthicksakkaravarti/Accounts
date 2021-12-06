import Vue from 'vue'
import Vuex from 'vuex'
import Axios from "../respo"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    UserInfo: null,
  },
  mutations: {
    SetUserInfo (state, data) {
      state.UserInfo = data
    }
  },
  getters: {
    GetUserInfo: state => {
      return state.UserInfo
    }
  },
  actions: {
    GET_USER_API({commit }, queryParam){
      return new Promise((resolve, reject) => {
        Axios.get('api/user/'+queryParam)
          .then(data => {
            commit('SetUserInfo', data.data)
              resolve(data)
          })
          .catch(err => {
              reject(err)
          })
      })
  },
  },
  modules: {
  }
})
