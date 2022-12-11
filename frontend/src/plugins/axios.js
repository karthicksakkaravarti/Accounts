// axios
import axios from 'axios'
import Vue from 'vue'

const axiosIns = axios.create({
  // You can add your headers here
  // ================================
  // baseURL: 'http://127.0.0.1:8001/',
  // timeout: 1000,
  // headers: {'X-Custom-Header': 'foobar'}
})

axiosIns.interceptors.request.use(
  config => {
    // Do something before request is sent

    const accessToken = localStorage.getItem('accessToken')

    // eslint-disable-next-line no-param-reassign
    if (accessToken) config.headers.Authorization = `Bearer ${accessToken}`

    return config
  },
  error => Promise.reject(error),
)

Vue.prototype.$http = axiosIns

export default axiosIns
