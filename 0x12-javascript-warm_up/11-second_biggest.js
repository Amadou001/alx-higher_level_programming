#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // Convert all arguments to integers

if (args.length < 2) {
  console.log(0);
} else {
  let maxValue = -Infinity;
  let secondMaxValue = -Infinity;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > maxValue) {
      secondMaxValue = maxValue;
      maxValue = args[i];
    } else if (args[i] > secondMaxValue && args[i] < maxValue) {
      secondMaxValue = args[i];
    }
  }

  console.log(secondMaxValue);
}
