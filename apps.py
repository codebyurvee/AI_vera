import subprocess
import webbrowser
from assistant import speak

APPS = {
    # Web
    "youtube":      lambda: webbrowser.open("https://youtube.com"),
    "google":       lambda: webbrowser.open("https://google.com"),
    "instagram":    lambda: webbrowser.open("https://instagram.com"),
    "whatsapp":     lambda: webbrowser.open("https://web.whatsapp.com"),
    "gmail":        lambda: webbrowser.open("https://mail.google.com"),
    "github":       lambda: webbrowser.open("https://github.com"),
    "chatgpt":      lambda: webbrowser.open("https://chatgpt.com"),
    "netflix":      lambda: webbrowser.open("https://netflix.com"),
    "spotify":      lambda: webbrowser.open("https://open.spotify.com"),
    "linkdin":      lambda: webbrowser.open("https://open.linkdin.com"),

    # System Apps
    "notepad":      lambda: subprocess.Popen("notepad.exe"),
    "calculator":   lambda: subprocess.Popen("calc.exe"),
    "paint":        lambda: subprocess.Popen("mspaint.exe"),
    "task manager": lambda: subprocess.Popen("taskmgr.exe"),
    "camera":       lambda: subprocess.Popen("start microsoft.windows.camera:", shell=True),

    # Dev Tools
    "vs code":      lambda: subprocess.Popen("code", shell=True),
    "terminal":     lambda: subprocess.Popen("start cmd", shell=True),

    # Folders
    "downloads":    lambda: subprocess.Popen("explorer shell:Downloads", shell=True),
    "documents":    lambda: subprocess.Popen("explorer shell:Documents", shell=True),
    "desktop":      lambda: subprocess.Popen("explorer shell:Desktop", shell=True),
}

def open_app(app_name):
    app_name = app_name.lower().strip()
    if app_name in APPS:
        APPS[app_name]()
        speak(f"Opening {app_name}!")
        return True
    for key in APPS:
        if key in app_name or app_name in key:
            APPS[key]()
            speak(f"Opening {key}!")
            return True
    speak(f"Sorry, I couldn't find {app_name}!")
    return False