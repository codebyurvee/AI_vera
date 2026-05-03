import json
import os
from dotenv import load_dotenv
from google import genai
from assistant import speak

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def gemini_understand(command):
    prompt = f"""
You are a smart voice assistant brain. The user said:
"{command}"

Understand the command and respond ONLY in this exact JSON format:
{{
  "action": "open_app | web_search | volume_up | volume_down | mute | write_file | answer | exit",
  "app_name": "app name if open_app, else null",
  "query": "search query if web_search, else null",
  "filename": "filename.txt if write_file, else null",
  "content": "file content if write_file, else null",
  "answer": "reply if action is answer, else null"
}}

Rules:
- If user wants to open anything → open_app
- If user asks a question or wants a joke/story → answer
- If user says exit/goodbye/stop → exit
- Keep answers short and friendly
- Respond in English
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        raw = response.text.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        return json.loads(raw)
    except Exception as e:
        print(f"Gemini error: {e}")
        return {"action": "answer", "answer": "Sorry, I didn't understand that!"}