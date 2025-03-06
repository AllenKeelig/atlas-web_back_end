const Utils = {
  calculateNumber: function(type, a, b) {
    const A = Math.round(a);
    const B = Math.round(b);
    const typeUppercase = type.toUpperCase();

    switch (typeUppercase) {
      case 'SUM':
        return (A + B);
      case 'SUBTRACT':
        return (A - B);
      case 'DIVIDE':
        if (B === 0) {
          return 'Error';
        } else {
          return (A / B);
        }
      default:
        return;
    }
  }
}

module.exports = Utils;