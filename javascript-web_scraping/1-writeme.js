#!/usr/bin/node
const fs = require('fs');

const data = process.argv[3];

// Writing the file
fs.writeFile(process.argv[2], data, (err) => {
  if (err);
  console.log(err);
});
