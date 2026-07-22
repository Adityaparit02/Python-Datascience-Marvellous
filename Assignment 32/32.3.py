import os
import time
import schedule
import sys

def DisplayFile(FileName):

    FilePath = os.path.abspath(FileName)
    FileExist = os.path.exists(FilePath)
    FileSize = os.path.getsize(FilePath)
    FileReadPermission = os.access(FilePath,os.R_OK)

    if FileExist == True:
        print("The File Exists")
    else:
        print("File does not Exist")

    if FileSize == 0:
        print("Empty File")
    else:
        print(f"File Size : {FileSize}")

    if FileReadPermission == True:
        print("File has Permission to Read")
    else:
        print("File Does Not have Permission to Read")  

    print("\n")
    fobj = open(FileName,"r")
    Data = fobj.read()
    print("File Contents: \n")
    print(Data)
    fobj.close()

def main():
    FileName = sys.argv[1]
    schedule.every(1).minute.do(DisplayFile,FileName)

    while True:
        schedule.run_pending()
        time.sleep(45)

if __name__ == "__main__":
    main()
