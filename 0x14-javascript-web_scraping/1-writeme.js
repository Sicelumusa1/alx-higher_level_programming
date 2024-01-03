#!/usr/bin/node
/* Writes data to a file */
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File saved');
});
