/*
test suite named getPaymentTokenFromAPI

  - How to test the result of getPaymentTokenFromAPI(true)?
  - You should use the done callback to execute this test
*/

const getPaymentTokenFromAPI = require('./6-payment_token');
const chai = require('chai');
const expect = chai.expect;

describe('getPaymentTokenFromAPI', () => {
  it('should return a resolved promise', (done) => {
    getPaymentTokenFromAPI(true).then((result) => {
      expect(result).to.eql({ data: 'Successful response from the API' });
      done();
    });
  });
});
