const assert = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  /* two integers */
  it('should add two numbers', () => {
    assert(calculateNumber('SUM', 1, 2)).to.equal(3);
  });

  it('should subtract two numbers', () => {
    assert(calculateNumber('SUBTRACT', 1, 2)).to.equal(-1);
  });

  it('should divide two numbers', () => {
    assert(calculateNumber('DIVIDE', 1, 2)).to.equal(0.5);
  });

  /* two floats */
  it('should add two floats', () => {
    assert(calculateNumber('SUM', 1.2, 2.3)).to.equal(3);
  });

  it('should subtract two floats', () => {
    assert(calculateNumber('SUBTRACT', 1.2, 2.3)).to.equal(-1);
  });

  it('should divide two floats', () => {
    assert(calculateNumber('DIVIDE', 1.2, 2.3)).to.equal(0.5);
  });

  /* two negatives */
  it('should add two negatives', () => {
    assert(calculateNumber('SUM', -1, -2)).to.equal(-3);
  });

  it('should subtract two negatives', () => {
    assert(calculateNumber('SUBTRACT', -1, -2)).to.equal(1);
  });

  it('should divide two negatives', () => {
    assert(calculateNumber('DIVIDE', -1, -2)).to.equal(0.5);
  });

  /* one negative */
  it('should add one negative', () => {
    assert(calculateNumber('SUM', -1, 2)).to.equal(1);
  });

  it('should subtract one negative', () => {
    assert(calculateNumber('SUBTRACT', -1, 2)).to.equal(-3);
  });

  it('should divide one negative', () => {
    assert(calculateNumber('DIVIDE', -1, 2)).to.equal(-0.5);
  });

  /* one float */
  it('should add one float', () => {
    assert(calculateNumber('SUM', 1.2, 2)).to.equal(3);
  });

  it('should subtract one float', () => {
    assert(calculateNumber('SUBTRACT', 1.2, 2)).to.equal(-1);
  });

  it('should divide one float', () => {
    assert(calculateNumber('DIVIDE', 1.2, 2)).to.equal(0.5);
  });

  /* one float and one negative */
  it('should add one float and one negative', () => {
    assert(calculateNumber('SUM', 1.2, -2)).to.equal(-1);
  });

  it('should subtract one float and one negative', () => {
    assert(calculateNumber('SUBTRACT', 1.2, -2)).to.equal(3);
  });

  it('should divide one float and one negative', () => {
    assert(calculateNumber('DIVIDE', 1.2, -2)).to.equal(-0.5);
  });

  /* zeros */
  it('should add zeros', () => {
    assert(calculateNumber('SUM', 0, 0)).to.equal(0);
  });

  it('should subtract zeros', () => {
    assert(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
  });

  it('should divide zeros', () => {
    assert(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
  });

  /* one zero */
  it('should add one zero', () => {
    assert(calculateNumber('SUM', 0, 2)).to.equal(2);
  });

  it('should subtract one zero', () => {
    assert(calculateNumber('SUBTRACT', 0, 2)).to.equal(-2);
  });

  it('should divide one zero', () => {
    assert(calculateNumber('DIVIDE', 0, 2)).to.equal(0);
  });

  /* one zero */
  it('should divide one zero', () => {
    assert(calculateNumber('DIVIDE', 2, 0)).to.equal('Error');
  });
});
