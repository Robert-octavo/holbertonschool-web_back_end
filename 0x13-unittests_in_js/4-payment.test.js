/*
Stub the function Utils.calculateNumber to always return the same number 10
Verify that the stub is being called with type = SUM, a = 100, and b = 20
Add a spy to verify that console.log is logging the correct message The total is: 10
*/
const Utils = require('./utils');
const assert = require('assert');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');

const spy = sinon.spy(console, 'log');
const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

sendPaymentRequestToApi(100, 20);
assert.equal(stub.calledOnce, true);
assert.equal(stub.calledWith('SUM', 100, 20), true);
assert.equal(spy.calledOnce, true);
assert.equal(spy.calledWith('The total is: 10'), true);

stub.restore();
spy.restore();
