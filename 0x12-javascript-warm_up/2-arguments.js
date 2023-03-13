#!/usr/bin/node
const arg = process.argv.length;
console.log(arg === 2 ? 'No argument' : arg === 3 ? 'Argument found' : 'Arguments found');
