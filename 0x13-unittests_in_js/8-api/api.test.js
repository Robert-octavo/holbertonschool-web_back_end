/*
Create one suite for the index page:

  - Correct status code?
  - Correct result?
  - Other?
*/

const chai = require('chai');
const expect = chai.expect;
const request = require('request');

describe('Index page', () => {
  it('should return 200', (done) => {
    request('http://localhost:7865', (err, res) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });
  it('should return the correct result', (done) => {
    request('http://localhost:7865', (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
