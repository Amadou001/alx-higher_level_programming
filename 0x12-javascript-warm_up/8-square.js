#!/usr/bin/node
const array = process.argv.slice(2);
let value = parseInt(array[0]);
let square = '';
if (value) {
  for (let i = 0; i < value; i++) {
    square += 'X';
  }
} else {
  console.log('Missing size');
}
while (value > 0) {
  console.log(square);
  value--;
}
