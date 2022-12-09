#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h, width, height) {
    if ((w !== 0 && w > 0) && (h !== 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rec = '';
    for (let i = 0; i < this.width; i++) {
      rec += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(rec);
    }
  }

  rotate () {
    const sup = this.width;
    this.width = this.height;
    this.height = sup;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
