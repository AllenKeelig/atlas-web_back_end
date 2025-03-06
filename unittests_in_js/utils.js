const Utils = {
    calculateNumber: function (type, a, b) {
      if (type === 'SUM') {
        return Math.round(a) + Math.round(b);
      }
      if (type === 'SUBTRACT') {
        return Math.round(a) - Math.round(b);
      }
      if (type === 'DIVIDE') {
        if (b === 0) return 'Error';
        return Math.round(a) / Math.round(b);
      }
      return 'Invalid Operation';
    }
  };
  
  module.exports = Utils;