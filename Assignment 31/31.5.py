import os
import time
import sys
import schedule

def DirectoryScanner(DirectoryName):
    TimeStamp = time.ctime()
    FilesCount = 0
    absolute_path_Dir = os.path.abspath(DirectoryName)
    print()
    print("_"*40)
    print("Scanning:", absolute_path_Dir)
    print("Exists:", os.path.exists(absolute_path_Dir))
    print("Is Directory:", os.path.isdir(absolute_path_Dir))
    print("The Directory Scanned report is logged into DirectoryScanReport.txt ")

    for FolderName, SubfolderName , FileName in os.walk(absolute_path_Dir):

        for fName in FileName:
            FilesCount = FilesCount + 1

    LogFileName = "DirectoryCountLog.txt"
    fobj4 = open(LogFileName,"a")
    fobj4.write("_"*40+"\n")
    fobj4.write(f"Directory Scanned : {absolute_path_Dir}"+"\n")
    fobj4.write(f"Number of Files Scanned :  {FilesCount}"+"\n")
    fobj4.write(f"Scan Time  :  {TimeStamp}"+"\n")
    fobj4.close()



def main():
    dir_name = sys.argv[1]
    schedule.every(5).minutes.do(DirectoryScanner,dir_name)

    while True:
        schedule.run_pending()
        time.sleep(280)

if __name__ == "__main__":
    main()

