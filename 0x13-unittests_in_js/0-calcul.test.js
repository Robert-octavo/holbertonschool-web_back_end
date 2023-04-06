const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calcul', () => {
  /* two integers */
  it('should add two numbers', () => {
    assert.equal(calculateNumber(1, 2), 3);
  });

  /* two floats */
  it('should add two floats', () => {
    assert.equal(calculateNumber(1.2, 2.3), 3);
  });

  /* two negatives */
  it('should add two negatives', () => {
    assert.equal(calculateNumber(-1, -2), -3);
  });

  /* one negative */
  it('should add one negative', () => {
    assert.equal(calculateNumber(-1, 2), 1);
  });

  /* one float */
  it('should add one float', () => {
    assert.equal(calculateNumber(1.2, 2), 3);
  });

  /* one float and one negative */
  it('should add one float and one negative', () => {
    assert.equal(calculateNumber(1.2, -2), -1);
  });

  /* zeros */
  it('should add zeros', () => {
    assert.equal(calculateNumber(0, 0), 0);
  });

  /* one zero */
  it('should add one zero', () => {
    assert.equal(calculateNumber(0, 2), 2);
  });
});
