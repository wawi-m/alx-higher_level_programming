#!/usr/bin/node
const args = process.argv.slice(2);
const arg1 = args[0];

const parsedInt = parseInt(arg1);
if (arg1 !== undefined && !isNaN(parsedInt)) {
  console.log(`My number: ${parseInt(arg1, 10)}`);
} else {
  console.log('Not a number');
}
