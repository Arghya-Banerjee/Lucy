import speech_recognition as sr

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


if __name__ == '__main__':

    pass