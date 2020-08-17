import os
import time
import winsound
from playsound import playsound


def playSound():
    repeat = 1

    for i in range(repeat):
        for j in range(9):
            playsound("alarm.mp3")
            # winsound.MessageBeep(-1)
        time.sleep(2)


def createAlarm(n):
    print()
    print("You'll here the alarm in:", n, "seconds.")
    time.sleep(n)
    playSound()


def setTime(user_input):
    if user_input == '1':

        user_input = int(input("Enter the desired hours: "))
        wait_time = (user_input * 60) * 60
        createAlarm(wait_time)

    elif user_input == '2':

        user_input = int(input("Enter the desired minutes: "))
        wait_time = user_input * 60
        createAlarm(wait_time)

    elif user_input == '3':

        user_input = int(input("Enter the desired seconds: "))
        wait_time = user_input
        createAlarm(wait_time)

    elif user_input == '4':

        hours = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))

        wait_time = ((hours * 60) * 60) + (minutes * 60) + seconds
        createAlarm(wait_time)

    else:
        try:
            os.system('cls')  # If OS is Windows
            main()
        except:
            os.system('clear')  # If OS is Linux or Mac
            main()


def main():
    """
    Main function
    - Get user's time
    - Set alarm
    """

    print("-- Alarm --\n")

    print("What unit of time do you want to wait?\n "
          "(1) Hours\n "
          "(2) Minutes\n "
          "(3) Seconds\n "
          "(4) Combination")
    value = input("> ")

    setTime(value)

    return


if __name__ == '__main__':
    main()
