#!/usr/bin/node
const nmb = parseInt(process.argv[2]);

if (Number.isNaN(nmb)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + nmb);
}
