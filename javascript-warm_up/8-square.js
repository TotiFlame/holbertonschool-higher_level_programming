#!/usr/bin/node

const args = (process.argv.slice(2));

if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  const num = parseInt(args[0]);
  let sq = '';
  for (let i = 1; i <= num; i++) {
    sq += 'X';
  }
  console.log(sq);
  for (let i = 1; i < num; i++) {
    console.log(sq);
  }
}
