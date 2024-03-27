#!/usr/bin/node
const request = require('request');
const reqUrl = process.argv[2];
let count = 0;
request(reqUrl, function (n0, n1, body) {
  let moviesList = JSON.parse(body).results;
  for (let i = 0; i < moviesList.length; i++)
  {
    if (moviesList[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/'))
    {
      count += 1;
    }
  }
  console.log(count);
});
