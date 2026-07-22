import schedule
import time

def Lunch():
    print("Lunch Time !")

def Wrap():
    print("Wrap up work..")

def main():
    schedule.every().day.at("13:00").do(Lunch)
    schedule.every().day.at("18:00").do(Wrap)

    while True:
        schedule.run_pending()
        time.sleep(17980)

if __name__ =="__main__":
    main()