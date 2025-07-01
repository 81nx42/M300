# LernJornal 

## 1. Tag – Lernjournal
### Zusammenfassung des Tages
Der erste Tag diente dem Einstieg in das Projekt. Ich verschaffte mir einen Überblick über die Projektziele und die geplante Architektur. Der Fokus lag auf der Planung der Inventar-API, der Vorbereitung der Ordnerstruktur sowie der Einrichtung des Node.js-Backends. Erste Tests mit npm init und dem Express-Framework wurden durchgeführt.

### Tagesziele
- Projektüberblick verschaffen

- Ordnerstruktur gemäß Vorgabe erstellen

- Node.js-Projekt initialisieren

- Express installieren und erstes Grundgerüst in app.js aufsetzen

### Erreichte Tagesziele
- Projektstruktur nach Anleitung angelegt (backend/, scripts/, docs/ etc.)

- Node.js-Backend mit npm init -y eingerichtet

- Express erfolgreich installiert

- Erste Basisfunktionen (GET /devices, POST /devices) in app.js implementiert

### Probleme & Herausforderungen
- Leichte Unsicherheiten bei der Strukturierung des Backends, insbesondere bei der Wahl des Ports und dem Umgang mit process.env.PORT

- Kleinere Syntaxprobleme beim JSON-Handling in Express

- Genutzte & neu entdeckte Ressourcen
- Express-Dokumentation

- Eigene Notizen zur Projektstrukturierung

---
# 2. Tag – Lernjournal
### Zusammenfassung des Tages
Heute wurde das Deployment auf Azure vorbereitet. Der Fokus lag auf dem Erstellen und Testen des PowerShell-Skripts deploy.ps1, um automatisiert Ressourcen wie die Resource Group, App Service Plan und Web App zu erstellen. Die Verbindung zu Azure wurde erfolgreich aufgebaut.

### Tagesziele
- Azure-Ressourcen automatisiert erstellen

- PowerShell-Skript deploy.ps1 schreiben und testen

- Verbindung zur Azure Cloud aufbauen

### Erreichte Tagesziele
- deploy.ps1 erfolgreich erstellt und getestet

- Azure-Ressourcen (Resource Group, App Service Plan, Web App) über CLI erstellt

- Verbindung zur Azure Cloud über Connect-AzAccount hergestellt

### Probleme & Herausforderungen
- Zeitverlust durch Berechtigungsprobleme beim Zugriff auf Azure

- Anpassung des Skripts wegen bereits existierender Ressourcen notwendig

- Fehlerhafte Eingabe des Runtime-Parameters musste korrigiert werden

### Genutzte & neu entdeckte Ressourcen
- Microsoft PowerShell Azure-Dokumentation

- Eigene Tests und Debugging mit -ErrorAction SilentlyContinue
--- 
# 3. Tag – Lernjournal
### Zusammenfassung des Tages
Der Fokus lag auf der Konfiguration und dem Upload des Node.js-Backends in Azure. Das Deployment wurde mit Visual Studio Code und der Azure App Service Extension durchgeführt. Die API war nach dem Upload unter der bereitgestellten URL erreichbar. Erste Tests mit GET /devices verliefen erfolgreich.

### Tagesziele
- Node.js-Backend deployen

- Funktionsfähigkeit der API über Azure überprüfen

- Erste Tests mit HTTP-Requests

### Erreichte Tagesziele
- Deployment über VS Code abgeschlossen

- API-Endpunkte funktionierten (GET /devices lieferte leeres Array)

- Projektstruktur wurde korrekt erkannt und ausgeführt

### Probleme & Herausforderungen
- Anfängliche Verwirrung über die Auswahl des Ordners beim Deploy-Prozess

- Debugging notwendig, da lokale Ports sich von der Azure-URL unterschieden

### Genutzte & neu entdeckte Ressourcen
- Azure App Service Extension für VS Code

- Azure-WebApp 

---

# 4. Tag – Lernjournal
### Zusammenfassung des Tages
Heute stand das Einrichten von Application Insights zur Überwachung der API im Mittelpunkt. Das Monitoring wurde über ein PowerShell-Skript (setup-monitoring.ps1) automatisiert eingerichtet. Erste Live-Metriken konnten im Azure-Portal eingesehen werden.

### Tagesziele
- Application Insights erstellen

- Überwachung mit Azure konfigurieren

- PowerShell-Skript schreiben und testen

### Erreichte Tagesziele
- Monitoring-Ressource erstellt und korrekt angebunden

- Application Insights Key in Azure Web App eingebunden

- setup-monitoring.ps1 erfolgreich ausgeführt

### Probleme & Herausforderungen
- Das Setzen der AppSettings mit dem Key war zunächst fehlerhaft formatiert

- Monitoring zeigte zunächst keine Daten – API ist nicht Live

---

# 5. Tag – Lernjournal
### Zusammenfassung des Tages
Heute wurde das API-Testing vertieft. Mit Postman und curl wurden GET- und POST-Anfragen getestet. Außerdem wurde die Funktionalität zum Hinzufügen neuer Geräte validiert. Die API erwies sich als stabil und reagierte erwartungsgemäß.

### Tagesziele
- Funktionalität der API-Endpunkte prüfen

- Testdaten hinzufügen

- Fehlerhafte Eingaben simulieren

### Erreichte Tagesziele
- Testdaten erfolgreich per POST hinzugefügt

- API zeigte stabile Performance

- GET-Abfragen spiegelten neu hinzugefügte Geräte korrekt wider

### Probleme & Herausforderungen
- Vergessener Content-Type Header bei curl-POSTs führte zu 400er Fehlern

- Kein Validierungsmechanismus vorhanden – falsche Eingaben wurden akzeptiert

### Genutzte & neu entdeckte Ressourcen
- Postman

- curl-Befehle für API-Tests

---

# 6. Tag – Lernjournal
### Zusammenfassung des Tages
Das Streamlit-Dashboard wurde implementiert, um die API-Daten visuell darzustellen. Es wurden Funktionen zum Anzeigen und Hinzufügen von Geräten integriert. Zusätzlich wurde eine Verbindung zur Application Insights API hergestellt, um Live-Daten zu visualisieren.

### Tagesziele
- Streamlit installieren und konfigurieren

- Dashboard entwickeln (Anzeige, Formular, Monitoring)

- API-Integration testen

### Erreichte Tagesziele
- Streamlit erfolgreich eingerichtet

- Geräteliste und POST-Formular im Dashboard funktionierten

- Erste Metriken aus Application Insights als Liniendiagramm dargestellt

### Probleme & Herausforderungen
- API-Key-Handling mit dotenv bereitete anfangs Schwierigkeiten

- Formatierung der KQL-Abfrage war fehleranfällig

- Live-Update des Dashboards erfordert manuelle Umsetzung

### Genutzte & neu entdeckte Ressourcen
- Streamlit-Tool

- python-dotenv zum Laden der Umgebungsvariablen

---

# 7. Tag – Lernjournal
### Zusammenfassung des Tages
Am letzten Projekttag wurden Dokumentation, Readme und Screenshots gepflegt. Zudem erfolgte ein kompletter Testlauf von der API bis zum Dashboard. Abschließend wurde über Erweiterungsmöglichkeiten (z.B. PUT/DELETE-Endpunkte) reflektiert.

### Tagesziele
- Projektdokumentation abschließen

- Readme-Datei überarbeiten

- Abschlussprüfung und Funktionstest

### Erreichte Tagesziele
- Readme mit Projektbeschreibung, Setup-Anleitung und Screenshots ergänzt

- Ordnerstruktur finalisiert

- Projekt vollständig getestet (inkl. Monitoring & Dashboard)

### Probleme & Herausforderungen
- Kein größeres technisches Problem – Fokus lag auf Qualitätssicherung

- Formatierung in Markdown musste teilweise manuell korrigiert werden
