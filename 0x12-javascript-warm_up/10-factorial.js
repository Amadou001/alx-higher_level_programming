#!/usr/bin/node
const args = process.argv.slice(2);
const value = parseInt(args[0]);
function factorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
console.log(factorial(value));
