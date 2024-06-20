#!/usr/bin/node
exports.esrever = function (list) {
  const newList = new Array(list.length);
  let index = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    newList[index] = list[i];
    index--;
  }
  return newList;
};
