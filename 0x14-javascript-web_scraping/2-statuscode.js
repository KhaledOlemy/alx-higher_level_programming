#!/usr/bin/node
const request = require('request');
console.log(process.argv[2]);
process.stdout.write('code: ');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`${response.statusCode}`);
});
