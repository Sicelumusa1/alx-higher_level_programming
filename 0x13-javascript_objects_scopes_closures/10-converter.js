#!/usr/bin/node

exports.converter = function (base) {
  if (base === 10) {
    return function (number) {
      return number;
    };
  } else {
    return function (number) {
      return number.toString(base);
    };
  }
};
