#!/usr/bin/node
const request = require('request');
const reqUrl = process.argv[2];
function getSuccess (movie) {
  return movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
}
request(reqUrl, function (n0, n1, body) {
  const moviesList = JSON.parse(body).results;
  const count = moviesList.filter(getSuccess).length;
  console.log(count);
});
