#!/usr/bin/node
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const args = process.argv.slice(2);
const n = parseInt(args[0]);
const ans = factorial(n);

console.log(`${ans}`);
