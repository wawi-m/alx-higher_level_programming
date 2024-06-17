#!/usr/bin/node
const args = process.argv.slice(2);
const arg1 = args[0];
const arg2 = args[1];

if (arg1 === undefined && arg2 === undefined) {
  console.log('undefined is undefined');
} else if (arg1 !== undefined && arg2 === undefined) {
  console.log(`${arg1} is undefined`);
} else {
  console.log(`${arg1} is ${arg2}`);
}
