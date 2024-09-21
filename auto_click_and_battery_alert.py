import psutil
import time
from plyer import notification
import pyautogui
import threading

# Disabilita il fail-safe di PyAutoGUI
pyautogui.FAILSAFE = False

def check_battery():
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged
        
        if percent < 51 and not plugged:
            notification.notify(
                title="Batteria Scarica",
                message=f"La batteria è al {percent}%. Collega il caricatore!",
                timeout=10  # Durata della notifica in secondi
            )

        # if percent > 97 and plugged:
        #     notification.notify(
        #         title="Batteria Carica",
        #         message=f"La batteria è al {percent}%. Scollega il caricatore!",
        #         timeout=10  # Durata della notifica in secondi
        #     )

        if percent == 100 and plugged:
            notification.notify(
                title="Batteria Carica",
                message=f"La batteria è al {percent}%. Scollega il caricatore!",
                timeout=10  # Durata della notifica in secondi
            )
        

        if percent < 51 and not plugged:
            time.sleep(600)  # Controlla ogni 600 secondi
        # if percent > 97 and plugged:
        #     time.sleep(1200) # Controlla ogni 1200 secondi
        if percent == 100 and plugged:
            time.sleep(1800) # Controlla ogni 1800 secondi
        else:
            time.sleep(60)  # Controlla ogni 60 secondi

def auto_click():
    while True:
        pyautogui.press('scrolllock')
        print("Clicked a button")
        time.sleep(4 * 60 + 30)  # Attendere 4 minuti e 30 sec

if __name__ == "__main__":
    battery_thread = threading.Thread(target=check_battery)
    click_thread = threading.Thread(target=auto_click)

    battery_thread.start()
    click_thread.start()

    battery_thread.join()
    click_thread.join()
