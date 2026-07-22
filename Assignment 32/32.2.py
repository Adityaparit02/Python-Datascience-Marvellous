import os
import schedule
import time
import sys

def SizeMonitor(FileName):

    TimeStamp = time.ctime()
    File_Path= os.path.abspath(FileName)
    File_Size = os.path.getsize(FileName)


    log_File_Name = "FileSizeLog.txt"
    Log_File_Path= os.path.abspath(log_File_Name)
    ret = os.path.exists(Log_File_Path)
    print("_"*50)
    print(f"The File : {File_Path}")
    print("Will be scanned every 30 seconds..")
    print(f"The Current Size is :{File_Size}")
    print("All File Size Updates will be logged in FileSizeLog.txt")


    fobj = open(Log_File_Path,"a")
    fobj.write("\n")
    fobj.write(f"File Path : {File_Path} \n")
    fobj.write(f"File Size : {File_Size} Bytes \n")
    fobj.write("_"*40+"\n")
    fobj.write(f"Date and Time : {TimeStamp} \n")
    fobj.write("\n")
    fobj.write("#"*100+"\n")
    fobj.write("\n")
    fobj.close()

def main():
    FileName= sys.argv[1]
    schedule.every(30).seconds.do(SizeMonitor,FileName)

    while True :
        schedule.run_pending()
        time.sleep(20)

if __name__ == "__main__":
    main()
