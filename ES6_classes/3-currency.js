export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') throw new TypeError('Code must be a string');
    if (typeof name !== 'string') throw new TypeError('Name must be a string');

    this._code = code;
    this._name = name;
  }
  get name() {
    return this._name;
  }
  get code() {
    return this._name;
  }
  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }
  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._code = newCode;
  }
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
