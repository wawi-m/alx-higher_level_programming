#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const secondArg = args[1];

if (firstArg === undefined || secondArg === undefined) {
    console.log("Usage: node script.js <arg1> <arg2>");
} else {
    console.log(`${firstArg} is ${secondArg}`);
}
