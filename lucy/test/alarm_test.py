import datetime
import plyer

def alarm(desH, desM):

    nowH = datetime.datetime.now().hour
    nowM = datetime.datetime.now().minute

    if nowH == desH and nowM == desM:

        plyer.notification.notify(
        title="Alarm You Set",
        message="This is your alarm",
        timeout=5
    )


if __name__ == '__main__':

    desH = int(input("Hour of your alarm?"))
    desM = int(input("Minute of your alarm?"))

    while True:

        alarm(desH, desM)
        break




   