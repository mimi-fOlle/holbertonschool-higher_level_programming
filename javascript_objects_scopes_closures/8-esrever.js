#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  for (let i = list.length; i > 0; i--) {
    myList.push(list[i - 1]);
  }
  return myList;
};
