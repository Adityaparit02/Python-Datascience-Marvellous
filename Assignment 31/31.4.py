import os
import time
import schedule
import sys


def LogCreator():

    TimeStamp = time.ctime()

    Dir_Name = "log Files 31.4"
    print(f"The Log Files are getting Created in directory : {Dir_Name}")
    Log_File_Name = "Backup%s"%(TimeStamp)+".txt"
    Log_File_Name = Log_File_Name.replace(" ","_")
    Log_File_Name = Log_File_Name.replace(":","_")
    Log_File_Path = os.path.join(Dir_Name,Log_File_Name)
    os.makedirs(Dir_Name,exist_ok=True)

    fobj2 = open(Log_File_Path,"w")
    fobj2.write("_"*40+"\n")
    fobj2.write("Log File Created Successfully."+"\n")
    fobj2.write("Creation Time : "+TimeStamp+"\n")
    fobj2.write("_"*40 +"\n" )

    LogFileName = "Log_of_Logfile_creation.txt"

    fobj4 = open(LogFileName,"a")
    fobj4.write("_"*40+"\n")
    fobj4.write(f"Backup Completed Successfully at {TimeStamp}"+"\n")

def main():
    schedule.every(10).minutes.do(LogCreator)

    while True:
        schedule.run_pending()
        time.sleep(580)

if __name__ == "__main__":
    main()