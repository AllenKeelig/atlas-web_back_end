// Import necessary libraries
const request = require('supertest');
const { expect } = require('chai');
const app = require('./app'); // Assuming your Express app is in 'app.js'

describe('Index Page', () => {
  // Test case 1: Correct status code
  it('should return status code 200', async () => {
    const response = await request(app).get('/');
    expect(response.status).to.equal(200);
  });

  // Test case 2: Correct result (message)
  it('should return the correct message', async () => {
    const response = await request(app).get('/');
    expect(response.text).to.equal('Welcome to the payment system');
  });

  // Test case 3: Other checks (e.g., content type)
  it('should return content type text/html', async () => {
    const response = await request(app).get('/');
    expect(response.header['content-type']).to.include('text/html');
  });
});
