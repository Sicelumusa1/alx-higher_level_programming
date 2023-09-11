#!/usr/bin/node

const args = process.argv.slice(2).map(arg => parseInt(arg));

let largest;
let secondLargest;

if (args.length <= 1) {
  console.log(0);
} else {
  largest = args[0];
  secondLargest = args[1];
}

if (args[1] > args[0]) {
  largest = args[1];
  secondLargest = args[0];
}

for (let i = 2; i < args.length; i++) {
  if (args[i] > largest) {
    secondLargest = largest;
    largest = args[i];
  } else if (args[i] > secondLargest && args[i] !== largest) {
    secondLargest = args[i];
  }
}

if (secondLargest !== undefined) {
  console.log(secondLargest);
}
