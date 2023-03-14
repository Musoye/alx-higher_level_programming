#!/usr/bin/node
let list = require('./100-data.js').list;
let arr = list.map((element, index) => element * index);
console.log(list);
console.log(arr);
