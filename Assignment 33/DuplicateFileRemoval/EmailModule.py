import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def SendEmail(SenderEmail,
              Password,
              ReceiverEmail,
              Subject,
              Body,
              AttachmentPath):

    try:

        Message = MIMEMultipart()

        Message["From"] = SenderEmail
        Message["To"] = ReceiverEmail
        Message["Subject"] = Subject

        Message.attach(MIMEText(Body,"plain"))

        with open(AttachmentPath,"rb") as fobj:

            Part = MIMEBase("application","octet-stream")

            Part.set_payload(fobj.read())

        encoders.encode_base64(Part)

        Part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(AttachmentPath)}"
        )

        Message.attach(Part)

        Server = smtplib.SMTP("smtp.gmail.com",587)

        Server.starttls()

        Server.login(SenderEmail,Password)

        Server.sendmail(SenderEmail,
                        ReceiverEmail,
                        Message.as_string())

        Server.quit()

        return True

    except Exception as e:

        print(e)

        return False


    


