#!/usr/bin/node
const movieNum = process.argv[2];
const request = require('request');
const reqUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieNum;
request(reqUrl, function (n0, n1, body) {
  console.log(JSON.parse(body).title);
});
