#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (x, size) {
    super(x, x, size, size);
    this.size = x;
  }

  charPrint (c) {
    if (!c) {
      let p = '';
      for (let i = 0; i < this.size; i++) {
        p += 'X';
      }
      for (let i = 0; i < this.size; i++) {
        console.log(p);
      }
    } else {
      let s = c;
      for (let i = 0; i < this.size; i++) {
        s += c;
      }
      for (let i = 0; i < this.size; i++) {
        console.log(s);
      }
    }
  }
};
