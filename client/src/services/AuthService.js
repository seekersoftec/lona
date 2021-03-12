
/**
 * Auth Service
 */
import axios from 'axios';
import { API_URL } from '../config';

const AuthService = {
  login: function (email, password) {
    // var data = {"email":"testemail1@mail.com","password":"123456781"};
    let data = JSON.stringify({ "email": email, "password": password });
    return axios.post(API_URL + '/v1/auth/login', { data });
  },
  register: function (data) {
    return axios.post(API_URL + '/v1/auth/register', { data });
  },
  logout: function () {
    let data = JSON.stringify({ refresh_token: this.getRefreshToken() });

    axios.post(API_URL + '/v1/auth/logout', { headers: this.authHeader(), data });

    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('profile');
  },

  // Loan
  requestLoan: function (data) {
    data["email"] = localStorage.getItem('profile');
    return axios.post(API_URL + '/v1/request_loan', { headers: this.authHeader(), 'Content-Type': 'application/json', data });
  },
  
  payCollateral: function (data) {
    data["email"] = localStorage.getItem('profile');
    data["paid"] = 'True'
    return axios.post(API_URL + '/v1/pay_collateral', { headers: this.authHeader(), 'Content-Type': 'application/json', data  });
  },
  repayLoan: function (data) {
    data["email"] = localStorage.getItem('profile');
    data["paid"] = 'True'
    return axios.post(API_URL + '/v1/repay_loan', { headers: this.authHeader(), 'Content-Type': 'application/json', data  });
  },


  // 
  getProfile: function () {
    let data = JSON.stringify({ "email": localStorage.getItem('profile') })
    return axios.post(API_URL + '/v1/profile', { data });
  },
  saveProfile: function(profile) {
    localStorage.setItem('profile', profile)
  },

  getAccessToken: function () {
    return localStorage.getItem('access_token');
  },
  getRefreshToken: function () {
    return localStorage.getItem('refresh_token');
  },
  saveTokens: function (access_token, refresh_token) {
    localStorage.setItem('access_token', access_token);
    localStorage.setItem('refresh_token', refresh_token);
  },
  authHeader: function () {
    return { Authorization: '' + this.getAccessToken() }
  }
}

export default AuthService
