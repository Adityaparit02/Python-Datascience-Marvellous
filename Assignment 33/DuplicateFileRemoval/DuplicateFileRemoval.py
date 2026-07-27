###############################################################################################
#
#   Import Required Modules
#
#   Description :
#   Imports all the standard libraries and user-defined modules required
#   for command-line processing, scheduling, directory handling,
#   duplicate detection, logging and email functionality.
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
#   Project Name : Duplicate File Removal Automation
#   File Name    : DuplicateFileRemoval.py
#   Description  : Main controller of the automation script. It validates the
#                  command line arguments, schedules the automation process,
#                  and coordinates duplicate file removal and email reporting.
#
#   Author       : Aditya Namdeo Parit
#   Date         : 25/07/2026
#
###############################################################################################








###############################################################################################
#
#   Function Name : DisplayHelp
#
#   Description :
#   Displays complete help information about the automation script,
#   including syntax, required arguments and an example of execution.
#
#   Input  : None
#   Output : Displays help information on the console
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
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




###############################################################################################
#
#   Function Name : DisplayUsage
#
#   Description :
#   Displays the correct command-line syntax when the user provides
#   invalid or insufficient arguments.
#
#   Input  : None
#   Output : Displays usage information on the console
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def DisplayUsage():

    print()

    print("Usage :")

    print("python DuplicateFileRemoval.py")

    print("<AbsoluteDirectoryPath>")

    print("<IntervalInMinutes>")

    print("<ReceiverEmail>")



###############################################################################################
#
#   Function Name : ValidateArguments
#
#   Description :
#   Validates all command-line arguments entered by the user.
#   It verifies:
#       - Number of command-line arguments
#       - Directory existence
#       - Valid directory path
#       - Numeric interval
#       - Positive interval value
#       - Valid email address
#
#   Input  : Command-line arguments
#   Output : Returns True if all validations succeed,
#            otherwise returns False.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

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



###############################################################################################
#
#   Function Name : Automation
#
#   Description :
#   Coordinates the complete duplicate file removal process.
#   It performs duplicate scanning, creates the log file,
#   sends the email report and displays the email status.
#
#   Input  : Directory path and receiver email obtained from
#            command-line arguments.
#
#   Output : Deletes duplicate files, creates a log file,
#            sends an email report and prints email status.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def Automation():
# Extract directory and receiver email from command-line arguments
    Directory = sys.argv[1]
    Receiver = sys.argv[3]


# Sender Gmail credentials (App Password required)
    Sender = "adityaparit44@gmail.com"
    Password = "xxxxxxxxxxxxxxxx"


# Perform duplicate file removal operation
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
#   Function Name : main
#
#   Description :
#   Entry point of the application.
#   Validates command-line arguments, schedules the automation
#   at the specified interval and starts the first execution.
#
#   Input  : Directory path, time interval and receiver email
#            from the command line.
#
#   Output : Starts the automation scheduler.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def main():

    if ValidateArguments()==False:

        return

    Interval = int(sys.argv[2])

# Schedule the automation to execute periodically
    schedule.every(Interval).minutes.do(Automation)


# Execute once immediately before scheduler starts
    Automation()


# Keep checking for pending scheduled tasks
    while True:

        schedule.run_pending()

        time.sleep(Interval * 0.7)



###############################################################################################
#
#   Program Execution Starts Here
#
###############################################################################################
if __name__=="__main__":

    main()



