require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

// --- Verbindung zur Datenbank herstellen ---
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => console.log("✅ Mit MongoDB verbunden"))
  .catch(err => console.error("❌ Fehler bei MongoDB-Verbindung:", err));

// --- Geräteschema definieren ---
const deviceSchema = new mongoose.Schema({
    name: String,
    serialNumber: String,
    user: String,
    timestamp: {
        type: Date,
        default: Date.now
    }
});

const Device = mongoose.model('Device', deviceSchema);

// --- GET: Alle Geräte ---
app.get('/devices', async (req, res) => {
    try {
        const devices = await Device.find();
        res.json(devices);
    } catch (err) {
        res.status(500).json({ error: "Fehler beim Abrufen der Geräte" });
    }
});

// --- POST: Neues Gerät ---
app.post('/devices', async (req, res) => {
    try {
        const newDevice = new Device(req.body);
        const saved = await newDevice.save();
        res.status(201).json({ message: "Gerät hinzugefügt", device: saved });
    } catch (err) {
        res.status(400).json({ error: "Fehler beim Speichern" });
    }
});

// --- PUT: Gerät aktualisieren ---
app.put('/devices/:id', async (req, res) => {
    try {
        const updated = await Device.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!updated) return res.status(404).json({ error: "Gerät nicht gefunden" });
        res.json({ message: "Gerät aktualisiert", device: updated });
    } catch (err) {
        res.status(400).json({ error: "Fehler beim Aktualisieren" });
    }
});

// --- DELETE: Gerät löschen ---
app.delete('/devices/:id', async (req, res) => {
    try {
        const deleted = await Device.findByIdAndDelete(req.params.id);
        if (!deleted) return res.status(404).json({ error: "Gerät nicht gefunden" });
        res.json({ message: "Gerät gelöscht" });
    } catch (err) {
        res.status(400).json({ error: "Fehler beim Löschen" });
    }
});

app.listen(port, () => {
    console.log(`🚀 API läuft auf Port ${port}`);
});
