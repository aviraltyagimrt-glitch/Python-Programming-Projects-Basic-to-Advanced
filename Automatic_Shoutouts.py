import win32api
import time
import win32com.client
names = ["Aviral Tyagi","Rohan","Virat","Messi"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")
print("Starting Shoutouts")
for i in names:
    shoutout = f"Shout out to {i}"
    print(f"{shoutout}")
    speaker.Speak(shoutout)
    time.sleep(1)
print("All shoutouts are Done")