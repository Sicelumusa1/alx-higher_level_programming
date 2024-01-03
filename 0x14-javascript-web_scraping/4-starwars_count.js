#!/usr/bin/node
/* Prints the number of movies where the character “Wedge Antilles” is present */
const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characterId = 18;

  const count = body.results.filter((film) => {
    return film.characters.some((character) => character.includes(`/people/${characterId}/`));
  }).length;

  console.log(`${count}`);
});
