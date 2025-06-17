# dashboard/app.py

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from datetime import datetime

# --- .env laden ---
load_dotenv()
APP_ID = os.getenv("APPINSIGHTS_APP_ID")
API_KEY = os.getenv("APPINSIGHTS_API_KEY")

# --- API-URL deiner WebApp ---
API_URL = "https://m300-inventar-api-55-h7aje5f2d7akdude.westeurope-01.azurewebsites.net/devices"

# --- Streamlit-Seite konfigurieren ---
st.set_page_config(page_title="Inventar Dashboard", layout="centered")
st.title("📦 Inventarverwaltung – Dashboard")
st.markdown("Dieses Dashboard zeigt die Geräte-API und Live-Monitoring aus Azure Application Insights.")

# --------------------------------------
# 🖥️ Geräte abrufen und anzeigen
# --------------------------------------
st.subheader("🖥️ Aktuelle Geräte")
def load_devices():
    try:
        res = requests.get(API_URL)
        if res.status_code == 200:
            return pd.DataFrame(res.json())
        else:
            st.error(f"Fehler beim Laden der Geräte: {res.status_code}")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Verbindung zur API fehlgeschlagen: {e}")
        return pd.DataFrame()

device_df = load_devices()
if not device_df.empty:
    st.dataframe(device_df)
else:
    st.info("Noch keine Geräte eingetragen.")

# --------------------------------------
# ➕ Neues Gerät hinzufügen
# --------------------------------------
st.subheader("➕ Neues Gerät hinzufügen")
with st.form("add_device"):
    name = st.text_input("Gerätename")
    serial = st.text_input("Seriennummer")
    user = st.text_input("Benutzer")
    submitted = st.form_submit_button("Hinzufügen")
    if submitted:
        new_device = {
            "name": name,
            "serialNumber": serial,
            "user": user
        }
        try:
            resp = requests.post(API_URL, json=new_device)
            if resp.status_code == 201:
                st.success("✅ Gerät erfolgreich hinzugefügt.")
                st.rerun()  # ersetzt experimental_rerun()
            else:
                st.error(f"❌ Fehler beim Hinzufügen: {resp.status_code}")
        except Exception as e:
            st.error(f"❌ Verbindungsfehler: {e}")

# --------------------------------------
# 📊 Azure Application Insights Query
# --------------------------------------
st.subheader("📈 Live API-Performance (Application Insights)")

def query_application_insights():
    url = f"https://api.applicationinsights.io/v1/apps/{APP_ID}/query"
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    kql = """
    requests
    | where success == true
    | order by timestamp desc
    | take 20
    | project timestamp, duration
    """
    body = { "query": kql }

    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            data = response.json()
            rows = data['tables'][0]['rows']
            df = pd.DataFrame(rows, columns=["timestamp", "duration"])
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df["duration"] = df["duration"].astype(float)
            return df.sort_values("timestamp")
        else:
            st.error(f"Fehler beim Laden der Insights-Daten: {response.text}")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Insights-Abfrage fehlgeschlagen: {e}")
        return pd.DataFrame()

df_insights = query_application_insights()
if not df_insights.empty:
    fig, ax = plt.subplots()
    ax.plot(df_insights["timestamp"], df_insights["duration"], marker="o")
    ax.set_title("Letzte Antwortzeiten der API")
    ax.set_ylabel("Antwortzeit (ms)")
    ax.set_xlabel("Zeit")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
else:
    st.info("Keine Metriken verfügbar. Stelle sicher, dass Live Metrics aktiv sind und Traffic vorhanden ist.")

# --------------------------------------
# ℹ️ Projektinfos
# --------------------------------------
st.markdown("---")
st.subheader("ℹ️ Projektbeschreibung")
st.markdown("""
- **API**: Node.js + Express  
- **Hosting**: Azure App Service (Linux)  
- **Deployment**: PowerShell + VS Code Extension  
- **Monitoring**: Application Insights (per REST API)  
- **Sicherheit**: Zugriffsbeschränkung via IP-Filter (Access Restrictions)
""")
