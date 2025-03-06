// 6-payment_token.js
function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({
      data: 'Successful response from the API'
    });
  }

  return;
}

module.exports = getPaymentTokenFromAPI;
