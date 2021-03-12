import { SET_CURRENT_USER, REGISTER_SUCCESS, REQUEST_LOAN_SUCCESS, PAY_COLLATERAL_SUCCESS, REPAY_LOAN_SUCCESS, LOGOUT, GET_ERRORS } from "./types";

export function setCurrentUser(user) {
  return {
    type: SET_CURRENT_USER,
    payload: user
  }
}

export function registerSuccess() {
  return {
    type: REGISTER_SUCCESS
  }
}

export function requestLoanSuccess(payload) {
  return {
    type: REQUEST_LOAN_SUCCESS,
    payload: payload
  }
}

export function payCollateralSuccess(payload) {
  return {
    type: PAY_COLLATERAL_SUCCESS,
    payload: payload
  }
}

export function repayLoanSuccess(payload) {
  return {
    type: REPAY_LOAN_SUCCESS,
    payload: payload
  }
}


export function logoutUser() {
  return {
    type: LOGOUT
  }
}

export function getErrors(errors) {
  return {
    type: GET_ERRORS,
    payload: errors
  }
}
