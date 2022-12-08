#!/usr/bin/node

const args = process.argv.slice(2);

if (isNaN(args[0]) || (!args[0])) {
  console.log('1');
} else {
  factorial(args[0], (args[0] - 1));
}

function factorial (num, snum) {
  if (snum > 1) {
    num = (num * (snum));
    return factorial(num, (snum - 1));
  }
  console.log(num);
}
