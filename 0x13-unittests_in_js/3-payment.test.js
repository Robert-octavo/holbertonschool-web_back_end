/*
By using sinon.spy, make sure the math used for sendPaymentRequestToApi(100, 20)
is the same as Utils.calculateNumber('SUM', 100, 20) (validate the usage of
  the Utils function
*/

const Utils = require('./utils');
const assert = require('assert');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');

const spy = sinon.spy(Utils, 'calculateNumber');

//console.log(spy);
sendPaymentRequestToApi(100, 20);
assert.equal(spy.calledOnce, true);
assert.equal(spy.calledWith('SUM', 100, 20), true);

spy.restore();
