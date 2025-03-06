const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
describe('Payment tests', () => {
  it('Check that Utils is called correctly, with stub', () => {
    const stub = sinon.stub(Utils, 'calculateNumber').callsFake(() => 10);
    const spy = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledWithExactly(spy, 'The total is: 10');
    spy.restore();
  });
});
