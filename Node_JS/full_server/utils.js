import fs from 'fs/promises';

async function readDatabase(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        const lines = data.trim().split('\n').filter(line => line.trim() !== '');
        const students = lines.slice(1); // Remove header

        const fields = {};

        for (const student of students) {
            const details = student.split(',');
            if (details.length < 2) continue; // Ensure valid entry
            const firstName = details[0].trim();
            const field = details[details.length - 1].trim();

            if (!fields[field]) fields[field] = [];
            fields[field].push(firstName);
        }

        return fields;
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

export default readDatabase;
