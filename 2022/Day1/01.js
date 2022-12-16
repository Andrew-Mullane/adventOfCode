// Day one
// Input data
var fs = require('fs');
var msg;
fs.readFile('./test.txt', 'utf-8', function (err, data) {
    if (err) {
        console.error(err);
        return;
    }
    msg = data.split('\n');
    console.log(msg);
});

