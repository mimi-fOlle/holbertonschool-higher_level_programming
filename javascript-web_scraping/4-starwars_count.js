#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  const film = JSON.parse(body).results;
  let count = 0;

  if (!error) {
    for (const x of film) {
      for (const role of x.characters) {
        if (role === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
}
);
