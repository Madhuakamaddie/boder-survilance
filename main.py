# main.py
import streamlit as st
from utils import send_email_alert, play_sound_alert
import random
import time

st.set_page_config(page_title="IoT Border Surveillance", layout="centered")
st.title("🛡️ IoT Intrusion Detection for Border Surveillance")
st.markdown("---")

# Simulated sensor data function
def simulate_sensor_data():
    motion_detected = random.choice([True, False])
    ir_detected = random.choice([True, False])
    heat_level = random.randint(25, 45)
    zone = random.randint(1, 5)
    return motion_detected, ir_detected, heat_level, zone

# Function to handle alert
def handle_alert(motion, ir, heat, zone):
    alert_msg = f"🔴 ALERT: Intrusion detected at Zone {zone} | Motion: {motion} | IR: {ir} | Heat: {heat}°C"
    st.error(alert_msg)
    send_email_alert(zone, motion, ir, heat)
    play_sound_alert()
    st.success("Email & Sound Alert Sent!")

# Live Simulation
if st.button("▶️ Start Simulation"):
    st.info("Monitoring sensors... Press Stop or Refresh to end.")
    placeholder = st.empty()

    while True:
        motion, ir, heat, zone = simulate_sensor_data()
        placeholder.markdown(f"📡 Zone: {zone} | Motion: `{motion}` | IR: `{ir}` | Heat: `{heat}°C`")

        if motion and ir and heat > 37:
            handle_alert(motion, ir, heat, zone)
            break

        time.sleep(2)

# Manual Trigger Button
st.markdown("---")
if st.button("🚨 Trigger Test Alert"):
    motion, ir, heat, zone = True, True, 39, 3
    handle_alert(motion, ir, heat, zone)
