const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.trim().split('\n').filter(line => line.trim() !== '');
            const students = lines.slice(1);

            let output = `Number of students: ${students.length}\n`;

            const fields = {};

            for (const student of students) {
                const details = student.split(',');
                if (details.length < 2) continue; 
                const firstName = details[0].trim();
                const field = details[details.length - 1].trim();

                if (!fields[field]) fields[field] = [];
                fields[field].push(firstName);
            }

            for (const [field, names] of Object.entries(fields)) {
                output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
            }

            resolve(output.trim()); // Return the formatted string
        });
    });
}

module.exports = countStudents;
