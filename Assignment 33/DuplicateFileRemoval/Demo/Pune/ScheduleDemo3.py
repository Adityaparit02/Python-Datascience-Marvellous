import schedule
import time
import datetime

def display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    print("Automation Script Started")
    schedule.every(1).minute.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)       #1 second
        
    print("End of Automation Script")

if __name__ =="__main__":
    main() 