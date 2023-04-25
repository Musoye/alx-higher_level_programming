#!/usr/bin/node
const request = require('request');
const file = process.argv;
request(file[2], function (error, response) {
  if (error) console.log(error);
  console.log('code: ', response && response.statusCode);
});
