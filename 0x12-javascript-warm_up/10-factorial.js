#!/usr/bin/node
let Out;

function factorial (input) {
  if (input === 1) {
    return input;
  } else {
    return input * factorial(input - 1);
  }
}
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  Out = factorial(parseInt(process.argv[2]));
  console.log(Out);
}
