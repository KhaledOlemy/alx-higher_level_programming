#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    let z;
    if (c === undefined) {
      z = 'X';
    } else {
      z = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(z.repeat(this.width));
    }
  }
}
module.exports = Square;
