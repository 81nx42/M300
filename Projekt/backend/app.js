const express = require('express');
const app = express();
app.use(express.json());

let devices = [];

// GET /devices
app.get('/devices', (req, res) => {
  res.json(devices);
});

// POST /devices
app.post('/devices', (req, res) => {
  const device = req.body;
  devices.push(device);
  res.status(201).json(device);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server läuft auf Port ${PORT}`);
});
