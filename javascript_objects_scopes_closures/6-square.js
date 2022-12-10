#!/usr/bin/node

const Ssquare = require('./5-square');

module.exports = class Square extends Ssquare {
  constructor (x, size) {
    super(x, x, size, size);
    this.size = x;
  }

  charPrint (c = 'X') {
    let s = '';
    for (let i = 0; i <= this.size; i++) {
      s += c;
    }
    for (let i = 0; i <= this.size; i++) {
      console.log(s);
    }
  }
};
