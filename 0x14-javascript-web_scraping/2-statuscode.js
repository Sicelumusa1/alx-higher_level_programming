#!/usr/bin/node
/* Displays the status code of a GET request */
const request = require('request');

request(process.argv[2], (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
