const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  /* two integers */
  it('should add two numbers', () => {
    expect(calculateNumber('SUM', 1, 2)).to.equal(3);
  });

  it('should subtract two numbers', () => {
    expect(calculateNumber('SUBTRACT', 1, 2)).to.equal(-1);
  });

  it('should divide two numbers', () => {
    expect(calculateNumber('DIVIDE', 1, 2)).to.equal(0.5);
  });

  /* two floats */
  it('should add two floats', () => {
    expect(calculateNumber('SUM', 1.2, 2.3)).to.equal(3);
  });

  it('should subtract two floats', () => {
    expect(calculateNumber('SUBTRACT', 1.2, 2.3)).to.equal(-1);
  });

  it('should divide two floats', () => {
    expect(calculateNumber('DIVIDE', 1.2, 2.3)).to.equal(0.5);
  });

  /* two negatives */
  it('should add two negatives', () => {
    expect(calculateNumber('SUM', -1, -2)).to.equal(-3);
  });

  it('should subtract two negatives', () => {
    expect(calculateNumber('SUBTRACT', -1, -2)).to.equal(1);
  });

  it('should divide two negatives', () => {
    expect(calculateNumber('DIVIDE', -1, -2)).to.equal(0.5);
  });

  /* one negative */
  it('should add one negative', () => {
    expect(calculateNumber('SUM', -1, 2)).to.equal(1);
  });

  it('should subtract one negative', () => {
    expect(calculateNumber('SUBTRACT', -1, 2)).to.equal(-3);
  });

  it('should divide one negative', () => {
    expect(calculateNumber('DIVIDE', -1, 2)).to.equal(-0.5);
  });

  /* one float */
  it('should add one float', () => {
    expect(calculateNumber('SUM', 1.2, 2)).to.equal(3);
  });

  it('should subtract one float', () => {
    expect(calculateNumber('SUBTRACT', 1.2, 2)).to.equal(-1);
  });

  it('should divide one float', () => {
    expect(calculateNumber('DIVIDE', 1.2, 2)).to.equal(0.5);
  });

  /* one float and one negative */
  it('should add one float and one negative', () => {
    expect(calculateNumber('SUM', 1.2, -2)).to.equal(-1);
  });

  it('should subtract one float and one negative', () => {
    expect(calculateNumber('SUBTRACT', 1.2, -2)).to.equal(3);
  });

  it('should divide one float and one negative', () => {
    expect(calculateNumber('DIVIDE', 1.2, -2)).to.equal(-0.5);
  });

  /* zeros */
  it('should add zeros', () => {
    expect(calculateNumber('SUM', 0, 0)).to.equal(0);
  });

  it('should subtract zeros', () => {
    expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
  });

  it('should divide zeros', () => {
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
  });

  /* one zero */
  it('should add one zero', () => {
    expect(calculateNumber('SUM', 0, 2)).to.equal(2);
  });

  it('should subtract one zero', () => {
    expect(calculateNumber('SUBTRACT', 0, 2)).to.equal(-2);
  });

  it('should divide one zero', () => {
    expect(calculateNumber('DIVIDE', 0, 2)).to.equal(0);
  });

  /* one zero */
  it('should divide one zero', () => {
    expect(calculateNumber('DIVIDE', 2, 0)).to.equal('Error');
  });
});
