import time
import schedule
import os

def Writer():
    CTime = time.localtime()
    FormattedTime = time.strftime("%d - %m - %y %I:%M:%S %p",CTime)
    fobj = open("Marvellous.txt","a")
    fobj.write(f"Task Excecuted at : {FormattedTime} \n")
    fobj.close()

def main():
    schedule.every(5).minutes.do(Writer)

    while True :
        schedule.run_pending()
        time.sleep(285)

if __name__ == "__main__":
    main()