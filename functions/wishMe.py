import datetime
from functions.speak import speak

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


if __name__ == '__main__':

    pass