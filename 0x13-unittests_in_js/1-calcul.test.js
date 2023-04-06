const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calcul', () => {
  /* two integers */
  it('should add two numbers', () => {
    assert.equal(calculateNumber('SUM', 1, 2), 3);
  });

  it('should subtract two numbers', () => {
    assert.equal(calculateNumber('SUBTRACT', 1, 2), -1);
  });

  it('should divide two numbers', () => {
    assert.equal(calculateNumber('DIVIDE', 1, 2), 0.5);
  });

  /* two floats */
  it('should add two floats', () => {
    assert.equal(calculateNumber('SUM', 1.2, 2.3), 3);
  });

  it('should subtract two floats', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.2, 2.3), -1);
  });

  it('should divide two floats', () => {
    assert.equal(calculateNumber('DIVIDE', 1.2, 2.3), 0.5);
  });

  /* two negatives */
  it('should add two negatives', () => {
    assert.equal(calculateNumber('SUM', -1, -2), -3);
  });

  it('should subtract two negatives', () => {
    assert.equal(calculateNumber('SUBTRACT', -1, -2), 1);
  });

  it('should divide two negatives', () => {
    assert.equal(calculateNumber('DIVIDE', -1, -2), 0.5);
  });

  /* one negative */
  it('should add one negative', () => {
    assert.equal(calculateNumber('SUM', -1, 2), 1);
  });

  it('should subtract one negative', () => {
    assert.equal(calculateNumber('SUBTRACT', -1, 2), -3);
  });

  it('should divide one negative', () => {
    assert.equal(calculateNumber('DIVIDE', -1, 2), -0.5);
  });

  /* one float */
  it('should add one float', () => {
    assert.equal(calculateNumber('SUM', 1.2, 2), 3);
  });

  it('should subtract one float', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.2, 2), -1);
  });

  it('should divide one float', () => {
    assert.equal(calculateNumber('DIVIDE', 1.2, 2), 0.5);
  });

  /* one float and one negative */
  it('should add one float and one negative', () => {
    assert.equal(calculateNumber('SUM', 1.2, -2), -1);
  });

  it('should subtract one float and one negative', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.2, -2), 3);
  });

  it('should divide one float and one negative', () => {
    assert.equal(calculateNumber('DIVIDE', 1.2, -2), -0.5);
  });

  /* zeros */
  it('should add zeros', () => {
    assert.equal(calculateNumber('SUM', 0, 0), 0);
  });

  it('should subtract zeros', () => {
    assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
  });

  it('should divide zeros', () => {
    assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
  });

  /* one zero */
  it('should add one zero', () => {
    assert.equal(calculateNumber('SUM', 0, 2), 2);
  });

  it('should subtract one zero', () => {
    assert.equal(calculateNumber('SUBTRACT', 0, 2), -2);
  });

  it('should divide one zero', () => {
    assert.equal(calculateNumber('DIVIDE', 0, 2), 0);
  });

  /* one zero */
  it('should divide one zero', () => {
    assert.equal(calculateNumber('DIVIDE', 2, 0), 'Error');
  });
});
