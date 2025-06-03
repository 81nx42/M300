# Projektbericht

## Einleitung

![](image.png)

Bei dem Modul 300 habe ich eine Inventar-API entwickelt, die in der Azure Cloud gehostet wird. Mein Ziel bei diesem Projekt war es des vertieften ablauf von Cloud-Services zu verstehen und dazu ein einfaches Backend aufzubauen. Das Backend wird in Azure bereitgestellt und mit Monitoring-Tools überwacht.

Die API wurde mit Node 22 TLS implementiert und ermöglicht das Abrufen und Hinzufügen von Geräten über HTTP-Endpoints.

## Dokumentation

#### Vorbereitung

Mein erster schritt war es eine VS Code Hirarchie zu bauen. In Meinem Projekt befinden sich die folgenden Ordner:

- Projekt
  - backend
    - app.js
    - package.json
  - docs
    - screenshots
      - image.png
  - scripts
    - deploy.ps1
    - setup-monitoring.ps1
  - Readme.md


#### Was die Dateien tun

Die Backend API läuft in Azure App Service.
Es bietet Endpunkte für GET POST /Devices 


Azure App Servuce Hostet meine API in einer Linux Umgebung mit Node 22. Stack

Die Powershell Skripte werden mir dabei helfen bei der Erstellung von Ressourcen. 