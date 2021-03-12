const jsonServer = require('json-server')
const server = jsonServer.create()
const middlewares = jsonServer.defaults()

server.use(jsonServer.bodyParser);
server.use(middlewares);

const testUser = {
  email: 'feyyaz@test.com',
  password: '1234'
};

const testProfile = {
  email: 'feyyaz@test.com',
  firstName: 'Feyyaz',
  lastName: 'Akkuş'
};

const testToken = 'example-token';

const authUser = (req) => {
  return req.body.email === testUser.email && req.body.password === testUser.password;
}

server.post('/v1/auth/login', (req, res) => {
  if (authUser(req)) {
    res.status(200).json({
      success: true,
      token: testToken,
      profile: testProfile
    });
  } else {
    res.status(401).json({
      success: false,
      error: 'Email or password incorrect'
    });
  }
});

server.post('/v1/auth/register', (req, res) => {
  res.status(200).json({
    success: true
  });
});

server.get('/v1/profile', (req, res) => {
  console.log(req.headers);
  res.status(200).json({
    success: true,
    profile: testProfile
  });
});

server.post('/v1/request-loan', (req, res) => {
  console.log(req.headers);
  if (authUser(req)) {
    res.status(200).json({
      success: true,
      token: testToken,
      profile: testProfile
    });
  } else {
    res.status(401).json({
      success: false,
      error: 'Email or password incorrect'
    });
  }
});

server.get('/v1/pay-collateral', (req, res) => {
  console.log(req.headers);
  res.status(200).json({
    success: true,
    profile: testProfile
  });
});

server.get('/v1/repay-loan', (req, res) => {
  console.log(req.headers);
  res.status(200).json({
    success: true,
    profile: testProfile
  });
});

server.listen(5000, () => {
  console.log('JSON Server is running..');
});
