ChatterBuddy — AI-Powered Auto-Reply Bot
ChatterBuddy is an automated chat responder bot built using Python and Google’s Gemini generative AI. It reads chat text from the screen, generates natural, casual replies in a friendly, conversational style, and types them back automatically — enabling seamless AI-driven chat interaction without manual typing.

Description
ChatterBuddy leverages Google Gemini's language model API to act as a friendly, humorous conversational partner named "Gaurav" — an Indian boy who speaks Hindi and English casually. The bot captures chat messages by simulating mouse and keyboard actions, sends them to Gemini for response generation, and pastes the AI-generated reply back into the chat interface automatically.

This system uses:

Python automation with pyautogui and pyperclip for screen interaction

Keyboard event monitoring to allow graceful bot termination

Google Gemini API for advanced conversational AI replies

Environment variables for securely managing API keys

Features
Automated detection and copying of chat messages from the screen

AI-generated replies mimicking a casual, bilingual conversational style

Automatic pasting and sending of generated replies

Runs in a loop with configurable intervals between replies

Stops gracefully on user command (press ESC)

Technologies Used
Python

pyautogui for mouse and keyboard control

pyperclip for clipboard management

keyboard for detecting keypress events

dotenv for environment variable management

Google Gemini API for natural language generation

Usage
Configure your Google Gemini API key in a .env file as YOUR_API_KEY=your_actual_api_key

Run the script to start the auto-reply bot

Make sure the chat window is visible and accessible on the screen

To stop the bot, press the ESC key

Use Cases
Automating replies in chat applications for demos or social experiments

Creating a friendly AI chatbot assistant on your desktop

Learning and experimenting with AI-driven automation and screen control
