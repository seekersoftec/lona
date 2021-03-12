import AuthService from '../../services/AuthService';
import { setCurrentUser, registerSuccess, requestLoanSuccess, payCollateralSuccess, repayLoanSuccess, logoutUser, getErrors } from "./actionCreators";

/**
 * Login user action
 */
export const loginUser = (state, history) => dispatch => {
  AuthService.login(state.email, state.password).then(resp => {
    if ('access_token' in resp.data) {
      dispatch(setCurrentUser(resp.data.profile));
      AuthService.saveProfile(resp.data.profile.email);
      AuthService.saveTokens(resp.data.access_token,resp.data.refresh_token);
      history.push('/');
    }
  }).catch(error => {
    if (error.response) {
      dispatch(getErrors({
        loginError: error.response.data.message
      }));
    }
  });
}

/**
 * Logout action
 */
export const logout = (history) => dispatch => {
  AuthService.logout();
  dispatch(logoutUser());
  history.push('/')
  window.location.reload();
}

/**
 * Register user action
 */
export const registerUser = (data, history) => dispatch => {
  AuthService.register(data).then(resp => {
    if (resp.data.success) {
      dispatch(registerSuccess());
      history.push('/login');
    }
  }).catch(error => {
    if (error.response) {
      dispatch(getErrors({
        registerError: error.response.data.message
      }));
    }
  });
}


/**
 * Request loan 
 */
export const requestLoan = (data, history) => dispatch => {
  AuthService.requestLoan(data).then(resp => {
    if (resp.data) {
      dispatch(requestLoanSuccess({
        requestLoanSuccess: resp.data
      }));
      history.push('/pay-collateral');
    }
  }).catch(error => {
    if (error.response) {
      dispatch(getErrors({
        requestLoanError: error.response.data.message
      }));
    }
  });
}

/**
 * Pay collateral
 */
export const payCollateral = (data, history) => dispatch => {
  AuthService.payCollateral(data).then(resp => {
    if (resp.data) {
      dispatch(payCollateralSuccess({
        payCollateralSuccess: resp.data
      }));
      history.push('/');
    }
  }).catch(error => {
    if (error.response) {
      dispatch(getErrors({
        payCollateralError: error.response.data.message
      }));
    }
  });
}

/**
 * Repay Loan
 */
export const repayLoan = (data, history) => dispatch => {
  AuthService.repayLoan(data).then(resp => {
    if (resp.data) {
      dispatch(repayLoanSuccess({
        repayLoanSuccess: resp.data.message
      }));
      history.push('/');
    }
  }).catch(error => {
    if (error.response) {
      dispatch(getErrors({
        repayLoanError: error.response.data.message
      }));
    }
  });
}