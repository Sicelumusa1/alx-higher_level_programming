#!/usr/bin/node

function add (a, b) {
  a = process.argv[2];
  b = process.argv[3];

  a = parseFloat(a);
  b = parseFloat(b);

  if (isNaN(a) || isNaN(b)) {
    return NaN;
  } else {
    const result = a + b;
    return result;
  }
}
console.log(add());
