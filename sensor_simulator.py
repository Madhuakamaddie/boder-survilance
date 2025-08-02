import random
import time

def generate_sensor_data():
    # Simulate 5 border zones
    zones = ["North Post", "East Gate", "Watchtower 3", "Sector A", "Sector B"]
    motion_detected = random.choice([True, False])
    infrared = random.randint(0, 100)  # Simulated IR sensor value
    heat = random.uniform(20.0, 45.0)  # Temperature in °C
    zone = random.choice(zones)
    
    intrusion = motion_detected and infrared > 70 and heat > 35.0
    return {
        "zone": zone,
        "motion": motion_detected,
        "infrared": infrared,
        "heat": round(heat, 2),
        "intrusion": intrusion
    }
