# import win32api
# import win32com.client
# names = ["Aviral"]
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# for i in names:
#     time.sleep(7)
#     reminder = f"This a reminder to drink a glass of water {i}"
#     print(f"This a Reminder to drink a glass of water {i}")
#     speaker.Speak(reminder)

import time
from plyer import notification
name = input("Enter your name\n")
i = 1
while (i<1):
    time.sleep(3600)
    notification.notify(title = "Reminder",message = f"This is a reminder to drink water {name}",timeout=4)
    i = i+1