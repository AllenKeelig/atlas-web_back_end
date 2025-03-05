const express = require('express');
const countStudents = require('./3-read_file_async');

const databasePath = process.argv[2]; // Get the database file from command-line arguments
const app = express();

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
    countStudents(databasePath)
        .then((output) => {
            res.send(`This is the list of our students\n${output}`);
        })
        .catch((err) => {
            res.send(`This is the list of our students\n${err.message}`);
        });
});

app.listen(1245);

module.exports = app;
