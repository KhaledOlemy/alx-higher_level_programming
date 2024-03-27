#!/usr/bin/node
const request = require('request');
const reqUrl = process.argv[2];
function getSuccess (movie) {
  let tempCount = 0;
  let tempCharacters = movie.characters;
  for (let j = 0; j <tempCharacters.length; j++) {
    if (tempCharacters[j].includes('18')) {
      tempCount += 1;
    }
  }
  return tempCount;

}
request(reqUrl, function (n0, n1, body) {
  const moviesList = JSON.parse(body).results;
  const count = moviesList.filter(getSuccess).length;
  console.log(count);
});
