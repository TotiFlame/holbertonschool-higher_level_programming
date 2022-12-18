#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  let counter = 0;
  const data = JSON.parse(body);
  for (const movie of data.results) {
    for (const character of movie.characters) {
      const r = character.split('/');
      const id = r.slice(-2)[0];
      if (id === '18') {
        counter++;
      }
    }
  }
  console.log(counter);
});
