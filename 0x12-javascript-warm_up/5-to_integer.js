#!/usr/bin/node
const args = process.argv.slice(2);
const value = parseInt(args[0]);
if (value) {
  console.log(`My number: ${value}`);
} else {
  console.log('Not a number');
}
