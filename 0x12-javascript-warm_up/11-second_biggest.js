#!/usr/bin/node
let i;
let max = -Infinity;
let secmax = -Infinity;
const lst = process.argv;
const len = lst.length;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (i = 2; i < len + 2; i++) {
    if (parseInt(lst[i]) > secmax) {
      if (parseInt(lst[i]) > max) {
        secmax = max;
        max = parseInt(lst[i]);
      } else {
        secmax = parseInt(lst[i]);
      }
    }
  }
}
console.log(secmax);
