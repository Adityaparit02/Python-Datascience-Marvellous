############################################################
#
# Program Name  : Platform Surveillance Automation
#
# Description   : This application periodically monitors
#                 the system by collecting CPU, RAM,
#                 Network and Running Process information.
#                 A detailed log file is generated and
#                 automatically emailed to the specified
#                 recipient along with the log attachment.
#
# Technologies  : Python, psutil, smtplib, schedule
#
# Author        : Aditya Namdeo Parit
# Date          : 28/07/2026
#
############################################################


############################################################
#
#                   IMPORT REQUIRED MODULES
#
############################################################

import os 
import time
import psutil
import sys
import smtplib
from email.message import EmailMessage
import mimetypes
import schedule


############################################################
#
# Function Name : BodyMaker
# Description   : Creates the HTML email body containing
#                 the system monitoring report.
# Input         : TimeTaken, Pcount, CPU_Usage,
#                 RAM_Usage, RAM_Available
# Output        : Returns HTML formatted email body.
# Author        : Aditya Namdeo Parit
# Date          : 28/07/2026
#
############################################################

def BodyMaker(TimeTaken, Pcount, CPU_Usage, RAM_Usage, RAM_Available):

    Body = f"""
<!DOCTYPE html>
<html>

<head>
<style>

body {{
    font-family: Arial, Helvetica, sans-serif;
    background-color: #f4f6f9;
    color: #333333;
}}

.container {{
    width: 700px;
    margin: auto;
    background: white;
    border-radius: 10px;
    border: 1px solid #dcdcdc;
    overflow: hidden;
}}

.header {{
    background-color: #0d6efd;
    color: white;
    text-align: center;
    padding: 20px;
}}

.header h1 {{
    margin: 0;
}}

.content {{
    padding: 25px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
}}

th {{
    background-color: #0d6efd;
    color: white;
    padding: 10px;
}}

td {{
    padding: 10px;
    border-bottom: 1px solid #dddddd;
}}

.status {{
    color: green;
    font-weight: bold;
}}

.footer {{
    text-align: center;
    padding: 15px;
    background: #f0f0f0;
    font-size: 13px;
}}

</style>
</head>

<body>

<div class="container">

<div class="header">
<h1>Platform Surveillance Automation</h1>
<h3>Aditya Namdeo Parit</h3>
</div>

<div class="content">

<p><b>Jay Ganesh,</b></p>

<p>
The Platform Surveillance Automation has completed successfully.
Please find the system summary below.
</p>

<table>

<tr>
<th>Parameter</th>
<th>Value</th>
</tr>

<tr>
<td>CPU Usage</td>
<td>{CPU_Usage:.2f}%</td>
</tr>

<tr>
<td>RAM Usage</td>
<td>{RAM_Usage:.2f}%</td>
</tr>

<tr>
<td>Available RAM</td>
<td>{RAM_Available/(1024**3):.2f} GB</td>
</tr>

<tr>
<td>Running Processes</td>
<td>{Pcount}</td>
</tr>

<tr>
<td>Execution Time</td>
<td>{TimeTaken:.2f} Seconds</td>
</tr>

<tr>
<td>Status</td>
<td class="status">SUCCESS</td>
</tr>

<tr>
<td>Log File</td>
<td>Attached</td>
</tr>

</table>

</div>

<div class="footer">

<b>This is an automatically generated email.</b><br>
Please do not reply.

<br><br>

Regards,<br>
<b>Platform Surveillance Automation</b><br>
Aditya Namdeo Parit

</div>

</div>

</body>
</html>
"""

    return Body


############################################################
#
# Function Name : send_email
# Description   : Sends an HTML email with the generated
#                 system report and attaches the log file.
# Input         : Sender Email, App Password,
#                 Receiver Email, Subject,
#                 HTML Body, Attachment Path
# Output        : Sends email successfully or displays
#                 an authentication error.
# Author        : Aditya Namdeo Parit
# Date          : 28/07/2026
#
############################################################
def send_email(sender,app_password,reciever,subject,Body,AttachmentPath):
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    msg.set_content("Your email client does not support HTML emails.")
    msg.add_alternative(Body, subtype="html")


    with open(AttachmentPath, "rb") as f:
        file_data = f.read()

    mime_type, _ = mimetypes.guess_type(AttachmentPath)

    if mime_type:
        maintype, subtype = mime_type.split("/")
    else:
        maintype, subtype = "application", "octet-stream"

    msg.add_attachment(file_data,
                       maintype=maintype,
                       subtype=subtype,
                       filename=os.path.basename(AttachmentPath))

    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, app_password)
            smtp.send_message(msg)

        print("Email sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your Gmail App Password.")



############################################################
#
# Function Name : DirectoryMaker
# Description   : Checks whether the specified directory
#                 exists. Creates it if it does not exist.
# Input         : Directory Name
# Output        : Returns the directory path.
# Author        : Aditya Namdeo Parit
# Date          : 28/07/2026
#
############################################################
def DirectoryMaker(DirectoryName):
    ret = os.path.exists(DirectoryName)

    if ret == False:
        os.makedirs(DirectoryName)

    return DirectoryName


############################################################
#
# Function Name : ProcessScanner
# Description   : Collects system information including
#                 CPU, RAM, Network and Running Processes.
#                 Generates a log file and emails the
#                 report with the log attached.
# Input         : Sender Email, App Password,
#                 Receiver Email, Subject
# Output        : Log File and Email Report
# Author        : Aditya Namdeo Parit
# Date          : 28/07/2026
#
############################################################
def ProcessScanner(Sender,app_password,receiver,subject):
    CPU_Usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    RAM_Usage = memory.percent
    RAM_Available = memory.available
    netobj = psutil.net_io_counters()
      
    Pcount = 0
    Border = "_"*50
    DirectoryName = DirectoryMaker(sys.argv[1])

    timeStamp = time.ctime()
    LogFileName = "LogFile_"+timeStamp+".log"
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    LogFilePath = os.path.join(DirectoryName,LogFileName)
    fobj = open(LogFilePath,"w")
    Border = "=" * 70

    fobj.write(Border + "\n")
    fobj.write("          ADITYA NAMDEO PARIT\n")
    fobj.write("     PLATFORM SURVEILLANCE REPORT\n")
    fobj.write(Border + "\n")
    fobj.write(f"Generated On : {timeStamp}\n")
    fobj.write(Border + "\n\n")
    starttime = time.perf_counter()

    fobj.write("[ SYSTEM INFORMATION ]\n")
    fobj.write("-" * 70 + "\n")
    fobj.write(f"CPU Cores          : {psutil.cpu_count()}\n")
    fobj.write(f"CPU Usage          : {CPU_Usage:.2f} %\n")
    fobj.write(f"RAM Usage          : {memory.percent:.2f} %\n")
    fobj.write(f"Total RAM          : {memory.total/(1024**3):.2f} GB\n")
    fobj.write(f"Available RAM      : {memory.available/(1024**3):.2f} GB\n")
    fobj.write("-" * 70 + "\n\n")


    fobj.write("[ NETWORK INFORMATION ]\n")
    fobj.write("-" * 70 + "\n")
    fobj.write(f"Data Sent          : {netobj.bytes_sent/(1024*1024):.2f} MB\n")
    fobj.write(f"Data Received      : {netobj.bytes_recv/(1024*1024):.2f} MB\n")
    fobj.write("-" * 70 + "\n\n")


    fobj.write("[ RUNNING PROCESS LIST ]\n")
    fobj.write("-" * 90 + "\n")

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username"])
            Pcount = Pcount +1
            fobj.write(f"""
    PID        : {info.get('pid')}
    Process    : {info.get('name')}
    User       : {info.get('username')}
    {'-'*90}
    """)
        except:
            pass


    endtime = time.perf_counter()

    TimeTaken = endtime - starttime

    fobj.write("\n")
    fobj.write(Border + "\n")
    fobj.write("REPORT SUMMARY\n")
    fobj.write(Border + "\n")
    fobj.write(f"Total Running Processes : {Pcount}\n")
    fobj.write(f"CPU Usage               : {CPU_Usage:.2f} %\n")
    fobj.write(f"RAM Usage               : {RAM_Usage:.2f} %\n")
    fobj.write(f"Execution Time          : {TimeTaken:.2f} Seconds\n")
    fobj.write(f"Report Generated On     : {timeStamp}\n")
    fobj.write(Border + "\n")
    fobj.write("End of Report\n")
    fobj.write(Border + "\n")
    fobj.close()



  

    Body = BodyMaker(TimeTaken,Pcount,CPU_Usage,RAM_Usage,RAM_Available)
    send_email(Sender,app_password,receiver,subject,Body,LogFilePath)


############################################################
#
# Function Name : main
# Description   : Entry point of the application.
#                 Validates command line arguments,
#                 schedules the monitoring task and
#                 starts the scheduler loop.
# Input         : Command Line Arguments
# Output        : Starts Platform Surveillance Automation
# Author        : Aditya Namdeo Parit
# Date          : 28/07/2026
#
############################################################
def main():
    sys.argv[1]

    if len(sys.argv) != 3:
        print("Usage : python Automation.py DirectoryName ReceiverEmail")
        return

    Sender = "adityaparit44@gmail.com"
    app_password = "gtaj bzsw zymf qgfw"
    receiver =     sys.argv[2]
    subject = "Process Report"
    schedule.every(1).minute.do(ProcessScanner,Sender,app_password,receiver,subject)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()