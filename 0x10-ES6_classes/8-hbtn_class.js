/*
Implement a class named HolbertonClass:

  - Constructor attributes:
    - size (Number)
    - location (String)
  - Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
  - When the class is cast into a Number, it should return the size.
  - When the class is cast into a String, it should return the location.
*/

export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(size) {
    if (typeof size === 'number') {
      this._size = size;
    } else {
      throw new TypeError('Size must be a number');
    }
  }

  get location() {
    return this._location;
  }

  set location(location) {
    if (typeof location === 'string') {
      this._location = location;
    } else {
      throw new TypeError('Location must be a string');
    }
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
