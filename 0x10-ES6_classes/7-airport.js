/*
Implement a class named Airport:

  - Constructor attributes:
    - name (String)
    - code (String)
  - Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
  - The default string description of the class should return the airport code (example below).
*/

export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  set code(code) {
    if (typeof code === 'string') {
      this._code = code;
    } else {
      throw new TypeError('Code must be a string');
    }
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }
}
