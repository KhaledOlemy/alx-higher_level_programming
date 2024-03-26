#!/usr/bin/node
const request = require('request');
console.log(process.argv[2]);
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
