import Validator from 'validator';
import isEmpty from 'lodash/isEmpty';
import { REQUIRED } from "./messages";

export default function validateInput(data) {
  let errors = {};

  if (Validator.isEmpty(data.firstname)) {
    errors.firstname = REQUIRED;
  }

  if (Validator.isEmpty(data.lastname)) {
    errors.lastname = REQUIRED;
  }

  if (Validator.isEmpty(data.email)) {
    errors.email = REQUIRED;
  }

  if (Validator.isEmpty(data.password_1)) {
    errors.password_1 = REQUIRED;
  }

  if (Validator.isEmpty(data.password_2)) {
    errors.password_2 = REQUIRED;
  }

  if (Validator.isEmpty(data.user_bank_name)) {
    errors.user_bank_name = REQUIRED;
  }

  if (Validator.isEmpty(data.bvn_number)) {
    errors.bvn_number = REQUIRED;
  }

  if (Validator.isEmpty(data.nin_number)) {
    errors.nin_number = REQUIRED;
  }

  if (Validator.isEmpty(data.bank_account_number)) {
    errors.bank_account_number = REQUIRED;
  }

  if (Validator.isEmpty(data.eth_address)) {
    errors.eth_address = REQUIRED;
  }

  // if (Validator.isEmpty(data.business_info)) {
  //   errors.business_info = REQUIRED;
  // }

  return {
    errors,
    isValid: isEmpty(errors)
  }
}
