# 🤖💬 ChatterBuddy — Your AI-Powered Auto-Reply Sidekick

**ChatterBuddy** is your personal chat assistant powered by **Google’s Gemini AI**. Built with Python, this smart bot **reads chat messages right off your screen**, cooks up a casual, bilingual (Hindi + English) reply in the voice of “Gaurav” — a friendly Indian guy — and **types it back into the chat for you automatically!**

No hands. No effort. Just chill conversations with AI magic.


## ✨ What Can ChatterBuddy Do?

🔹 Instantly **reads incoming messages** from any visible chat app  
🔹 Crafts **casual, humorous replies** using Google's Gemini API  
🔹 **Types and sends** the response back on its own  
🔹 Understands and switches between **Hindi & English** naturally  
🔹 **Runs in a loop** — you sit back, it keeps chatting  
🔹 Press **ESC** any time to gracefully stop the bot

---

## 🧠 How It Works

Behind the scenes, ChatterBuddy combines Python's screen control tools with the Gemini AI model:

1. **Captures** the chat text using `pyautogui` and `pyperclip`
2. **Generates a response** in the voice of "Gaurav" via the Gemini API
3. **Simulates typing** and sends the reply automatically
4. **Listens** for the ESC key so you can stop it any time

---

## 🛠️ Tech Stack

| Tool            | Purpose                                  |
|-----------------|-------------------------------------------|
| `pyautogui`     | Mouse/keyboard control                    |
| `pyperclip`     | Clipboard access for copying/pasting text|
| `keyboard`      | Detect keypresses (like ESC)              |
| `dotenv`        | Securely manage your API key              |
| **Gemini API**  | Generate AI responses in natural language |

--
