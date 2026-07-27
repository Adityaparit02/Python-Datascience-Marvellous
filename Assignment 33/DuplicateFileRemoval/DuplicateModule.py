###############################################################################################
#
#   Project Name : Duplicate File Removal Automation
#   File Name    : DuplicateModule.py
#
#   Description  :
#   This module contains all the core functions required for duplicate
#   file detection, checksum generation, directory scanning, duplicate
#   deletion, log generation and email body creation.
#
#   Author       : Aditya Namdeo Parit
#   Date         : 25/07/2026
#
###############################################################################################




###############################################################################################
#
#   Import Required Modules
#
#   Description :
#   Imports all standard libraries required for file handling,
#   checksum generation, date and time operations,
#   regular expressions and directory manipulation.
#
###############################################################################################
import os
import hashlib
import datetime
import re




###############################################################################################
#
#   Function Name : CalculateChecksum
#
#   Description :
#   Calculates the MD5 checksum of the specified file.
#   The checksum is later used to identify duplicate files.
#
#   Input  : File Name
#   Output : MD5 checksum string or None if an error occurs.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def CalculateChecksum(FileName):

# Create MD5 hash object
    hash_md5 = hashlib.md5()

    try:
        with open(FileName, "rb") as fobj:          # Open file in binary mode

            while True:

                Buffer = fobj.read(4096)            # Read file in chunks of 4096 bytes

                if len(Buffer) == 0:
                    break

                hash_md5.update(Buffer)             # Update checksum using current chunk

        return hash_md5.hexdigest()                 # Return hexadecimal representation of checksum

    except Exception:
        return None




###############################################################################################
#
#   Function Name : IsValidEmail
#
#   Description :
#   Validates the email address using Regular Expressions.
#
#   Input  : Email Address
#   Output : Returns True if email is valid, otherwise False.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def IsValidEmail(Email):

# Regular expression for email validation
    Pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

# Match email against the regular expression
    if re.match(Pattern, Email):
        return True

    return False




###############################################################################################
#
#   Function Name : CreateLogDirectory
#
#   Description :
#   Creates a folder named "Marvellous" in the current
#   working directory if it does not already exist.
#
#   Input  : None
#   Output : Returns complete path of the log directory.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def CreateLogDirectory():

# Name of folder that stores log files
    FolderName = "Marvellous"

# Get absolute path of log directory
    DirectoryPath = os.path.join(os.getcwd(), FolderName)

# Create folder if it does not exist
    if os.path.exists(DirectoryPath) == False:
        os.mkdir(DirectoryPath)

    return DirectoryPath




###############################################################################################
#
#   Function Name : GetLogFileName
#
#   Description :
#   Generates a unique timestamp-based log file name.
#
#   Input  : Log Directory Path
#   Output : Complete path of the log file.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def GetLogFileName(LogDirectory):
# Generate current timestamp
    TimeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

# Create unique log filename
    FileName = "DuplicateRemovalLog_" + TimeStamp + ".log"

# Return complete path
    return os.path.join(LogDirectory, FileName)





###############################################################################################
#
#   Function Name : ScanDirectory
#
#   Description :
#   Recursively scans the specified directory.
#   Calculates checksum for every file and stores
#   duplicate information using a dictionary.
#
#   Input  : Directory Name
#   Output : Dictionary containing checksum as key and
#            list of duplicate files as value.
#            Also returns total number of files scanned.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def ScanDirectory(DirectoryName):

# Dictionary to store checksum and file list
    DuplicateData = {}

# Count total files scanned
    TotalFiles = 0


# Traverse all folders recursively
    for FolderName, SubFolderName, FileNames in os.walk(DirectoryName):

        for File in FileNames:

            FilePath = os.path.join(FolderName, File)   # Create complete file path

            if os.path.isfile(FilePath):                # Process only regular files

                TotalFiles += 1

                Checksum = CalculateChecksum(FilePath)   # Calculate checksum of file


# Ignore files whose checksum cannot be calculated
                if Checksum is None:
                    continue

                if Checksum in DuplicateData:           
                    DuplicateData[Checksum].append(FilePath)            # If checksum already exists, append file
                else:
                    DuplicateData[Checksum] = [FilePath]                # Otherwise create new checksum entry

    return DuplicateData, TotalFiles






###############################################################################################
#
#   Function Name : DeleteDuplicates
#
#   Description :
#   Deletes duplicate files while keeping one original copy.
#   Also maintains a list of deleted files for log generation.
#
#   Input  : Dictionary containing duplicate file information.
#
#   Output : Number of duplicate files deleted and
#            list of deleted files with checksum.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def DeleteDuplicates(DuplicateData):

# Store deleted file information
    DeletedFiles = []

    # Count deleted duplicate files
    DuplicateCount = 0

# Iterate through each checksum group
    for Checksum in DuplicateData:

        FileList = DuplicateData[Checksum]

        if len(FileList) > 1:           # Ignore groups containing only one file

            for FilePath in FileList[1:]:       # Keep first file and delete remaining duplicates

                try:
                    os.remove(FilePath)        # Delete duplicate file

                    DeletedFiles.append((FilePath, Checksum))       # Store deletion details

                    DuplicateCount += 1


# Store deletion error if file cannot be removed
                except Exception as e:

                    DeletedFiles.append(
                        ("ERROR : " + FilePath + " -> " + str(e), Checksum)
                    )

    return DuplicateCount, DeletedFiles






###############################################################################################
#
#   Function Name : CreateLog
#
#   Description :
#   Generates a detailed log file containing
#   operation statistics, deleted file information
#   and email status.
#
#   Input  :
#       Log File Name
#       Start Time
#       End Time
#       Directory Name
#       Total Files
#       Duplicate Count
#       Deleted File List
#       Email Status
#
#   Output :
#       Returns True if log is created successfully,
#       otherwise False.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def CreateLog(LogFileName,
              StartTime,
              EndTime,
              DirectoryName,
              TotalFiles,
              DuplicateCount,
              DeletedFiles,
              EmailStatus):

    try:
# Open log file in write mode
        with open(LogFileName, "w") as fobj:

# Write header information
            fobj.write("-" * 60 + "\n")
            fobj.write("Duplicate File Removal Automation\n")
            fobj.write("-" * 60 + "\n\n")

# Write execution statistics
            fobj.write(f"Starting Time : {StartTime}\n")
            fobj.write(f"Completion Time : {EndTime}\n\n")

# Write deleted file details
            fobj.write(f"Directory Scanned : {DirectoryName}\n")
            fobj.write(f"Total Files : {TotalFiles}\n")
            fobj.write(f"Duplicate Files Deleted : {DuplicateCount}\n\n")

            fobj.write("Deleted Files\n")
            fobj.write("-" * 60 + "\n")

# If no duplicates found
            if len(DeletedFiles) == 0:
                fobj.write("No Duplicate Files Found\n")

            else:

                for FilePath,Checksum in DeletedFiles:

                    fobj.write(f"{FilePath}\n")
                    fobj.write(f"Checksum : {Checksum}\n\n")

# Write email delivery status
            fobj.write("\n")
            fobj.write(f"Email Status : {EmailStatus}\n")

            fobj.write("-" * 60 + "\n")

    except Exception:

        return False

    return True




###############################################################################################
#
#   Function Name : GenerateEmailBody
#
#   Description :
#   Creates the email message containing
#   summary of duplicate file removal operation.
#
#   Input  :
#       Start Time
#       End Time
#       Directory Name
#       Total Files
#       Duplicate Count
#
#   Output :
#       Returns formatted email body.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def GenerateEmailBody(StartTime,
                      EndTime,
                      DirectoryName,
                      TotalFiles,
                      DuplicateCount):

# Prepare formatted email body
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




###############################################################################################
#
#   Function Name : PerformOperation
#
#   Description :
#   Performs the complete duplicate removal operation.
#   It scans the directory, deletes duplicate files,
#   creates log information and prepares the email body.
#
#   Input  : Directory Name
#
#   Output :
#       Returns:
#       Start Time
#       End Time
#       Total Files
#       Duplicate Count
#       Deleted Files
#       Log File Path
#       Email Body
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def PerformOperation(DirectoryName):
# Record operation start time
    StartTime = datetime.datetime.now()

# Scan directory for duplicate files
    DuplicateData, TotalFiles = ScanDirectory(DirectoryName)

# Delete duplicate files
    DuplicateCount, DeletedFiles = DeleteDuplicates(DuplicateData)

# Record operation completion time
    EndTime = datetime.datetime.now()

# Create log directory
    LogDirectory = CreateLogDirectory()

# Generate log file name
    LogFile = GetLogFileName(LogDirectory)

# Generate email body
    Body = GenerateEmailBody(
                StartTime,
                EndTime,
                DirectoryName,
                TotalFiles,
                DuplicateCount
            )

# Return all operation details to caller
    return (StartTime,
            EndTime,
            TotalFiles,
            DuplicateCount,
            DeletedFiles,
            LogFile,
            Body)

