// Day one
// Input data

const fs = require('fs')

let msg: string[] 

fs.readFile('./test.txt', 'utf-8', (err: string, data: string) => {
  if (err) {
    console.error(err)
    return
  }
  msg = data.split('\n')

console.log(msg)
})

