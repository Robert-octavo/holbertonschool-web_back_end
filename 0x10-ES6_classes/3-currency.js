/*
Implement a class named Currency:

    - Constructor attributes:
      - code (String)
      - name (String)
    - Each attribute must be stored in an “underscore” attribute version
    (ex: name is stored in _name)
    - Implement a getter and setter for each attribute.
    - Implement a method named displayFullCurrency that will return the
    attributes in the following format name (code).
*/

export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code === 'string') {
      this._code = code;
    } else {
      throw new TypeError('Code must be a string');
    }
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
