#!/usr/bin/node
const myvar = parseInt(process.argv[2]);
if (isNaN(myvar)) {
  console.log('Not a number');
} else {
  console.log('My number:', myvar);
}
