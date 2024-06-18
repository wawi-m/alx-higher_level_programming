#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);
const arg1 = parseInt(args[0]);
const arg2 = parseInt(args[1]);

if (isNaN(arg1) || isNaN(arg2)) {
  console.log('Invalid input. Please provide two integers.');
} else {
  // Calculate the addition using the add function
  const result = add(arg1, arg2);
  console.log(`The addition of ${arg1} and ${arg2} is: ${result}`);
}
