const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when given (SUM, 1.4, 4.5)', function () {
      expect(calculateNumber('SUM', 1.function calculateNumber(type, a, b) {
        const roundedA = Math.round(a);
        const roundedB = Math.round(b);
      
        if (type === 'SUM') {
          return roundedA + roundedB;
        } else if (type === 'SUBTRACT') {
          return roundedA - roundedB;
        } else if (type === 'DIVIDE') {
          if (roundedB === 0) {
            return 'Error';
          }
          return roundedA / roundedB;
        } else {
          throw new Error('Invalid operation type');
        }
      }
      
      module.exports = calculateNumber;
      4, 4.5)).to.equal(6);
    });

    it('should return 2 when given (SUM, 1.2, 1.4)', function () {
      expect(calculateNumber('SUM', 1.2, 1.4)).to.equal(2);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when given (SUBTRACT, 1.4, 4.5)', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 0 when given (SUBTRACT, 2.5, 2.5)', function () {
      expect(calculateNumber('SUBTRACT', 2.5, 2.5)).to.equal(0);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when given (DIVIDE, 1.4, 4.5)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when given (DIVIDE, 1.4, 0)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return 5 when given (DIVIDE, 10.2, 2)', function () {
      expect(calculateNumber('DIVIDE', 10.2, 2)).to.equal(5);
    });
  });

  describe('Invalid Operation', function () {
    it('should throw an error when an invalid operation is given', function () {
      expect(() => calculateNumber('MULTIPLY', 2, 3)).to.throw(Error);
    });
  });
});
