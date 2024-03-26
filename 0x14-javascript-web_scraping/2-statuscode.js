#!/usr/bin/node
const request = require('request');
process.stdout.write('code: ');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`${response.statusCode}`);
});
