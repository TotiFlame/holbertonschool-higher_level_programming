#!/usr/bin/node

const args = process.argv.slice(2);

if (!args[0] || args.length === 1) {
  console.log('0');
} else {
  const numbers = args.sort((a, b) => (b - a));
  console.log(numbers[1]);
}
