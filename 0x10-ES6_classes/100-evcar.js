/*
Import Car from 10-car.js.

Implement a class named EVCar that extends the Car class:

  - Constructor attributes:
      - brand (String)
      - motor (String)
      - color (String)
      - range (String)
  - Each attribute must be stored in an “underscore” attribute version
  (ex: name is stored in _name)
  - For privacy reasons, when cloneCar is called on a EVCar object,
  the object returned should be an instance of Car instead of EVCar.
*/

import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  get range() {
    return this._range;
  }

  set range(range) {
    if (typeof range === 'number') {
      this._range = range;
    } else {
      throw new TypeError('Range must be a number');
    }
  }

  static get [Symbol.species]() {
    return Car;
  }
}
