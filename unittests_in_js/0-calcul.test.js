const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('should return 4 when given (1, 3)', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return 5 when given (1, 3.7)', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return 5 when given (1.2, 3.7)', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return 6 when given (1.5, 3.7)', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should return 0 when given (0.4, 0.4)', function () {
    assert.strictEqual(calculateNumber(0.4, 0.4), 0);
  });

  it('should return 2 when given (0.6, 0.6)', function () {
    assert.strictEqual(calculateNumber(0.6, 0.6), 2);
  });

  it('should return -2 when given (-0.6, -0.6)', function () {
    assert.strictEqual(calculateNumber(-0.6, -0.6), -2);
  });

  it('should return 1 when given (0.4, 0.6)', function () {
    assert.strictEqual(calculateNumber(0.4, 0.6), 1);
  });
});
