from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email_config
import smtplib
import os
from email import encoders


def send_mail(
        *,
        recipients: list[str],
        mail_body: str,
        mail_subject: str,
        attachment: str = None
):
    SERVER = email_config.SMTP_SERVER
    PASSWORD = email_config.TOKEN_API
    USER = email_config.USER

    msg = MIMEMultipart('')
    msg['Subject'] = mail_subject
    msg['From'] = f'<lection 13 user {USER}'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    if attachment:
        file_exists = os.path.exists(attachment)
        if not file_exists:
            print(f"file {attachment} does not exists")
        else:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('application', f'octet-stream; name = {basename}')
            file.set_payload(open(attachment, 'rb').read())
            file.add_header('Content-Description', attachment)
            file.add_header('Content-Description', f'attachment; filename={attachment}; size={filesize}')
            encoders.encode_base64(file)
            msg.attach(file)

    text_to_send = MIMEText(mail_body, 'plain')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SERVER)
    mail.login(USER, PASSWORD)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


def check_email():
    pass

# recipients = ['dduckker@ukr.net']
# mail_body = 'blah'
# mail_subject = 'blah'
# attachment = 'main.py'
# send_mail(
#     recipients=['dduckker@ukr.net'],
#     mail_body='blah blah blah blah blah blah blah ',
#     mail_subject='blah blah ',
#     attachment='main.py'
# )
