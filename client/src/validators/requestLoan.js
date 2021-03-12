import Validator from 'validator';
import isEmpty from 'lodash/isEmpty';
import { REQUIRED } from "./messages";

export default function validateInput(data) {
  let errors = {};

  if (Validator.isEmpty(data.amount)) {
    errors.amount = REQUIRED;
  }

  if (Validator.isEmpty(data.loan_expire_date)) {
    errors.loan_expire_date = REQUIRED;
  }

  return {
    errors,
    isValid: isEmpty(errors)
  }
}
