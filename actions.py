import os
import webbrowser
import pyautogui
from assistant import speak
import pyautogui
import time


def control_volume(action):
    if action == "up":
        for _ in range(5): pyautogui.press("volumeup")
        speak("Volume increased!")
    elif action == "down":
        for _ in range(5): pyautogui.press("volumedown")
        speak("Volume decreased!")
    elif action == "mute":
        pyautogui.press("volumemute")
        speak("Muted!")

def web_search(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Searching for: {query}")

def write_file(filename, content):
    path = os.path.join(os.path.expanduser("~"), "Desktop", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    speak(f"File {filename} saved to your Desktop!")


def type_in_active_window(text):
    time.sleep(0.5)  # Window focus ke liye wait
    pyautogui.typewrite(text, interval=0.05)
    speak(f"Typed: {text}")