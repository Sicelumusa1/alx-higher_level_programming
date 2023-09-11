#!/usr/bin/node

const arg = process.argv[2];

const num = Number(arg);

if (!isNaN(num) && Number.isInteger(num)) {
  for (let digit = 0; digit < num; digit++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
