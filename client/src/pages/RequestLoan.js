import React, { Component } from 'react'
import {
  Button, Form, Grid, Header, Message,
  Segment, Loader
} from 'semantic-ui-react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import Main from './Main';

import validateInput from '../validators/requestLoan';
import { requestLoan } from '../store/actions/auth';

class RequestLoan extends Component {
  constructor(props) {
    super(props);
    this.state = {
      amount: '',
      loan_expire_date: '6',
      errors: {},
      isLoading: false
    };
  }

  onSubmit = (e) => {
    e.preventDefault();
    if (this.isValid()) {
      this.setState({ errors: {}, isLoading: true });
      this.props.requestLoan(this.state, this.props.history);
    }
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  }

  isValid = () => {
    const { errors, isValid } = validateInput(this.state);
    if (!isValid) {
      this.setState({ errors });
    }
    return isValid;
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.errors) {
      this.setState({
        errors: nextProps.errors,
        isLoading: false
      });
    }
  }

  render() {
    const {
      amount,
      loan_expire_date,
      errors,
      isLoading
    } = this.state;

    return (
      <Main>
        <div className="register-form">
          <Grid textAlign='center' style={{ height: '100%' }} verticalAlign='middle'>
            <Grid.Column style={{ maxWidth: 350 }}>

              <Header as='h4' color='teal' textAlign='center'>
                Request loan
            </Header>

              <Form size='large'
                onSubmit={this.onSubmit}
                error={errors.requestLoanError ? true : false}
                autoComplete='off'
              >
                <Segment stacked>
                  <Form.Input
                    fluid
                    type="number"
                    min="0"
                    placeholder='Loan Amount'
                    name='amount'
                    defaultValue={amount}
                    error={errors.amount ? true : false}
                    onChange={this.onChange}
                  />

                  <select
                    fluid
                    name="loan_expire_date"
                    onChange={this.onChange}
                    defaultValue={loan_expire_date}
                    error={errors.loan_expire_date ? true : false}
                  >
                    <option value="6">6 months</option>
                    <option value="7">7 months</option>
                    <option value="8">8 months</option>
                    <option value="9">9 months</option>
                    <option value="10">10 months</option>
                    <option value="11">11 months</option>
                    <option value="12">12 months</option>
                    <option value="13">13 months</option>
                    <option value="14">14 months</option>
                    <option value="15">15 months</option>
                    <option value="16">16 months</option>
                    <option value="17">17 months</option>
                    <option value="18">18 months</option>
                    <option value="19">19 months</option>
                    <option value="20">20 months</option>
                    <option value="21">21 months</option>
                    <option value="22">22 months</option>
                    <option value="23">23 months</option>
                    <option value="24">24 months</option>
                  </select>
                  <br />
                  <Message error content={errors.requestLoanError} />

                  <Button color='teal' fluid size='large' disabled={isLoading}>
                    {!isLoading
                      ? 'Request'
                      : <Loader active inverted inline size='small' />
                    }
                  </Button>
                </Segment>
              </Form>

            </Grid.Column>
          </Grid>
        </div >
      </Main>

    )
  }
}

RequestLoan.propTypes = {
  errors: PropTypes.object.isRequired
}

const mapStateToProps = (state) => ({
  errors: state.errors
})

export default connect(mapStateToProps, { requestLoan })(RequestLoan)
