# Input: 
# mandatory - invoice number, type (water (w) or electricity(e), pdf) 
# optional - email address

# Procedure:
# 1. find pdf
# 2. Make email text (with invoice number)
# 3. Add pdf as attachment
# 4. confirmation 
# 5. Send email

import os, smtplib
import emailsetup
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

#TODO: split input, email to separate modules

def get_user_inputs(user_inputs):
    user_inputs['invoice_number'] = get_required_input('Invoice number: ')
    user_inputs['type_bill'] = get_type_bill('Type - water (w) or electricity (e): ')
    user_inputs['transfer_receipt_filename'] = get_required_input('Transfer receipt filename: ')

def get_required_input(input_help_text):
    user_input = ''
    while(not user_input):
        user_input = input(input_help_text)
    return user_input

def get_type_bill(input_help_text):
    type_bill = ''
    input_is_e_or_w = True
    while input_is_e_or_w:
        type_bill = input(input_help_text).lower()
        if type_bill == 'e' or type_bill == 'w': input_is_e_or_w = False
    return type_bill

user_inputs = {}
get_user_inputs(user_inputs)
print(user_inputs)

email_message = make_email_message('water')

verify_message(email_message)

send_email(email_message)
