#!/usr/bin/node
/* Prints the title of a Star Wars movie where the episode number matches a given integer */
const request = require('request');

const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);

  if (data.detail === 'Not found') {
    console.log(`No movie with ID ${id}`);
    return;
  }

  console.log(data.title);
});
