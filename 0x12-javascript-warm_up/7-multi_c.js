#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
let i;
if (isNaN(myVar)) {
  console.log('Missing number of occurences');
} else {
  for (i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
