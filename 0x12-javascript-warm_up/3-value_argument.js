#!/usr/bin/node
const args = process.argv.slice(2);
for (let i = 0; i < 1; i++) {
  if (args[i] === undefined) {
    console.log('No argument');
  } else {
    console.log(args[i]);
  }
}
