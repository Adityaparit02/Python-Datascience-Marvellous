import glob
import os
import shutil
import sys
import schedule
import time

def FileCopyMaker(srcDirectoryName ,dstDirectoryName):

    srcDirectoryPath = os.path.abspath(srcDirectoryName)
    dstDirectoryPath = os.path.abspath(dstDirectoryName)

    for FolderName , SubFolderName , FileName in os.walk(srcDirectoryName):
        for fname in FileName:
            os.makedirs(dstDirectoryPath, exist_ok=True)
            for src_file in glob.glob(os.path.join(srcDirectoryPath, "*.txt")):
                shutil.copy(src_file, dstDirectoryPath)

def main():
    sourcedirPath = sys.argv[1]
    dstdirPath = sys.argv[2]
    schedule.every(10).minutes.do(FileCopyMaker,sourcedirPath,dstdirPath)

    while True:
        schedule.run_pending()
        time.sleep(580)

if __name__ == "__main__":
    main()