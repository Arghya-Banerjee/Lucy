import pyttsx3


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

if __name__ == '__main__':

    pass
