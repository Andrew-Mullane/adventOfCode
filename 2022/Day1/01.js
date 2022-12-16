// Day one
// Input data
var fs = require('fs');

let input = fs.readFileSync('./input.txt', 'utf-8')

let inputArr = input.split('\n');
let elfSigmas = []

let elf = 0
for (let i in inputArr) {
  // console.log(inputArr[i])
  if(inputArr[i] == ''){
    elfSigmas.push(elf)
    elf = 0
      }
  else if (i == (inputArr.length - 1)){
    elf += Number(inputArr[i])
    elfSigmas.push(elf)
  }
  else {
    elf += Number(inputArr[i])
  }
  // console.log(inputArr[i])
}

// console.log(elfSigmas)
let top3 = 0
let max = findMax(elfSigmas)

max
top3 += max

let index1 = findMaxIndex(elfSigmas, max)

index1

elfSigmas.splice(128,1)

max = findMax(elfSigmas)
let index2 = findMaxIndex(elfSigmas, max)

max
index2
top3 += max

elfSigmas.splice(27,1)

max = findMax(elfSigmas)
let index3 = findMaxIndex(elfSigmas, max)

max
index3
top3 += max

top3



function findMax(arr){
  return Math.max(...arr)
}

function findMaxIndex(arr, max){
  return arr.indexOf(max)
}