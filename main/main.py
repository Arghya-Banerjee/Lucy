import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pandas as pd
import pyautogui
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 190)


# Text to speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Taking speech and converting to text


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to ur beautiful Voice....")
        r.pause_threshold = 1.0
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query, "\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query


# Wishing Function for Lucy


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!!")

    else:
        speak("Good Evening Sir!!")

    speak("What may I do for you sir?")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("arghya17112002@gmail.com", "Google_2020")
    server.sendmail("arghya17112002@gmail.com", to, content)
    server.close()


# Main program for Lucy

if __name__ == "__main__":

    WishMe()

    while True:

        query = takeCommand().lower()

        # Searching Wikipedia

        if "offline" in query:
            speak("Going offline Sir")
            quit()

        elif "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # Opening other links

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Sir, what should I search on google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open hackerrank" in query:
            webbrowser.open("hackerrank.com")

        elif "the time now" in query:
            nowTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The time now is {nowTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\arghy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open spotify" in query:
            spotifyPath = "C:\\Users\\arghy\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)

        elif "open discord" in query:
            discordPath = "C:\\Users\\arghy\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
            os.startfile(discordPath)

        elif "send email to arghya" in query:
            try:
                speak("What should I say in the email?")
                content = takeCommand()
                to = "arghya.banerjee.dev@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir")

            except Exception as e:
                print(e)
                speak("Unable to send this email Sir")
                
        elif "who are you" in query or "what are you" in query:
            speak("I am Lucy sir. I am a virtual assisstant made by my master to ease him in his daily tasks")
            
            
        elif "take a screenshot" in query or "take screenshot" in query or "screenshot this" in query:
            speak("What should I name the file sir?")
            name = takeCommand().lower()
            speak("Taking screenshot..")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot taken sir!")
            
            
            
        elif "volume up a bit" in query:
            pyautogui.press('volumeup')
            
        elif "volume up a bit" in query:
            pyautogui.press('volumedown')
            
