#!/usr/bin/node
const file = require('fs');
const file1 = file.readFileSync(process.argv[2]).toString();
const file2 = file.readFileSync(process.argv[3]).toString();
file.writeFileSync(process.argv[4], file1 + file2);
