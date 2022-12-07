#!/usr/bin/node

const args = parseInt(process.argv[2]);

if (!isNaN(args[0])) {
  console.log('Missing size');
} else {
  let sq = '';
  for (let i = 1; i <= args; i++) {
    sq += 'X';
  }
  console.log(sq);
  for (let i = 1; i < args; i++) {
    console.log(sq);
  }
}
