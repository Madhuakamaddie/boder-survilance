# utils.py
import smtplib
import platform
import os

def send_email_alert(zone, motion, ir, heat):
    sender_email = "vellurumadhusri@gmail.com"
    sender_password = "plux nnps emsm hqrk"  # 16-character Gmail App Password
    receiver_email = "madhusrivelluru@gmail.com"

    subject = "🔴 Border Intrusion Alert!"
    body = f"Intrusion detected at Zone {zone}.\nMotion: {motion}\nIR Sensor: {ir}\nTemperature: {heat}°C\nTake immediate action."

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(f"Email failed: {e}")

def play_sound_alert():
    if platform.system() == "Windows":
        import winsound
        duration = 800  # milliseconds
        freq = 1000  # Hz
        winsound.Beep(freq, duration)
    elif platform.system() == "Darwin":
        os.system("say 'Intrusion detected'")
    else:
        os.system("paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga")
