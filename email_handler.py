import os, sys, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import email_setup

SUBJECT = 'DAMEN - A 16 13A'
ELECTRICITY = 'ELECTRICITY'
RENT = 'RENT'
WATER = 'WATER'

BODY_MESSAGE_TEMPLATE = '''Hi,

Please find attached $BILL_TYPE bill for A-16-13A 

Tax Invoice no: $INVOICE_NR

Sincerely,        

Oskar Ahlroth'''

def make_email_message(user_input):
    print('bill_type', user_input)
    body_message = get_body_message(user_input)
    email_msg = MIMEMultipart()
    email_msg['From'] = email_setup.getFromAddress() 
    email_msg['To'] = email_setup.getSendToAddress(user_input['type_bill'])
    email_msg['Date'] = formatdate(localtime=True)
    email_msg['Subject'] = get_subject(user_input['type_bill'])
    email_msg.attach(MIMEText(body_message))
    return email_msg

def get_body_message(user_input):
    bill_type = get_full_bill_type_name(user_input['type_bill']).capitalize()
    message = BODY_MESSAGE_TEMPLATE.replace('$BILL_TYPE', bill_type).replace('$INVOICE_NR', user_input['invoice_number'])
    return message

def get_subject(type_bill):
    subject = get_full_bill_type_name(type_bill) + ' ' + SUBJECT
    return subject

def get_full_bill_type_name(type_bill):
    if type_bill == 'e':
        return ELECTRICITY
    if type_bill == 'r':
        return RENT
    if type_bill == 'w':
        return WATER

def verify_message(email_msg):
    user_verified = False
    is_ok = None
    while not user_verified:
        print(email_msg)
        is_ok = input('Looks ok? y/n: ').lower()
        if is_ok == 'y' or is_ok == 'n': user_verified = True 
    if is_ok == 'n':
        print('Ok, terminating program... :(')
        sys.exit()
        return False
    return True

def send_email():
    print('sending email...')
