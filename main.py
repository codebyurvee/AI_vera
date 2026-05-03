from assistant import speak, listen
from security import wait_for_wake_word, verify_pin
from apps import open_app
from actions import control_volume, web_search, write_file
from brain import gemini_understand

def handle_command(command):
    if not command:
        return True

    result = gemini_understand(command)
    action = result.get("action", "answer")
    print(f"🧠 Vera: {action}")

    if action == "open_app":
        open_app(result.get("app_name", ""))

    elif action == "web_search":
        web_search(result.get("query", command))

    elif action == "volume_up":
        control_volume("up")

    elif action == "volume_down":
        control_volume("down")

    elif action == "mute":
        control_volume("mute")

    elif action == "type_text":
        text = result.get("content", "")
        type_in_active_window(text)

    elif action == "write_file":
        write_file(
            result.get("filename", "note.txt"),
            result.get("content", "")
        )

    elif action == "answer":
        answer = result.get("answer", "")
        speak(answer if answer else "I don't know the answer to that!")

    elif action == "exit":
        speak("Goodbye! Have a great day!")
        return False

    return True

# ── Main Loop ──────────────────────────────────────
while True:
    wait_for_wake_word()

    if not verify_pin():
        speak("Access denied. Going back to sleep.")
        continue

    speak("I'm ready! Say 'goodbye' when done.")
    while True:
        command = listen()
        if command:
            should_continue = handle_command(command)
            if not should_continue:
                speak("Going back to sleep. Say 'hey assistant' to wake me up!")
                break