#!/usr/bin/node
const argc = process.argv.length;
if (argc < 4) {
  console.log(0);
} else {
  const arg = process.argv.slice(2);
  arg.sort().reverse();
  console.log(arg[1]);
}
