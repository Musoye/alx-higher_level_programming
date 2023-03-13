#!/usr/bin/node
const arg = Math.floor(Number(process.argv[2]));
if (Number.isInteger(arg)) {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let j = 0; j < arg; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
