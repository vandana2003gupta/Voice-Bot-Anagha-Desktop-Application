# 🎙️ Voice Assistant: Anagha (Desktop Application)

Anagha is an intelligent, Python-based desktop voice assistant designed to simplify everyday tasks using voice commands. With natural voice interaction, it can send emails, set reminders, fetch news, tell jokes, report weather, control system volume, and more.

---

## Features

| Feature                      | Description                                                                |
|----------------------------- |----------------------------------------------------------------------------|
| 🔊 Voice Commands           | Trigger Anagha with "Anagha" and speak your command                         |
| 📧 Email Integration        | Send emails via Outlook to multiple recipients                              |
| ⏰ Reminders                | Set voice-based reminders with flexible time delays                         |
| 📰 News Headlines           | Get top news in categories like technology, sports, and entertainment       |
| 🌦️ Weather Reports          | Fetch real-time weather info for any city                                   |
| 🎵 Play Music               | Search and play songs on YouTube                                            |
| 🕐 Time & Wikipedia         | Get current time or short Wikipedia summaries                               |
| 🖼️ Screenshots              | Take and save screenshots with voice commands                               |
| 🔋 System Info              | Get battery and charging status                                             |
| 🔊 Volume Control           | Adjust system volume between 0–100%                                         |
| 🗣️ Voice Gender Switch      | Choose between male and female voice output                                 |

---

## Tech Stack

| Category             | Libraries / Tools                            |
|----------------------|----------------------------------------------|
| Speech Recognition   | `speech_recognition`, `pyttsx3`              |
| NLP & Utilities      | `wikipedia`, `word2number`, `pyjokes`        |
| Email Handling       | `smtplib` with Outlook SMTP                  |
| News API             | [NewsAPI.org](https://newsapi.org)           |
| Weather API          | [OpenWeatherMap](https://openweathermap.org) |
| Audio Control        | `pycaw`, `psutil`, `pyautogui`               |
| UI Tools             | CLI + `pywhatkit`, `os`, `webbrowser`        |
| Packaging (optional) | `pyinstaller` / `auto-py-to-exe`             |

---

## How to Download & Install the Application

You can use the application directly without writing or executing any code. Here's how:

### Step-by-Step Guide:

1. Visit the **[Releases Page](https://github.com/vandana2003gupta/Voice-Bot-Anagha-Desktop-Application/releases)** of this repository.
2. Under the latest release, you'll find two files:
   - `VoiceBotInstaller.exe` – *(Recommended)* Full installer version. Just download and install.
   - `Voice_Bot_Spyder.exe` – *(Portable)* No installation needed. Just double-click and use.
3. Once downloaded:
   - For the installer:
     - Double-click `VoiceBotInstaller.exe`
     - Follow the installation wizard
     - After install, search **"Voice Bot Anagha"** from the Start menu to launch
   - For the portable `.exe`:
     - Just double-click `Voice_Bot_Spyder.exe` to run the app directly

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/vandana2003gupta/Voice-Bot-Anagha-Desktop-Application.git
cd Voice-Bot-Anagha-Desktop-Application
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Assistant
```bash
python Voice_Bot_Spyder.py
```

## Example Commands

Say This	What Happens

"Anagha, play a song"	Plays random song on YouTube
"Anagha, what is machine learning"	Gives a brief Wikipedia explanation
"Anagha, set a reminder"	Prompts message and delay in seconds
"Anagha, send email"	Asks for recipient, subject, body, repeat
"Anagha, show sports news"	Reads top sports headlines aloud
"Anagha, take screenshot"	Saves screenshot to project directory
"Anagha, system info"	Reports battery level and charging status


## system 

```
+-------------------+
|   User (Voice)    |
+-------------------+
          |
          v
+-------------------+
| Wake Word: "Anagha"|
+-------------------+
          |
          v
+----------------------------+
| Speech Recognition Engine  |
| (speech_recognition)       |
+----------------------------+
          |
          v
+----------------------------+
| NLP & Command Processing   |
| - Wikipedia                |
| - word2number              |
| - pyjokes                  |
+----------------------------+
          |
          v
+----------------------------+
| Task Execution Layer       |
| - Email (smtplib)          |
| - News (NewsAPI)           |
| - Weather (OpenWeatherMap) |
| - Music (pywhatkit)        |
| - System Control (pycaw,   |
|   psutil, pyautogui)       |
+----------------------------+
          |
          v
+----------------------------+
| Voice Response Generator   |
| (pyttsx3 - Male/Female)    |
+----------------------------+
          |
          v
+-------------------+
|   User Output     |
| (Speech + Action) |
+-------------------+

```




