#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
