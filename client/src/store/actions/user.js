import AuthService from "../../services/AuthService";
import { setCurrentUser } from "./actionCreators";

/**
 * Get user profile based on token
 */
export function getProfile() {
  return dispatch => {
    return new Promise((resolve, reject) => {
      const token = AuthService.getAccessToken();
      if (token) {
        AuthService.getProfile().then(resp => {
          if (resp.data.profile) {
            dispatch(setCurrentUser(resp.data.profile));
          }
          resolve();
        });
      } else {
        resolve();
      }
    });
  }
}

/**
 * user loan request based on token
 */
export function requestLoan() {
  return dispatch => {
    return new Promise((resolve, reject) => {
      const token = AuthService.getAccessToken();
      if (token) {
        AuthService.getProfile().then(resp => {
          if (resp.data.profile) {
            dispatch(setCurrentUser(resp.data.profile));
          }
          resolve();
        });
      } else {
        resolve();
      }
    });
  }
}
