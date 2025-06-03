const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

let devices = [];

app.get('/', (req, res) => {
  res.send('Hello from M300 API');
});

app.get('/devices', (req, res) => {
  res.json(devices);
});

app.post('/devices', (req, res) => {
  const device = req.body;
  devices.push(device);
  res.status(201).json({ message: "Gerät hinzugefügt", device });
});
