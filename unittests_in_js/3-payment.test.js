// 3-payment.test.js
const sinon = require('sinon');
const assert = require('chai').assert;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with correct arguments', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');  // Create a spy for Utils.calculateNumber

    sendPaymentRequestToApi(100, 20);  // Call the function that uses calculateNumber

    // Check that the spy was called with the correct arguments
    assert.isTrue(spy.calledWith('SUM', 100, 20), 'Utils.calculateNumber should be called with correct arguments');
    
    spy.restore();  // Restore the original method to avoid side effects
  });
});
