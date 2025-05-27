const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

let devices = [];

app.use(express.json());

app.get('/devices', (req, res) => {
  res.json(devices);
});

app.post('/devices', (req, res) => {
  const device = req.body;
  devices.push(device);
  res.json({ message: "Gerät hinzugefügt", device });
});

app.listen(port, () => {
  console.log(`API läuft auf Port ${port}`);
});
