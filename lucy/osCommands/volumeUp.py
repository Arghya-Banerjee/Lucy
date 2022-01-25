import pyautogui
from lucy.main import takeCommand

def volumeUp(query):

    # Example query :
    # Volume up by 20

    query_str = str(query)
    query_str_lower = query_str.lower()
    query_broken = query_str_lower.split("volume up by ")

    vol_amt = int(query_broken[1])

    for i in range(0,vol_amt):
        pyautogui.press('volumeup')


    print(query_broken)

if __name__ == '__main__':


    sub = takeCommand().lower()

    volumeUp(sub)