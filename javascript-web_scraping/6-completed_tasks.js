#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const count = {};
    const obj = JSON.parse(body);

    for (const todo of obj) {
      if (todo.completed === true) {
        if (todo.userId in count) {
          count[todo.userId]++;
        } else {
          count[todo.userId] = 1;
        }
      }
    }
    console.log(count);
  }
});
