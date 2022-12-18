#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed) {
        console.log(data[i].completed);
    }
  }
});