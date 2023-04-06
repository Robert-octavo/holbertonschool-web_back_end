/*
  - Add a new endpoint: GET /cart/:id
  - :id must be only a number (validation must be in the route definition)
  - When access, the endpoint should return Payment methods for cart :id
*/

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`);
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});
