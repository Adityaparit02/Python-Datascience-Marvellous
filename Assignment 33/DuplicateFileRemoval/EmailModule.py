###############################################################################################
#
#   Project Name : Duplicate File Removal Automation
#   File Name    : EmailModule.py
#
#   Description  :
#   This module is responsible for sending the email report.
#   It creates the email message, attaches the generated log file,
#   establishes a secure SMTP connection with Gmail and sends
#   the email to the specified receiver.
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
#   Imports the libraries required for SMTP communication,
#   email creation, file attachment handling and file path operations.
#
###############################################################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os




###############################################################################################
#
#   Function Name : SendEmail
#
#   Description :
#   Sends an email with the generated log file as an attachment
#   using Gmail's SMTP server. Establishes a secure connection,
#   authenticates the sender and delivers the email to the receiver.
#
#   Input  :
#       Sender Email
#       App Password
#       Receiver Email
#       Subject
#       Email Body
#       Attachment Path
#
#   Output :
#       Returns True if the email is sent successfully,
#       otherwise returns False.
#
#   Author : Aditya Namdeo Parit
#   Date   : 25/07/2026
#
###############################################################################################

def SendEmail(SenderEmail,
              Password,
              ReceiverEmail,
              Subject,
              Body,
              AttachmentPath):

    try:

# Create a multipart email message
        Message = MIMEMultipart()

# Set sender, receiver and subject of the email
        Message["From"] = SenderEmail
        Message["To"] = ReceiverEmail
        Message["Subject"] = Subject

# Attach plain text email body
        Message.attach(MIMEText(Body,"plain"))

# Open log file in binary mode for attachment
        with open(AttachmentPath,"rb") as fobj:

# Create MIME object for file attachment
# MIME (Multipurpose Internet Mail Extensions)
# allows files to be attached to an email.
            Part = MIMEBase("application","octet-stream")

            Part.set_payload(fobj.read())           # Read attachment data into MIME object

# Convert binary attachment into text format
# so it can be transmitted safely over email.
        encoders.encode_base64(Part)                # Encode attachment into Base64 format

# Add attachment filename to email header
        Part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(AttachmentPath)}"
        )

# Attach the log file to the email
        Message.attach(Part)

# Gmail SMTP Server (Port 587 uses TLS encryption)
        Server = smtplib.SMTP("smtp.gmail.com",587)         # Connect to Gmail SMTP server

        Server.starttls()                                   # Start encrypted TLS communication

        Server.login(SenderEmail,Password)                  # Authenticate sender using Gmail App Password

# Send email with attachment
        Server.sendmail(SenderEmail,
                        ReceiverEmail,
                        Message.as_string())                # Convert complete email message into string format
                                                            # before transmitting through SMTP.

        Server.quit()               # Close SMTP connection


        return True             # Email sent successfully



# Display error message if email sending fails
    except Exception as e:

        print(e)

        return False            # Email sending failed



    


