import express from 'express';
import AppController from '../controllers/AppController.js';
import StudentsController from '../controllers/StudentsController.js';

const router = express.Router();

// Route for the homepage, linked to AppController
router.get('/', AppController.getHomepage);

// Route for /students, linked to StudentsController
router.get('/students', StudentsController.getAllStudents);

// Route for /students/:major, linked to StudentsController
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;
