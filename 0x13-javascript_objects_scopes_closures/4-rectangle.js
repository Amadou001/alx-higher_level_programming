#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && !isNaN(w) && !isNaN(h)) {
      this.width = w;
      this.height = h;
    }
    }
  
    print () {
      let line = '';
      for (let i = 0; i < this.width; i++) {
        line += 'X';
      }
      let count = 0;
      while (count < this.height) {
        console.log(line);
        count++;
      }
    }

    rotate () {
      let temp = this.width;
      this.width = this.height;
      this.height = temp;
    }

    double () {
      this.width *= 2;
      this.height *= 2;
    }
}
module.exports = Rectangle;
  