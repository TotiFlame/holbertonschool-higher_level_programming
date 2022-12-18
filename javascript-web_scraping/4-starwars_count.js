#!/usr/bin/node
const request = require('request');

<<<<<<< HEAD
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
=======
const url = proccess.argv[1];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(body);
>>>>>>> 9c951a2488b4fc023df394cc11cd632fa3ccba45
});
