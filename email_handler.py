import os, smtplib
import user_input, email_handler
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import emailsetup

msg = None

def make_email_message(bill_type):
    print('bill_type', bill_type)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

def verify_message():
    return True

def send_email():
    print('sending email...')
