import React from 'react';
import Main from './Main';
import { Link } from 'react-router-dom';
import { Image } from 'semantic-ui-react'

const HomePage = () => (
  <Main>
    <Link to='/'>
      <Image src='/assets/images/logo200.png' size='tiny' centered />
    </Link>
    {/* <h4>Usage(Step by Step Process):</h4> */}
    <p>
      Note: notifications are sent directly to your mail
    </p>
  </Main>
)

export default HomePage;
