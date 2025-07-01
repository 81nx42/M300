import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# --- .env laden ---
load_dotenv()
API_URL = "https://m300-inventar-api-55-h7aje5f2d7akdude.westeurope-01.azurewebsites.net/devices"
APP_ID = os.getenv("APPINSIGHTS_APP_ID")
API_KEY = os.getenv("APPINSIGHTS_API_KEY")
USERNAME = os.getenv("DASHBOARD_USER")
PASSWORD = os.getenv("DASHBOARD_PASSWORD")

# --- Login-Session prüfen ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login():
    st.set_page_config(page_title="Login", layout="centered")
    st.title("🔐 Admin Login")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    if st.button("Einloggen"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["authenticated"] = True
            st.success("✅ Login erfolgreich")
            st.rerun()
        else:
            st.error("❌ Zugangsdaten ungültig")

if not st.session_state["authenticated"]:
    login()
    st.stop()

# --- Haupt-Dashboard ---
st.set_page_config(page_title="Inventar Dashboard", layout="centered")
st.title("📦 Inventar-Dashboard")
st.markdown("Geräte abrufen, hinzufügen, bearbeiten oder löschen.")

# --- Geräteliste laden ---
def load_devices():
    try:
        res = requests.get(API_URL)
        if res.status_code == 200:
            return pd.DataFrame(res.json())
        else:
            st.error("❌ Fehler beim Laden der Geräte.")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Verbindungsfehler zur API: {e}")
        return pd.DataFrame()

device_df = load_devices()

# --- Geräte anzeigen ---
st.subheader("🖥️ Geräteübersicht")
if not device_df.empty:
    st.dataframe(device_df)
else:
    st.info("Keine Geräte vorhanden.")

# --- Gerät hinzufügen ---
st.subheader("➕ Neues Gerät hinzufügen")
with st.form("add_form"):
    name = st.text_input("Gerätename")
    serial = st.text_input("Seriennummer")
    user = st.text_input("Benutzer")
    submit = st.form_submit_button("Hinzufügen")
    if submit:
        payload = {"name": name, "serialNumber": serial, "user": user}
        try:
            resp = requests.post(API_URL, json=payload)
            if resp.status_code == 201:
                st.success("✅ Gerät hinzugefügt.")
                st.rerun()
            else:
                st.error(f"❌ Fehler beim Hinzufügen: {resp.status_code}")
        except Exception as e:
            st.error(f"Verbindungsfehler: {e}")

# --- Gerät aktualisieren / löschen ---
st.subheader("🛠️ Gerät bearbeiten oder löschen")
if not device_df.empty:
    options = {
        f"{row['id']}: {row['name']} ({row['serialNumber']})": row['id']
        for _, row in device_df.iterrows()
    }
    selected = st.selectbox("Gerät auswählen", list(options.keys()))
    selected_id = options[selected]
    selected_row = device_df[device_df["id"] == selected_id].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✏️ Gerät aktualisieren")
        new_name = st.text_input("Neuer Name", selected_row["name"])
        new_serial = st.text_input("Neue Seriennummer", selected_row["serialNumber"])
        new_user = st.text_input("Neuer Benutzer", selected_row["user"])
        if st.button("✅ Aktualisieren"):
            updated = {
                "name": new_name,
                "serialNumber": new_serial,
                "user": new_user
            }
            try:
                resp = requests.put(f"{API_URL}/{selected_id}", json=updated)
                if resp.status_code == 200:
                    st.success("✅ Gerät aktualisiert.")
                    st.rerun()
                else:
                    st.error(f"Fehler: {resp.status_code}")
            except Exception as e:
                st.error(f"Fehler beim Update: {e}")

    with col2:
        st.markdown("### 🗑️ Gerät löschen")
        if st.button("❌ Löschen bestätigen"):
            try:
                resp = requests.delete(f"{API_URL}/{selected_id}")
                if resp.status_code == 200:
                    st.success("✅ Gerät gelöscht.")
                    st.rerun()
                else:
                    st.error(f"Fehler: {resp.status_code}")
            except Exception as e:
                st.error(f"Fehler beim Löschen: {e}")
else:
    st.info("Keine Geräte verfügbar zum Bearbeiten oder Löschen.")

# --- Live API-Monitoring ---
st.subheader("📈 Live API-Antwortzeiten")

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
    try:
        res = requests.post(url, headers=headers, json={"query": kql})
        if res.status_code == 200:
            data = res.json()
            rows = data['tables'][0]['rows']
            df = pd.DataFrame(rows, columns=["timestamp", "duration"])
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df["duration"] = df["duration"].astype(float)
            return df.sort_values("timestamp")
        else:
            st.error(f"Fehler beim Abrufen der Insights: {res.text}")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Verbindungsfehler zu Insights: {e}")
        return pd.DataFrame()

df_insights = query_application_insights()
if not df_insights.empty:
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(df_insights["timestamp"], df_insights["duration"], marker="o")
    ax.set_title("Antwortzeiten der letzten API-Requests")
    ax.set_ylabel("Dauer (ms)")
    ax.set_xlabel("Zeit")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
else:
    st.info("Noch keine Insights-Daten oder keine Zugriffe.")

# --- Footer ---
st.markdown("---")
st.caption("M300 Projekt – Inventar API Dashboard mit Login & Monitoring")
