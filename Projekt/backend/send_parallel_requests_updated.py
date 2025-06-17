import random
import json
import concurrent.futures
import requests

# Neue Ziel-URL deines Servers (Azure)
URL = "https://m300-inventar-api-55-h7aje5f2d7akdude.westeurope-01.azurewebsites.net/devices"

# Mögliche Gerätetypen und Benutzer
device_names = ["Laptop Dell", "Laptop HP", "MacBook Pro", "Surface Pro", "ThinkPad X1", "iMac", "Chromebook", "MacBook Air"]
users = ["Max Muster", "Anna Schmidt", "John Doe", "Lara Kunz", "Tim Becker", "Nina Graf", "Paul Frei", "Eva Roth"]

# Seriennummer-Generator
def generate_serial_number():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))

# Erzeuge 100 zufällige Gerätedaten
requests_payloads = [
    {
        "name": random.choice(device_names),
        "serialNumber": generate_serial_number(),
        "user": random.choice(users)
    }
    for _ in range(100)
]

# Funktion zum Senden einer einzelnen Anfrage
def send_request(payload):
    try:
        response = requests.post(URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        print(f"Status: {response.status_code} | Response: {response.text.strip()}")
    except Exception as e:
        print(f"Fehler: {str(e)}")

# Paralleles Ausführen aller Anfragen
def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(send_request, requests_payloads)

if __name__ == "__main__":
    main()
