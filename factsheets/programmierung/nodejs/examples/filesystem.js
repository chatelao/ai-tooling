const fs = require('fs');

const content = 'Hello from Node.js File System!';
fs.writeFile('example.txt', content, err => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File written successfully');

  fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('File content:', data);
  });
});
