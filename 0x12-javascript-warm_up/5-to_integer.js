#!/usr/bin/node
const args = process.argv.slice(2);
const arg1 = args[0];

if (arg1 !== undefined && !isNaN(arg1) && Number.isInteger(parseFloat(arg1))) {
    console.log(`My number: ${parseInt(firstArg, 10)}`);
} else {
    console.log('Not a number');
}
