#!/usr/bin/node

const args = (process.argv.slice(2));

if (isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(args[0]);
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
}
