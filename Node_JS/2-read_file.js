const fs = require('fs');

function countStudents(path) {
    try {
        // Read file synchronously
        const data = fs.readFileSync(path, 'utf8').trim();
        if (!data) throw new Error('Cannot load the database');

        const lines = data.split('\n').filter(line => line.trim() !== '');
        const students = lines.slice(1); // Exclude header

        console.log(`Number of students: ${students.length}`);

        const fields = {};

        for (const student of students) {
            const details = student.split(',');
            if (details.length < 2) continue; // Ensure valid entry
            const firstName = details[0].trim();
            const field = details[details.length - 1].trim();

            if (!fields[field]) fields[field] = [];
            fields[field].push(firstName);
        }

        for (const [field, names] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
