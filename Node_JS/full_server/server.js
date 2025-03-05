import express from 'express';
import indexRoutes from './routes/index.js';  // Import routes

const app = express();

// Use the routes defined in index.js
app.use('/', indexRoutes);

// Start the server on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

export default app;
