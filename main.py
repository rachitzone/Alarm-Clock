import time
from playsound import playsound
from datetime import datetime
alarmtime = "18:46"
while True:
    lcltime = datetime.now().strftime('%H:%M')
    if lcltime == alarmtime:
        playsound("Alarm.mp3")
        break

    else:
        print("Not yet!")
        time.sleep(10)