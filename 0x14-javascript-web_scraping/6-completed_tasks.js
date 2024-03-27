#!/usr/bin/node

const request = require('request');
const reqUrl = process.argv[2];
request(reqUrl, function (n0, n1, body) {
  const tasksByUsers = {};
  let bodyJson = JSON.parse(body);
  for (let i = 0; i < bodyJson.length; ++i) {
    const userId = bodyJson[i].userId;
    const completed = bodyJson[i].completed;
    if (!tasksByUsers[userId] && completed) {
      tasksByUsers[userId] = 0;
    }
    if (completed) ++tasksByUsers[userId];
  }
  console.log(tasksByUsers);
});
