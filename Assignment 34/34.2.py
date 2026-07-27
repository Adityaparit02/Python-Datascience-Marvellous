import time
import os
import psutil
import schedule

def RunningProcessScan():
    DirectoryName = "34.2_LogFiles" 
    Border = "_"*50
    ret = os.path.exists(DirectoryName)

    if ret == False:
        os.makedirs(DirectoryName)

    timeStamp = time.ctime()
    LogFileName = "LogFile_"+timeStamp+".log"
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    LogFilePath = os.path.join(DirectoryName, LogFileName)

    fobj = open(LogFilePath,"w")
    fobj.write(Border + "\n")
    fobj.write("-----------------Running Processes-----------------\n")
    fobj.write(f"Time : {timeStamp}\n")
    fobj.write(Border + "\n")


    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["name","status"])

        if info.get("status") == "running":
            fobj.write(f"Name : {info.get("name")}\n")
            fobj.write(f"status : {info.get("status")}\n")
            fobj.write(Border + "\n")

    fobj.write(Border + "\n")
    fobj.write("-----------------End of File-----------------\n")
    fobj.write(f"Time : {timeStamp}\n")
    fobj.write(Border + "\n")
    fobj.close()


def main():
    schedule.every(1).minute.do(RunningProcessScan)

    while True:
        schedule.run_pending()
        time.sleep(5)

        
if __name__ == "__main__":
    main()