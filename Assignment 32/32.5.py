import os
import time
import schedule
import sys


def DeleteEmptyFiles(DirectoryName):

    TimeStamp = time.ctime()
    DirectoryPath = os.path.abspath(DirectoryName)
    LogFileName = "Empty_Delete_Log.txt"
    LogFilePath = os.path.abspath(LogFileName)


    for FolderName,SubFolderName,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            FilePath = os.path.abspath(fname)
            FilePath = os.path.join(FolderName,fname)
            FileSize = os.path.getsize(FilePath)
            DeletionTime = time.ctime()

            if FileSize == 0:
                os.remove(FilePath)
                fobj = open(LogFilePath,"a")
                fobj.write("\n")
                fobj.write(f"The Empty File Path is : {FilePath} \n")
                fobj.write(f"Scanned Time  : {TimeStamp} \n")
                fobj.write(f"Deletion Time  : {DeletionTime} \n")
                fobj.write("\n")
                fobj.write("_"*40+"\n")
                fobj.close()

def main():
    DirectoryName = sys.argv[1]
    schedule.every(1).hour.do(DeleteEmptyFiles,DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(3580)

if __name__ == "__main__":
    main()