import schedule
import os
import time

def Display(Text):
    print(Text)

def main():
    Content = input("Enter Message : ")
    Time = int(input("Enter Time interval in seconds : "))

    if Time == 1:
        schedule.every(Time).second.do(Display,Content)

    else :
        schedule.every(Time).seconds.do(Display,Content)


    sleep_t = 70/100 * Time

    while True:
        schedule.run_pending()
        time.sleep(sleep_t)

if __name__ == "__main__":
    main()