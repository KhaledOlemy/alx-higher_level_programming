#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const reqUrl = process.argv[2];
const fName = process.argv[3];
console.log(reqUrl);
console.log(fName);
request(reqUrl, function (n0, n1, body) {
    fs.writeFileSync(fName, body, { encoding: 'utf-8' });
});
