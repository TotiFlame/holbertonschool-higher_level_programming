#!/usr/bin/node

const Ssquare = require('./5-square');

module.exports = class Square extends Ssquare {
  charPrint (c = 'X') {
    let s = '';
    for (let i = 0; i < this.height; i++) {
      s += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(s);
    }
  }
};
