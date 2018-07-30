import os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import email_setup

msg = None

SUBJECT = 'DAMEN - A 16 13A'
ELECTRICITY = 'ELECTRICITY'
RENT = 'RENT'
WATER = 'WATER'

def make_email_message(user_input):
    print('bill_type', user_input)
    body_message = get_body_message(user_input)
    msg = MIMEMultipart()
    msg['From'] = email_setup.getFromAddress() 
    msg['To'] = email_setup.getSendToAddress(user_input["type_bill"])
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = get_subject(user_input["type_bill"])
    msg.attach(MIMEText(body_message))
    print(msg)

def get_body_message(user_input):
    return 'test'


def get_subject(type_bill):
    if type_bill == 'e':
        return ELECTRICITY + ' ' + SUBJECT
    if type_bill == 'r':
        return RENT + ' ' + SUBJECT
    if type_bill == 'w':
        return WATER + ' ' + SUBJECT

def verify_message():
    return True

def send_email():
    print('sending email...')
