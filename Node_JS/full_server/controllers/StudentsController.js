import readDatabase from '../utils.js'; // Import the readDatabase function

class StudentsController {
  // Static method to get all students
  static async getAllStudents(req, res) {
    try {
      const fields = await readDatabase('./database.csv');
      let studentsList = 'This is the list of our students\n';

      // Sort fields alphabetically
      const sortedFields = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      sortedFields.forEach(field => {
        const names = fields[field].join(', ');
        studentsList += `Number of students in ${field}: ${fields[field].length}. List: ${names}\n`;
      });

      res.status(200).send(studentsList);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  // Static method to get students by major
  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    
    // Check if major is CS or SWE
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const fields = await readDatabase('./database.csv');

      // Check if the field exists in the database
      if (!fields[major]) {
        return res.status(500).send('Cannot load the database');
      }

      const names = fields[major].join(', ');
      res.status(200).send(`List: ${names}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
