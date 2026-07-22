import schedule
import time

def Monday():
    print("Start Your Weekly Goals : ")
    print(time.ctime())

def Wednesday():
    print("Review your weekly progress")
    print(time.ctime())


def Friday():
    print("weekly Work Completed")
    print(time.ctime())


def main():
    schedule.every().monday.at("09:00").do(Monday)
    schedule.every().wednesday.at("17:00").do(Wednesday)
    schedule.every().friday.at("18:00").do(Friday)



    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()


