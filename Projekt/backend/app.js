const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello from M300 API!');
});

app.listen(port, () => {
  console.log(`Server läuft auf Port ${port}`);
});
