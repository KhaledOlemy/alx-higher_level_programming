#!/usr/bin/node
const request = require('request');
let reqUrl = 'https://swapi-api.alx-tools.com/api/films/';
reqUrl = reqUrl + process.argv[2] + '/';
request(reqUrl, function (n0, n1, body) {
  const charactersList = JSON.parse(body).characters;
  for (let i = 0; i < charactersList.length; i++) {
    request(charactersList[i], function (n0, n1, cBody) {
      const aName = JSON.parse(cBody).name;
      console.log(aName);
    });
  }
});
