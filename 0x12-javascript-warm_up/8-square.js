#!/usr/bin/node

const arg = process.argv[2];

const num = Number(arg);

if (!isNaN(num) && Number.isInteger(num)) {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
