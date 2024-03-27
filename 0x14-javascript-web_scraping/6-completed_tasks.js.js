#!/usr/bin/node
const request = require('request');
const reqUrl = process.argv[2];

request(reqUrl, function (n0, n1, body) {
  const allTasks = JSON.parse(body);
  const completedTasks = {};
  for (let i = 0; i < allTasks.length; i++) {
    if (allTasks[i].completed) {
      if (completedTasks[`${allTasks[i].userId}`]) {
        completedTasks[`${allTasks[i].userId}`] += 1;
      } else {
        completedTasks[`${allTasks[i].userId}`] = 1;
      }
    }
  }
  console.log(completedTasks);
  // const count = moviesList.filter(getSuccess).length;
  // console.log(count);
});
