import os
import time
import pyautogui
import pyperclip
from dotenv import load_dotenv
import google.generativeai as genai
import keyboard

load_dotenv()
api_key = os.getenv("YOUR API KEY")  
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

pyautogui.click(1144, 1046)  
time.sleep(2)

def get_chat_text():
    pyautogui.moveTo(669, 258)
    pyautogui.dragTo(1839, 906, duration=1.5, button='left')
    time.sleep(1)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    return pyperclip.paste()

def get_gemini_reply(chat_history):
 
    prompt = f"""
Act as a friendly, cheerful, humorous and nonchalant indian boy who is not a coder named Gaurav who speaks Hindi and English.
You are part of the following chat. Reply *only* as if you're continuing the conversation — not summarizing or analyzing:

{chat_history}

Respond naturally as the next message in the conversation like you are Gaurav and respond casually not formally.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Gemini Error]: {str(e)}"

def send_reply_to_chat(reply_text):
    # Copy the reply to clipboard
    pyperclip.copy(reply_text)
    time.sleep(1)

    # Focus input box and send reply
    pyautogui.click(x=1027, y=981)
    time.sleep(0.8)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter")

def main_loop():
    print("🤖 Auto-reply bot started. Press Ctrl+C to stop.")
    while True:
        time.sleep(5)
        chat_text = get_chat_text()
        if not chat_text.strip():
            print("No text selected. Skipping...")
            continue

        print("\n📨 Chat Text:\n", chat_text)

        reply = get_gemini_reply(chat_text)
        print("\n💬 Gemini Reply:\n", reply)

        send_reply_to_chat(reply)
        time.sleep(12)
        def main_loop():
            print("🤖 Auto-reply bot started. Press ESC to stop.")
        while True:
            if keyboard.is_pressed('esc'):
                print("\n🛑 Stopping... ESC key pressed.")
                break

if __name__ == "__main__":
    main_loop()
