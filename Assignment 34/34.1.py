import psutil
import os
import time
import schedule

def ProcessScanner():
    Border = "_"*50


    DirectoryName = "34.1_LogFiles"
    ret = os.path.exists(DirectoryName)

    if ret == False:
        os.makedirs(DirectoryName)

    timeStamp = time.ctime()
    LogFileName = "LogFile_"+timeStamp+".log"
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    LogFilePath = os.path.join(DirectoryName, LogFileName)

    fobj = open(LogFilePath,"w")
    fobj = open(LogFilePath,"w")
    fobj.write(Border + "\n")
    fobj.write("-----------------Running Processes-----------------\n")
    fobj.write(f"Time : {timeStamp}\n")
    fobj.write(Border + "\n")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["name","pid","username"])
        
        fobj.write(f"Name : {info.get('name')}\n")
        fobj.write(f"pid : {info.get('pid')}\n")
        fobj.write(f"username : {info.get('username')}\n")
        fobj.write(Border + "\n")


    fobj.write(Border + "\n")
    fobj.write("-----------------End of File-----------------\n")
    fobj.write(f"Time : {timeStamp}\n")
    fobj.write(Border + "\n")
    fobj.close()

def main():
    schedule.every(1).minute.do(ProcessScanner)

    while True:
        schedule.run_pending()
        time.sleep(5)
        
if __name__=="__main__":
    main()