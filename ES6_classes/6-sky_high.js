import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Floors must be a number');
    }
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
