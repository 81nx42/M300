const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

let devices = [];
let nextId = 0;

app.get('/', (req, res) => {
  res.send('Hello from M300 API');
});

app.get('/devices', (req, res) => {
  res.json(devices);
});

app.post('/devices', (req, res) => {
  const device = req.body;
  device.id = nextId++;
  devices.push(device);
  res.status(201).json({ message: "Gerät hinzugefügt", device });
});

app.put('/devices/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = devices.findIndex(d => d.id === id);
  if (index === -1) {
    return res.status(404).json({ error: "Gerät nicht gefunden" });
  }
  devices[index] = { ...req.body, id }; // ID bleibt gleich
  res.json({ message: 'Gerät aktualisiert', device: devices[index] });
});

app.delete('/devices/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = devices.findIndex(d => d.id === id);
  if (index === -1) {
    return res.status(404).json({ error: "Gerät nicht gefunden" });
  }
  devices.splice(index, 1);
  res.json({ message: 'Gerät gelöscht' });
});

app.listen(port, () => {
  console.log(`Server läuft auf Port ${port}`);
});
