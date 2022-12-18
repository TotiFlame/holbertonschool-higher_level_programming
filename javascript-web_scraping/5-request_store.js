#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(filepath, body, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
