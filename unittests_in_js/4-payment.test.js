
const sinon = require('sinon');
const assert = require('chai').assert;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with correct arguments', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    assert.isTrue(spy.calledWith('SUM', 100, 20), 'Utils.calculateNumber should be called with correct arguments');
    spy.restore();
  });
});
