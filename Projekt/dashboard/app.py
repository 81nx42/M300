# dashboard/app.py
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "https://m300-inventar-api-55-h7aje5f2d7akdude.westeurope-01.azurewebsites.net/devices"

st.set_page_config(page_title="Inventar Dashboard", layout="centered")

st.title("📦 Inventarverwaltung – Dashboard")
st.markdown("Dieses Dashboard zeigt Daten und Status der Azure-API aus dem Modul 300-Projekt.")

# --- Geräte abrufen ---
st.subheader("🖥️ Aktuelle Geräte")
try:
    res = requests.get(API_URL)
    if res.status_code == 200:
        devices = res.json()
        df = pd.DataFrame(devices)
        if not df.empty:
            st.dataframe(df)
        else:
            st.info("Noch keine Geräte eingetragen.")
    else:
        st.error(f"Fehler beim Laden der Geräte (Status: {res.status_code})")
except Exception as e:
    st.error(f"Verbindung fehlgeschlagen: {e}")

# --- Gerät hinzufügen ---
st.subheader("➕ Neues Gerät hinzufügen")
with st.form("add_device"):
    name = st.text_input("Gerätename")
    serial = st.text_input("Seriennummer")
    user = st.text_input("Benutzer")
    submitted = st.form_submit_button("Hinzufügen")
    if submitted:
        new_device = {"name": name, "serialNumber": serial, "user": user}
        resp = requests.post(API_URL, json=new_device)
        if resp.status_code == 201:
            st.success("Gerät hinzugefügt!")
        else:
            st.error("Fehler beim Hinzufügen.")

# --- Monitoring: Dummy-Daten anzeigen (optional) ---
st.subheader("📊 API Performance (Demo)")
fake_data = pd.DataFrame({
    "Zeitpunkt": pd.date_range(end=pd.Timestamp.now(), periods=10),
    "Antwortzeit (ms)": [120, 150, 130, 110, 145, 160, 155, 148, 132, 125]
})
fig, ax = plt.subplots()
ax.plot(fake_data["Zeitpunkt"], fake_data["Antwortzeit (ms)"])
ax.set_title("Antwortzeiten der API (Demo)")
ax.set_ylabel("ms")
ax.set_xlabel("Zeit")
st.pyplot(fig)

# --- Projektinfos ---
st.markdown("---")
st.subheader("ℹ️ Projektbeschreibung")
st.markdown("""
- **API**: Node.js + Express
- **Hosting**: Azure App Service (Linux)
- **Deployment**: PowerShell + VS Code Extension
- **Monitoring**: Application Insights
- **Security**: Zugriffsbeschränkung via IP-Filter (Azure Access Restrictions)
""")
