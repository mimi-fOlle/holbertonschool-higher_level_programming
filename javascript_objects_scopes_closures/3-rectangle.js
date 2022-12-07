#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Instance method
  print () {
    for (let i = 0; i <= this.height; i++) {
      let row = '';
      for (let j = 0; j <= this.width - 1; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
