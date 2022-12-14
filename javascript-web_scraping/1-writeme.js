#!/usr/bin/node
const fs = require('fs');

const filepath = process.argv[2];
const text = process.argv[3];

fs.writeFile(filepath, text, function (error) {
  if (error) {
    console.error(error);
  }
});
