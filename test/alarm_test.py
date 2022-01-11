import datetime
from typing_extensions import IntVar
import plyer

def alarm(desH, desM):

    nowH = datetime.datetime.now().hour
    nowM = datetime.datetime.now().minute
    



if __name__ == '__main__':

    
    desH = int(input("Hour of your alarm?"))
    desM = int(input("Minute of your alarm?"))


    plyer.facades.notification.notify(
        title="Alarm You Set",
        message="This is your alarm",
        timeout=5
    )