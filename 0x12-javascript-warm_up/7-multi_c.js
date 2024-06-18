#!/usr/bin/node
const array = process.argv.slice(2);
const value = parseInt(array[0]);
if (value) {
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
