import schedule
import time

def display():
    print("Namaskar...")

def main():

    schedule.every().day.at("09:00").do(display)

    while True:
        schedule.run_pending()
        time.sleep(89700)
        
if __name__ == "__main__":
    main()