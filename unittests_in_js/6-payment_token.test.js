const assert = require('chai').assert;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
  it('should return a successful response when success is true', function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        assert.deepEqual(response, { data: 'Successful response from the API' });
        done(); // Call done to indicate that the test is complete
      })
      .catch(done); // If there is an error, call done with the error
  });

  it('should not return anything when success is false', function (done) {
    getPaymentTokenFromAPI(false)
      .then((response) => {
        assert.isUndefined(response); // No response expected
        done(); // Call done to indicate that the test is complete
      })
      .catch(done); // If there is an error, call done with the error
  });
});
