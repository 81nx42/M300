const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

let devices = [];

app.get('/', (req, res) => {
  res.send('Hello from M300 API');
});

app.get('/devices', (req, res) => {
  let tableRows = devices.map(device => `
    <tr>
      <td>${device.id || ''}</td>
      <td>${device.name}</td>
      <td>${device.serialNumber}</td>
      <td>${device.user}</td>
    </tr>
  `).join('');

  let html = `
    <!DOCTYPE html>
    <html>
    <head>
      <title>Geräteliste</title>
      <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
      </style>
    </head>
    <body>
      <h1>Inventarliste</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Gerätename</th>
            <th>Seriennummer</th>
            <th>Benutzer</th>
          </tr>
        </thead>
        <tbody>
          ${tableRows}
        </tbody>
      </table>
    </body>
    </html>
  `;

  res.send(html);
});


app.post('/devices', (req, res) => {
  const device = req.body;
  devices.push(device);
  res.status(201).json({ message: "Gerät hinzugefügt", device });
});
