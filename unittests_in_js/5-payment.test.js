// 5-payment.test.js
const sinon = require('sinon');
const assert = require('chai').assert;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function () {
  let spy;
  beforeEach(function () {
    spy = sinon.spy(console, 'log');
  });
  afterEach(function () {
    spy.restore();
  });

  it('should log the correct message when given 100 and 20', function () {
    sendPaymentRequestToApi(100, 20);
    assert.isTrue(spy.calledWith('The total is: 120'), 'console.log should log "The total is: 120"');
    assert.strictEqual(spy.callCount, 1, 'console.log should be called only once');
  });
  it('should log the correct message when given 10 and 10', function () {
    sendPaymentRequestToApi(10, 10);
    assert.isTrue(spy.calledWith('The total is: 20'), 'console.log should log "The total is: 20"');
    assert.strictEqual(spy.callCount, 1, 'console.log should be called only once');
  });
});
