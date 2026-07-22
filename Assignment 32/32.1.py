import schedule
import os
import time

def CreateFile():
    TimeStamp = time.ctime()
    Date = time.strftime("%D / %M /%Y")
    Time = time.strftime("%H : %M : %S")
    FolderName = "32.1_txt_Files"


    ret = os.path.exists(FolderName)
    if ret == False:
        os.makedirs(FolderName)
    FolderPath = os.path.abspath(FolderName)
    File_Name = "File_"+TimeStamp+".txt"
    File_Name = File_Name.replace(" ","_")
    File_Name = File_Name.replace(":","_")

    FilePath = os.path.join(FolderPath,File_Name)

    fobj = open(FilePath,"w")
    fobj.write(f"File Name : {File_Name} \n")
    fobj.write("_"*40+"\n")
    fobj.write("_"*40+"\n")
    fobj.write(f"Creation Date : {Date} \n")
    fobj.write(f"Creation Time : {Time} \n")
    fobj.write("_"*40+"\n")

    fobj.close()


def main():
    schedule.every(1).minute.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(50)

if __name__ == "__main__":
    main()
