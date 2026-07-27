import os 
import time
import psutil
import sys
import smtplib
from email.message import EmailMessage
import mimetypes

def BodyMaker(TimeTaken, Pcount, CPU_Usage, RAM_Usage, RAM_Available):

    Body = f"""
============================================================
                ADITYA NAMDEO PARIT
      PLATFORM SURVEILLANCE AUTOMATION REPORT
============================================================

Jay Ganesh,

The system monitoring process has completed successfully.

-------------------- SYSTEM SUMMARY --------------------

CPU Usage               : {CPU_Usage:.2f} %
RAM Usage               : {RAM_Usage:.2f} %
Available RAM           : {RAM_Available/(1024**3):.2f} GB
Running Processes       : {Pcount}
Execution Time          : {TimeTaken:.2f} Seconds

--------------------------------------------------------

Status                  : SUCCESS
Log File                : Attached

============================================================
This is an automatically generated email.
Please do not reply.

Regards,
Platform Surveillance Automation
Aditya Namdeo Parit
============================================================
"""

    return Body



def send_email(sender,app_password,reciever,subject,Body,AttachmentPath):
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    msg.set_content(Body)
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




def DirectoryMaker(DirectoryName):
    ret = os.path.exists(DirectoryName)

    if ret == False:
        os.makedirs(DirectoryName)

    return DirectoryName


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

def main():
    sys.argv[1]

    if len(sys.argv) != 3:
        print("Usage : python Automation.py DirectoryName ReceiverEmail")
        return

    Sender = "adityaparit44@gmail.com"
    app_password = "xxxx xxxx xxxx xxxx"
    receiver =     sys.argv[2]
    subject = "Process Report"
    ProcessScanner(Sender,app_password,receiver,subject)

if __name__ == "__main__":
    main()