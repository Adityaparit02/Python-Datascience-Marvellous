import os
import time
import sys
import psutil
import schedule


def DirectoryMaker(DirectoryName):
    ret = os.path.exists(DirectoryName)

    if ret == False:
        os.makedirs(DirectoryName)

    return DirectoryName


def ProcessScanner():
    Border = "_"*50
    DirectoryName = DirectoryMaker(sys.argv[1])

    timeStamp = time.ctime()
    LogFileName = "LogFile_"+timeStamp+".log"
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    LogFilePath = os.path.join(DirectoryName,LogFileName)
    fobj = open(LogFilePath,"w")
    fobj.write(Border + "\n")
    fobj.write("-----------------Running Processes-----------------\n")
    fobj.write(f"Time : {timeStamp}\n")
    fobj.write(Border + "\n")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        fobj.write(f"PID : {info.get("pid")}\n")
        fobj.write(f"Name : {info.get("name")}\n")
        fobj.write(f"Username : {info.get("username")}\n")
        fobj.write(Border + "\n")


    fobj.write(Border + "\n")
    fobj.write("-----------------End of File-----------------\n")
    fobj.write(f"Time : {timeStamp}\n")
    fobj.write(Border + "\n")
    fobj.close()


def main():
    sys.argv[1]
    
    schedule.every(1).minute.do(ProcessScanner)
    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ =="__main__":
    main()

