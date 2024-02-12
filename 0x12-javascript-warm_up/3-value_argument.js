#!/usr/bin/node
const myVar = process.argv[2];
if (myVar) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
