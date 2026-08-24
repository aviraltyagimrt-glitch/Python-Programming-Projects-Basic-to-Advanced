import win32api
import time
import win32com.client
names = ["Aviral"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")
for i in names:
    time.sleep(7)
    reminder = f"This a reminder to drink a glass of water {i}"
    print(f"This a Reminder to drink a glass of water {i}")
    speaker.Speak(reminder)

