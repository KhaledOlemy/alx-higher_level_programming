#!/usr/bin/node
exports.esrever = function (list) {
  let temp;
  let i;
  for (i = 0; i < Math.floor(list.length / 2); i++) {
    temp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = temp;
  }
  return list;
};
