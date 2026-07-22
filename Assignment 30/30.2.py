import schedule
import time

def displaytime():
    CTime = time.localtime()
    FormattedTime = time.strftime("%d - %m - %y %I:%M:%S %p",CTime)
    print("Current Date and Time : ",FormattedTime)


def main():
    schedule.every(1).minute.do(displaytime)

    while True:
        schedule.run_pending()
        time.sleep(45)

if __name__ == "__main__":
    main()

