#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);
add(x, y);
