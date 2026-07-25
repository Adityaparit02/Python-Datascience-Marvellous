import schedule
import time
import datetime

def display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    print("Automation Script Started")
    schedule.every(1).minute.do(display)

    #issue

if __name__ =="__main__":
    main() 