#!/usr/bin/node

const request = require('request');

const movieid = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieid;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
