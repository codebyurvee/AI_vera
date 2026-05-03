import pyttsx3
import speech_recognition as sr

def speak(text):
    print(f"🤖 Vera: {text}")
    engine = pyttsx3.init()  # Har baar naya engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen(timeout=6):
    r = sr.Recognizer()
    r.pause_threshold = 1.5
    r.energy_threshold = 300
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = r.listen(source, timeout=6, phrase_time_limit=8)
            command = r.recognize_google(audio, language="en-IN")
            print(f"👤 You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""