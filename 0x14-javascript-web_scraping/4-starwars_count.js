#!/usr/bin/node
const request = require('request');
const reqUrl = 'https://swapi-api.alx-tools.com/api/people/18';
request(reqUrl, function (n0, n1, body) {
  console.log(JSON.parse(body).films.length);
});
