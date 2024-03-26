#!/usr/bin/node
const fname = process.argv[2];
const fs = require('fs');
const temp = fs.readFileSync(fname, { encoding: 'utf-8' });
console.log(temp);
