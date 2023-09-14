#!/usr/bin/node

const program = 'C is fun, Python is cool, JavaScript is amazing';
const language = program.split(', ');

for (let lang = 0; lang < 3; lang++) {
  console.log(language[lang]);
}
