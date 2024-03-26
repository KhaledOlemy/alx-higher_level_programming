#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const fileContent = process.argv[3];
fs.writeFileSync(fileName, fileContent, { encoding: 'utf-8' });
