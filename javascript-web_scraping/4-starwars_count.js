#!/usr/bin/node
const request = require('request');

const url = proccess.argv[1];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(body);
});
