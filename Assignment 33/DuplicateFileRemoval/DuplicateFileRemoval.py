###############################################################################################
#    
#    Importing Required Libraries
#
#
###############################################################################################


import sys

import time

import schedule

import os

from DuplicateModule import *

from EmailModule import *

###############################################################################################
#    
#       Function Name : Duplicate Files Scanner
#       Input :         Name of Directory
#       Description :   Deletes all empty files periodically
#       Date :          25/07/2026
#       Author :        Aditya Namdeo Parit
#
#
###############################################################################################



def DisplayHelp():

    print("--------------------------------------------")
    print("Duplicate File Removal Automation")
    print("--------------------------------------------")

    print()

    print("Usage")

    print("python DuplicateFileRemoval.py")
    print("<Directory>")
    print("<Interval>")
    print("<ReceiverEmail>")

    print()

    print("Example")

    print("python DuplicateFileRemoval.py")
    print("E:/Demo")
    print("50")
    print("abc@gmail.com")



def DisplayUsage():

    print()

    print("Usage :")

    print("python DuplicateFileRemoval.py")

    print("<AbsoluteDirectoryPath>")

    print("<IntervalInMinutes>")

    print("<ReceiverEmail>")


def ValidateArguments():

    if len(sys.argv)==2:

        if sys.argv[1] in ("-h","--help"):

            DisplayHelp()

            return False

        elif sys.argv[1] in ("-u","--usage"):

            DisplayUsage()

            return False

    if len(sys.argv)!=4:

        DisplayUsage()

        return False

    Directory = sys.argv[1]

    Interval = sys.argv[2]

    Email = sys.argv[3]

    if os.path.exists(Directory)==False:

        print("Directory not found")

        return False

    if os.path.isdir(Directory)==False:

        print("Invalid Directory")

        return False

    if Interval.isdigit()==False:

        print("Invalid Interval")

        return False

    if int(Interval)<=0:

        print("Interval must be greater than zero")

        return False

    if IsValidEmail(Email)==False:

        print("Invalid Email")

        return False

    return True

def Automation():

    Directory = sys.argv[1]
    Receiver = sys.argv[3]

    Sender = "adityaparit44@gmail.com"
    Password = "kxni wtxz zicm pvsu"

    (
        StartTime,
        EndTime,
        TotalFiles,
        DuplicateCount,
        DeletedFiles,
        LogFile,
        Body

    ) = PerformOperation(Directory)

    # Create the log first
    CreateLog(
        LogFile,
        StartTime,
        EndTime,
        Directory,
        TotalFiles,
        DuplicateCount,
        DeletedFiles,
        "Pending"
    )

    # Now send the email
    Status = SendEmail(
        Sender,
        Password,
        Receiver,
        "Duplicate File Removal Report",
        Body,
        LogFile
    )

    print("Email Status :", Status)


###############################################################################################
#    
#       Function Name : Main
#       Input :         Directory Name , time interval and email as Command Line Input
#       Description :   Automator Starter
#       Date :          25/07/2026
#       Author :        Aditya Namdeo Parit
#
#
###############################################################################################

def main():

    if ValidateArguments()==False:

        return

    Interval = int(sys.argv[2])

    schedule.every(Interval).minutes.do(Automation)

    Automation()

    while True:

        schedule.run_pending()

        time.sleep(1)


###############################################################################################
#    
#    start of automation script
#
#
###############################################################################################

if __name__=="__main__":

    main()



