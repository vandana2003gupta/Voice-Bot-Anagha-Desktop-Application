# -*- coding: utf-8 -*-
"""
Voice Assistant: Anagha (Final Version)
Features:
- Outlook email (multi-recipient + spam count)
- Reminder (voice or fallback text)
- News (category + headline count)
- Voice recognition with text fallback
- Word2Number support for spoken numbers
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import os
import webbrowser
import sys
import threading
import time
import smtplib
import psutil
import pyautogui
from word2number import w2n
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize core components
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

talk_lock = threading.Lock()  # ✅ Fix for NameError

# Speak function
def engine_talk(text):
    print(f"Anagha: {text}")
    with talk_lock:
        engine.say(text)
        engine.runAndWait()

# Get user input (fallback to text if needed)
def get_input(prompt):
    engine_talk(prompt)
    response = user_commands()
    if not response:
        engine_talk("I couldn't understand. Please type it.")
        response = input(f"{prompt}: ")
    return response.strip()

# Weather API integration
def weather(city):
    api_key = "bcde558ca3fe60ab9793019b415bcfcf"  # Replace with your actual key
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}"
    try:
        data = requests.get(url).json()
        if data.get("cod") != 200:
            return f"Sorry, I couldn't find the weather for {city}."
        temp_celsius = round(data["main"]["temp"] - 273.15, 2)
        return f"The current temperature in {city} is {temp_celsius} degrees Celsius."
    except:
        return "Error fetching weather data."

# Set voice-based reminder
def set_reminder(message, delay):
    def reminder():
        time.sleep(delay)
        engine_talk(f"Reminder: {message}")
    threading.Thread(target=reminder).start()

# Send email via Outlook
def send_email(to_list, subject, body, count):
    sender = "vandana.22b1541061@abes.ac.in"
    password = "16122003@UTKk"  # 🔐 Use env variable in production
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            for i in range(count):
                for to in to_list:
                    server.sendmail(sender, to, message)
        engine_talk(f"Email sent to all recipients {count} time(s).")
    except Exception as e:
        engine_talk("Failed to send email.")
        print(f"[ERROR] {e}")

# Fetch news headlines
def get_news(category, count):
    api_key = "5bf9eef1cdce4dcc8ae1a36dfef67e4d"
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api_key}"
    try:
        articles = requests.get(url).json().get("articles", [])[:count]
        headlines = [article["title"] for article in articles]
        return headlines
    except:
        return []

# Control system volume
def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100.0, None)

# Get battery and power info
def system_info():
    battery = psutil.sensors_battery()
    return f"Battery is at {battery.percent} percent. Charging: {'Yes' if battery.power_plugged else 'No'}"

# Capture voice command
def user_commands():
    command = ""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if "anagha" in command:
                command = command.replace("anagha", "").strip()
                print(f"Command: {command}")
    except:
        pass
    return command

# Core assistant functionality
def run_anagha():
    command = user_commands()

    if "play a song" in command:
        engine_talk("Playing a song from YouTube")
        pywhatkit.playonyt("Arijit Singh")

    elif "play" in command:
        song = command.replace("play", "")
        engine_talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        engine_talk("The current time is " + datetime.datetime.now().strftime("%I:%M %p"))

    elif any(x in command for x in ["who is", "what is", "explain"]):
        term = command.replace("who is", "").replace("what is", "").replace("explain", "").strip()
        engine_talk(wikipedia.summary(term, 1))

    elif "joke" in command:
        engine_talk(pyjokes.get_joke())

    elif "weather" in command:
        city = get_input("Which city?")
        engine_talk(weather(city))

    elif "google" in command:
        engine_talk("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "notepad" in command:
        os.system("notepad.exe")

    elif "reminder" in command:
        message = get_input("What should I remind you about?")
        delay_text = get_input("In how many seconds?")
        try:
            delay = w2n.word_to_num(delay_text)
            set_reminder(message, delay)
            engine_talk(f"Reminder set for {delay} seconds.")
        except:
            engine_talk("Sorry, I couldn't understand the delay time.")

    elif "email" in command:
        to_raw = input("Enter recipient emails (comma-separated): ").strip()
        to_list = [email.strip() for email in to_raw.split(",") if email.strip()]
        subject = get_input("What's the subject?")
        body = get_input("What should I say?")
        count_text = get_input("How many times should I send the email?")
        try:
            count = w2n.word_to_num(count_text)
            send_email(to_list, subject, body, count)
        except:
            engine_talk("Invalid email count.")

    elif "news" in command:
        category = get_input("Which topic? (like technology, sports, entertainment)")
        count_text = get_input("How many headlines should I read?")
        try:
            count = w2n.word_to_num(count_text)
            headlines = get_news(category, count)
            if headlines:
                engine_talk(f"Top {count} {category} news headlines:")
                for headline in headlines:
                    engine_talk(headline)
            else:
                engine_talk("No news found.")
        except:
            engine_talk("Invalid number of headlines.")

    elif "battery" in command or "system info" in command:
        engine_talk(system_info())

    elif "screenshot" in command:
        pyautogui.screenshot().save("screenshot.png")
        engine_talk("Screenshot taken and saved.")

    elif "volume" in command:
        level_text = get_input("What volume level from 0 to 100?")
        if level_text.isdigit():
            set_volume(int(level_text))
            engine_talk(f"Volume set to {level_text} percent.")

    elif "voice" in command:
        choice = get_input("Say male or female.")
        if "male" in choice:
            engine.setProperty("voice", voices[0].id)
        elif "female" in choice:
            engine.setProperty("voice", voices[1].id)
        engine_talk("Voice changed.")

    elif "stop" in command or "exit" in command:
        engine_talk("Goodbye!")
        sys.exit()

    else:
        engine_talk("I didn’t catch that. Please try again.")

# Main entry point
if __name__ == "__main__":
    engine_talk("Hello, I am Anagha, your assistant. How can I help you today?")
    while True:
        run_anagha()
