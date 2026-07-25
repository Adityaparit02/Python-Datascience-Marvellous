import os
import hashlib
import datetime
import re

def CalculateChecksum(FileName):

    hash_md5 = hashlib.md5()

    try:
        with open(FileName, "rb") as fobj:

            while True:

                Buffer = fobj.read(4096)

                if len(Buffer) == 0:
                    break

                hash_md5.update(Buffer)

        return hash_md5.hexdigest()

    except Exception:
        return None


def IsValidEmail(Email):

    Pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if re.match(Pattern, Email):
        return True

    return False


def CreateLogDirectory():

    FolderName = "Marvellous"

    DirectoryPath = os.path.join(os.getcwd(), FolderName)

    if os.path.exists(DirectoryPath) == False:
        os.mkdir(DirectoryPath)

    return DirectoryPath


def GetLogFileName(LogDirectory):

    TimeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    FileName = "DuplicateRemovalLog_" + TimeStamp + ".log"

    return os.path.join(LogDirectory, FileName)


def ScanDirectory(DirectoryName):

    DuplicateData = {}

    TotalFiles = 0

    for FolderName, SubFolderName, FileNames in os.walk(DirectoryName):

        for File in FileNames:

            FilePath = os.path.join(FolderName, File)

            if os.path.isfile(FilePath):

                TotalFiles += 1

                Checksum = CalculateChecksum(FilePath)

                if Checksum is None:
                    continue

                if Checksum in DuplicateData:
                    DuplicateData[Checksum].append(FilePath)
                else:
                    DuplicateData[Checksum] = [FilePath]

    return DuplicateData, TotalFiles

def DeleteDuplicates(DuplicateData):

    DeletedFiles = []
    DuplicateCount = 0

    for Checksum in DuplicateData:

        FileList = DuplicateData[Checksum]

        if len(FileList) > 1:

            for FilePath in FileList[1:]:

                try:
                    os.remove(FilePath)

                    DeletedFiles.append((FilePath, Checksum))

                    DuplicateCount += 1

                except Exception as e:

                    DeletedFiles.append(
                        ("ERROR : " + FilePath + " -> " + str(e), Checksum)
                    )

    return DuplicateCount, DeletedFiles

def CreateLog(LogFileName,
              StartTime,
              EndTime,
              DirectoryName,
              TotalFiles,
              DuplicateCount,
              DeletedFiles,
              EmailStatus):

    try:

        with open(LogFileName, "w") as fobj:

            fobj.write("-" * 60 + "\n")
            fobj.write("Duplicate File Removal Automation\n")
            fobj.write("-" * 60 + "\n\n")

            fobj.write(f"Starting Time : {StartTime}\n")
            fobj.write(f"Completion Time : {EndTime}\n\n")

            fobj.write(f"Directory Scanned : {DirectoryName}\n")
            fobj.write(f"Total Files : {TotalFiles}\n")
            fobj.write(f"Duplicate Files Deleted : {DuplicateCount}\n\n")

            fobj.write("Deleted Files\n")
            fobj.write("-" * 60 + "\n")

            if len(DeletedFiles) == 0:
                fobj.write("No Duplicate Files Found\n")

            else:

                for FilePath,Checksum in DeletedFiles:

                    fobj.write(f"{FilePath}\n")
                    fobj.write(f"Checksum : {Checksum}\n\n")

            fobj.write("\n")
            fobj.write(f"Email Status : {EmailStatus}\n")

            fobj.write("-" * 60 + "\n")

    except Exception:

        return False

    return True


def GenerateEmailBody(StartTime,
                      EndTime,
                      DirectoryName,
                      TotalFiles,
                      DuplicateCount):

    Body = f"""
Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics

Starting Time : {StartTime}

Completion Time : {EndTime}

Directory Scanned : {DirectoryName}

Total Files Scanned : {TotalFiles}

Duplicate Files Deleted : {DuplicateCount}

Please find the attached log file.

Regards,

Marvellous Automation System
"""

    return Body


def PerformOperation(DirectoryName):

    StartTime = datetime.datetime.now()

    DuplicateData, TotalFiles = ScanDirectory(DirectoryName)

    DuplicateCount, DeletedFiles = DeleteDuplicates(DuplicateData)

    EndTime = datetime.datetime.now()

    LogDirectory = CreateLogDirectory()

    LogFile = GetLogFileName(LogDirectory)

    Body = GenerateEmailBody(
                StartTime,
                EndTime,
                DirectoryName,
                TotalFiles,
                DuplicateCount
            )

    return (StartTime,
            EndTime,
            TotalFiles,
            DuplicateCount,
            DeletedFiles,
            LogFile,
            Body)

