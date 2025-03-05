const http = require('http');
const countStudents = require('./3-read_file_async');

const databasePath = process.argv[2]; // Get database file from command-line argument

const app = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    if (req.url === '/') {
        res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
        res.write('This is the list of our students\n');
        countStudents(databasePath)
            .then((output) => {
                res.end(`${output}\n`); // Send output in response
            })
            .catch((err) => {
                res.end(`${err.message}\n`);
            });
    } else {
        res.end('Not Found');
    }
});

app.listen(1245);

module.exports = app;
