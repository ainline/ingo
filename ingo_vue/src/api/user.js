/**
 * user 用户模块接口列表
 */
import base from '@/api/base'
import axios from '@/utils/request'
import qs from 'qs'

const user = {
  getUserInfo(params) {
    return axios.get('url', params)
  }
}
export function login(params) {
  return axios.post(`${base.url}/user`, qs.stringify(params))
}

export default user

// export function logins(data) {
//   return request({
//     url: '/user/login',
//     method: 'post',
//     data
//   })
// }

// export function getInfo(token) {
//   return request({
//     url: '/user/info',
//     method: 'get',
//     params: { token }
//   })
// }

// export function logout() {
//   return request({
//     url: '/user/logout',
//     method: 'post'
//   })
// }
