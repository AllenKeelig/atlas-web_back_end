const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when given (SUM, 1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 3 when given (SUM, 1.2, 1.4)', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 1.4), 3);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when given (SUBTRACT, 1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 0 when given (SUBTRACT, 2.5, 2.5)', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.5, 2.5), 0);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when given (DIVIDE, 1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when given (DIVIDE, 1.4, 0)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return 5 when given (DIVIDE, 10.2, 2)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 10.2, 2), 5);
    });
  });

  describe('Invalid Operation', function () {
    it('should throw an error when an invalid operation is given', function () {
      assert.throws(() => calculateNumber('MULTIPLY', 2, 3), Error);
    });
  });
});
