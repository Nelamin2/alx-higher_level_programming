#!/usr/bin/node
const dict = require('./101-data').dict;

let occurrences = {};

for (let userId in dict) {
  let occurrence = dict[userId];
  if (occurrences[occurrence] === undefined) {
    occurrences[occurrence] = [];
  }
  occurrences[occurrence].push(userId);
}

console.log(occurrences);

