import os

def opneCode():
    '''
    opneCode 
    
    Function to open Visual Studio Code
    '''

    path = "C:\\Users\\arghy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(path)

def openDiscord():
    '''
    openDiscord 

    Function to open Discord Application
    '''

    path = "C:\\Users\\arghy\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
    os.startfile(path)

def opneSpotify():
    '''
    opneSpotify 
    
    Function to open Spotify Application
    '''

    path = "C:\\Users\\arghy\\AppData\\Roaming\\Spotify\\Spotify.exe"
    os.startfile(path)

if __name__ == "__main__":

    openDiscord()
    opneCode()
    opneSpotify()
