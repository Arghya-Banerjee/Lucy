import pyttsx3
import speech_recognition as sr
import datetime

def speak(audio):
    '''
    speak - To convert text to voice output

    Args:
        audio (string): What it needs to speak
    '''    

    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 190)

    engine.say(audio)
    engine.runAndWait()


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


def wishMe():
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