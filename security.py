from assistant import speak, listen

WAKE_WORD = "hello"
SECRET_PIN = "1234"
MAX_WRONG_ATTEMPTS = 3

def wait_for_wake_word():
    print("\n😴 Sleeping... ")
    while True:
        command = listen(timeout=10)
        if WAKE_WORD in command:
            speak("Hey! i'm Vera, Please say your PIN.")
            return True

def verify_pin():
    wrong = 0
    while wrong < MAX_WRONG_ATTEMPTS:
        pin = listen(timeout=5)
        pin_digits = pin.replace(" ", "")
        if pin_digits == SECRET_PIN:
            speak("Access granted! How can I help you?")
            return True
        else:
            wrong += 1
            remaining = MAX_WRONG_ATTEMPTS - wrong
            if remaining > 0:
                speak(f"Wrong PIN. {remaining} attempts remaining.")
            else:
                speak("Too many wrong attempts. Locking down!")
                return False
    return False