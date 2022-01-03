''' Imports from other modules installed to run Lucy '''

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
from wikipedia.wikipedia import search

''' Imports from web folder containing functions regarding web surfing '''

from web.openGoogle import openGoogle
from web.searchGoogle import searchGoogle   
from web.openYoutube import openYoutube
from web.searchYoutube import searchYoutube

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 190)


def speak(audio):
    '''
    speak - To convert text to voice output

    Args:
        audio (string): What it needs to speak
    '''    

    engine.say(audio)
    engine.runAndWait()


# Taking speech and converting to text


def takeCommand():
    '''
    takeCommand - To convert voice input to text

    Returns:
        [string]: What user said in microphone
    '''

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



def WishMe():
    '''
    WishMe - To wish the user whenever this program starts
    '''  

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Arghya!!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Arghya!!") 

    else:
        speak("Good Evening Arghya!!")

    speak("How may I help you?")


def sendEmail(to, content):
    '''
    sendEmail - To send email to someone

    Args:
        to (string): Email address
        content (string): Content of the email
    '''

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("arghya17112002@gmail.com", "Google_2020")
    server.sendmail("arghya17112002@gmail.com", to, content)
    server.close()



if __name__ == "__main__":

    WishMe()

    while True:

        query = takeCommand().lower()


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
            openYoutube()

        elif "search youtube" in query:
            
            speak("What should I search in youtube sir?")
            searchQuery = takeCommand().lower()

            searchYoutube(searchQuery)

        elif "open google" in query:
            openGoogle()

        elif "search google" in query:
            
            speak("What should I search for sir?")
            searchQuery = takeCommand().lower()

            searchGoogle(searchQuery)


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
                
        elif "who are you" in query or "who are you" in query:
            speak("I am Lucy sir. I am a virtual assisstant made by my master, Arghya, to ease him in his daily tasks")
            
            
        elif "take a screenshot" in query or "take screenshot" in query or "screenshot this" in query:
            speak("What should I name the file sir?")
            name = takeCommand().lower()
            speak("Taking screenshot..")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot taken sir!")
            

        # Volume up and down
            
            
        elif "volume up" in query:
            pyautogui.press('volumeup')
            
        elif "volume down" in query:
            pyautogui.press('volumedown')


        
            
