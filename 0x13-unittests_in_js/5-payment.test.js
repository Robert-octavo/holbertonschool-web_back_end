/*
  - Inside the same describe, create 2 tests:
    - The first test will call sendPaymentRequestToAPI with 100, and 20:
      - Verify that the console is logging the string The total is: 120
      - Verify that the console is only called once
    - The second test will call sendPaymentRequestToAPI with 10, and 10:
      - Verify that the console is logging the string The total is: 20
      - Verify that the console is only called once

Requirements:

  - You should be able to run the test suite using npm test 5-payment.test.js
  - Every test should pass without any warning
  - You should use only one spy to complete this exercise
  - You should use a beforeEach and a afterEach hooks to complete this exercise
*/

const Utils = require('./utils');
const assert = require('assert');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let spy;
  beforeEach(() => {
    spy = sinon.spy(console, 'log');
  });
  afterEach(() => {
    spy.restore();
  });
  it('should log the correct message with 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);
    assert.equal(spy.calledOnce, true);
    assert.equal(spy.calledWith('The total is: 120'), true);
  });
  it('should log the correct message with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);
    assert.equal(spy.calledOnce, true);
    assert.equal(spy.calledWith('The total is: 20'), true);
  });
}
);
