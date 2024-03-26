#!/usr/bin/node
const request = require('request');
process.stdout.write('');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`${response.statusCode}`);
});
