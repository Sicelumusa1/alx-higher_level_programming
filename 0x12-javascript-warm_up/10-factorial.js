#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}

const arg = process.argv[2];
const num = parseInt(arg);

const result = factorial(num);

console.log(result);
