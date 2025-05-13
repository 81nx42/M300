# API-Endpunkte – Inventarverwaltung

Die API erlaubt die Verwaltung von Geräten im Inventarsystem.

## Endpunkte

### `GET /devices`
- Gibt eine Liste aller Geräte zurück.
- Response: JSON-Array mit Geräten.

### `POST /devices`
- Fügt ein neues Gerät hinzu.
- Body (JSON): 
```json
{
  "name": "Laptop Dell",
  "serialNumber": "ABC123",
  "user": "Max Muster"
}
