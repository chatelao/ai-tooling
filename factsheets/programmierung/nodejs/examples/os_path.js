const path = require('path');
const os = require('os');

console.log('Home Directory:', os.homedir());
console.log('Total Memory:', (os.totalmem() / 1024 / 1024 / 1024).toFixed(2), 'GB');
console.log('Joined Path:', path.join(__dirname, 'examples', 'hello.js'));
