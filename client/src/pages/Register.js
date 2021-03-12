import React, { Component } from 'react'
import {
  Button, Form, Grid, Header, Image, Message,
  Segment, Loader
} from 'semantic-ui-react'
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import validateInput from '../validators/register';
import { registerUser } from '../store/actions/auth';

class RegisterForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      firstname: '',
      lastname: '',
      email: '',
      password_1: '',
      password_2: '', // confirm password
      nin_number: '',
      bvn_number: '',
      user_bank_name: '',
      bank_account_number: '',
      eth_address: '',
      business_info: '',
      errors: {},
      isLoading: false
    };
  }

  onSubmit = (e) => {
    e.preventDefault();
    if (this.isValid()) {
      this.setState({ errors: {}, isLoading: true });
      this.props.registerUser(this.state, this.props.history);
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
      firstname,
      lastname,
      email,
      password_1,
      password_2,
      user_bank_name,
      nin_number,
      bvn_number,
      bank_account_number,
      eth_address,
      business_info,
      errors,
      isLoading
    } = this.state;

    return (
      <div className="register-form">
        <Grid textAlign='center' style={{ height: '100%' }} verticalAlign='middle'>
          <Grid.Column style={{ maxWidth: 450 }}>

            <Link to='/'>
              <Image src='/assets/images/logo.png' size='tiny' centered />
            </Link>

            <Header as='h2' color='teal' textAlign='center'>
              Register
            </Header>

            <Form 
              size='large'
              onSubmit={this.onSubmit}
              error={errors.registerError ? true : false}
              autoComplete='on'
            >
              <Segment stacked>
                <Form.Input
                  fluid
                  placeholder='First Name'
                  name='firstname'
                  defaultValue={firstname}
                  error={errors.firstname ? true : false}
                  onChange={this.onChange}
                />
                <Form.Input
                  fluid
                  placeholder='Last Name'
                  name='lastname'
                  defaultValue={lastname}
                  error={errors.lastname ? true : false}
                  onChange={this.onChange}
                />
                <Form.Input
                  fluid
                  placeholder='E-mail'
                  name='email'
                  defaultValue={email}
                  error={errors.email ? true : false}
                  onChange={this.onChange}
                />
                <Form.Input
                  fluid
                  placeholder='Password [8 characters minimum]'
                  name='password_1'
                  type='password'
                  pattern=".{8,}"
                  defaultValue={password_1}
                  error={errors.password_1 ? true : false}
                  onChange={this.onChange}
                />
                <Form.Input
                  fluid
                  placeholder='Confirm Password [8 characters minimum]'
                  name='password_2'
                  type='password'
                  pattern=".{8,}"
                  defaultValue={password_2}
                  error={errors.password_2 ? true : false}
                  onChange={this.onChange}
                />

                <select
                  fluid
                  name="user_bank_name"
                  onChange={this.onChange}
                  defaultValue={user_bank_name}
                  error={errors.user_bank_name ? true : false}
                >
                  <option selected>Bank name</option>
                  <option value="access">Access Bank</option>
                  <option value="citibank">Citibank</option>
                  <option value="diamond">Diamond Bank</option>
                  <option value="ecobank">Ecobank</option>
                  <option value="fidelity">Fidelity Bank</option>
                  <option value="fcmb">First City Monument Bank (FCMB)</option>
                  <option value="fsdh">FSDH Merchant Bank</option>
                  <option value="gtb">Guarantee Trust Bank (GTB)</option>
                  <option value="heritage">Heritage Bank</option>
                  <option value="Keystone">Keystone Bank</option>
                  <option value="rand">Rand Merchant Bank</option>
                  <option value="skye">Skye Bank</option>
                  <option value="stanbic">Stanbic IBTC Bank</option>
                  <option value="standard">Standard Chartered Bank</option>
                  <option value="sterling">Sterling Bank</option>
                  <option value="suntrust">Suntrust Bank</option>
                  <option value="union">Union Bank</option>
                  <option value="uba">United Bank for Africa (UBA)</option>
                  <option value="unity">Unity Bank</option>
                  <option value="wema">Wema Bank</option>
                  <option value="zenith">Zenith Bank</option>
                </select>
                <br />
                <Form.Input
                  fluid
                  placeholder="National Identity Number [min 11 numbers]"
                  name="nin_number"
                  pattern=".{11,11}"
                  defaultValue={nin_number}
                  error={errors.nin_number ? true : false}
                  onChange={this.onChange}
                />
                <Form.Input
                  fluid
                  placeholder="Bank Verification Number [min 11 numbers]"
                  name="bvn_number"
                  pattern=".{11,11}"
                  defaultValue={bvn_number}
                  error={errors.bvn_number ? true : false}
                  onChange={this.onChange}
                />
                <Form.Input
                  fluid
                  placeholder="Bank Account Number [min 10 numbers]"
                  name="bank_account_number"
                  pattern=".{10,10}"
                  defaultValue={bank_account_number}
                  error={errors.bank_account_number ? true : false}
                  onChange={this.onChange}
                />
                <Form.Input
                  fluid
                  placeholder="Ethereum Address"
                  name="eth_address"
                  pattern=".{42,42}"
                  defaultValue={eth_address}
                  error={errors.eth_address ? true : false}
                  onChange={this.onChange}
                />
                <Form.Input 
                  fluid
                  placeholder="About Business" 
                  name="business_info"
                  defaultValue={business_info}
                  onChange={this.onChange}
                />

                <Message error content={errors.registerError} />

                <Button color='teal' fluid size='large' disabled={isLoading}>
                  {!isLoading
                    ? 'Register'
                    : <Loader active inverted inline size='small' />
                  }
                </Button>
              </Segment>
            </Form>

            <Message>
              Already have an account? <Link to='/login'>Login</Link>
            </Message>

          </Grid.Column>
        </Grid>
      </div >
    )
  }
}

RegisterForm.propTypes = {
  errors: PropTypes.object.isRequired
}

const mapStateToProps = (state) => ({
  errors: state.errors
})

export default connect(mapStateToProps, { registerUser })(RegisterForm)
