#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, function (error, response, body) {
  if (!error) {
    fs.writeFile(filename, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
