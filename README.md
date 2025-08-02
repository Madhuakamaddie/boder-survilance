# IoT Intrusion Detection Alert System (Software-Only)

This is a software-only simulation of an IoT-based intrusion detection and alerting system. It mimics real-time perimeter defense by monitoring simulated sensor inputs such as motion, infrared (IR), and temperature. When a potential intrusion is detected, the system triggers both an email alert and a sound alarm.

---

## Use Case

This project demonstrates a prototype of a smart security system useful for:
- Defense installations
- Border surveillance
- Remote infrastructure monitoring
- ISRO/DRDO restricted zone simulation

---

## Features

- Smart intrusion detection using conditional logic
- Automatic email alert with custom message
- Sound alarm support for Windows, Linux, and macOS
- Live dashboard with status updates via Streamlit
- No physical sensors or hardware required

---

## Technology Stack

- Python 3.x
- Streamlit (for UI)
- smtplib (for email alerts)
- os, platform
