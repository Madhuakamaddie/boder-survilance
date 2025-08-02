import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("data/intrusions.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        zone TEXT,
        motion INTEGER,
        infrared INTEGER,
        heat REAL,
        intrusion INTEGER,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()

def insert_log(data):
    conn = sqlite3.connect("data/intrusions.db")
    c = conn.cursor()
    c.execute('''INSERT INTO logs (zone, motion, infrared, heat, intrusion, timestamp)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (data['zone'], int(data['motion']), data['infrared'],
               data['heat'], int(data['intrusion']),
               datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
