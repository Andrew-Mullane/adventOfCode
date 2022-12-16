// Day one
// Input data
var fs = require('fs');

let input = fs.readFileSync('./test.txt', 'utf-8')

let inputArr = input.split('\n');
let elfSigma = []

let elf = 0
for (let i in inputArr) {
  if(inputArr[i] == ''){
    elfSigma.push(elf)
    elf = 0
      }
  else {
    elf += inputArr[i]
  }
  // console.log(inputArr[i])
}
console.log(elfSigma)