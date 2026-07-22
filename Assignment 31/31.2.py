import schedule
import time

def DisplayMessage(Message):
    print(Message)

def main():
    Message = input("Enter your Message: ")
    schedule.every(5).seconds.do(DisplayMessage,Message)

    while True:
        schedule.run_pending()
        time.sleep(3)

if __name__ =="__main__":
    main()
