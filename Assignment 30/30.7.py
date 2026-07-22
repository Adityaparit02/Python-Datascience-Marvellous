import schedule
import os
import sys
from pathlib import Path
import time

def fileBackup(FileName,DirectoryName):
    absolute_path_File = os.path.abspath(FileName)
    fobj = open(absolute_path_File,"r")
    Data_Original = fobj.read()

    TimeStamp = time.ctime()

    Backup_File_Name = "Backup%s"%(TimeStamp)+".txt"
    Backup_File_Name = Backup_File_Name.replace(" ","_")
    Backup_File_Name = Backup_File_Name.replace(":","_")
    Backup_File_Path = os.path.join(DirectoryName,Backup_File_Name)
    os.makedirs(DirectoryName,exist_ok=True)

    fobj2 = open(Backup_File_Path,"w")
    fobj2.write("_"*40+"\n")
    fobj2.write(time.ctime()+"\n")
    fobj2.write("_"*40 +"\n" )
    fobj2.write("\n")
    fobj2.write(Data_Original)

    LogFileName = "Backup_Log.txt"

    fobj4 = open(LogFileName,"a")
    fobj4.write("_"*40+"\n")
    fobj4.write(f"Backup Completed Successfully at {TimeStamp}"+"\n")

def main():
    file_name = sys.argv[1]
    Dir_Name = sys.argv[2]
    print(f"The File Will be backed up every Hour in Directory : {Dir_Name} ")
    print("Strating From Now...")
    schedule.every(1).hour.do(fileBackup,file_name,Dir_Name)

    while True:
        schedule.run_pending()
        time.sleep(3580)
if __name__=="__main__":
    main()

