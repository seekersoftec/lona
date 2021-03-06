import React, { Component } from 'react'
import {
  Button, Form, Grid, Header, Message,
  Segment, Loader
} from 'semantic-ui-react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import Main from './Main';

import validateInput from '../validators/payCollateral';
import { payCollateral } from '../store/actions/auth';

class PayCollateral extends Component {
  constructor(props) {
    super(props);
    this.state = {
      amount: '',
      errors: {},
      isLoading: false
    };
  }

  onSubmit = (e) => {
    e.preventDefault();
    if (this.isValid()) {
      this.setState({ errors: {}, isLoading: true });
      this.props.payCollateral(this.state, this.props.history);
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
      errors,
      isLoading
    } = this.state;

    return (
      <Main>
        <div className="register-form">
          <Grid textAlign='center' style={{ height: '100%' }} verticalAlign='middle'>
            <Grid.Column style={{ maxWidth: 350 }}>

              <Header as='h4' color='teal' textAlign='center'>
                Pay collateral
            </Header>

              <Form size='large'
                onSubmit={this.onSubmit}
                error={errors.PayCollateralError ? true : false}
                autoComplete='off'
              >
                <Segment stacked>
                  <Form.Input
                    fluid
                    type="number"
                    min="0"
                    placeholder='Collateral Amount'
                    name='amount'
                    defaultValue={amount}
                    error={errors.amount ? true : false}
                    onChange={this.onChange}
                  />
                  <br />
                  <Message error content={errors.payCollateralError} />

                  <Button color='teal' fluid size='large' disabled={isLoading}>
                    {!isLoading
                      ? 'Pay'
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

payCollateral.propTypes = {
  errors: PropTypes.object.isRequired
}

const mapStateToProps = (state) => ({
  errors: state.errors
})

export default connect(mapStateToProps, { payCollateral })(PayCollateral)
