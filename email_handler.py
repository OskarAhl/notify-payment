import os, sys, smtplib, traceback
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import email_setup


DOWNLOAD_FOLDER_PATH = '/Users/oskarahlroth/Downloads'
SUBJECT = 'DAMEN - A 16 13A'
ELECTRICITY = 'ELECTRICITY'
RENT = 'RENT'
WATER = 'WATER'
BODY_MESSAGE_TEMPLATE = '''Hi,

Please find attached $BILL_TYPE bank transfer receipt for A-16-13A
$INVOICE_NR

Sincerely,        

Oskar Ahlroth'''

bill_type = None
def make_email_message(user_input):
    global bill_type
    bill_type = user_input['type_bill'];
    body_message = get_body_message(user_input)
    email_message = MIMEMultipart()
    email_message['From'] = email_setup.getFromAddress() 
    email_message['To'] = email_setup.getSendToAddress(bill_type)
    email_message['Date'] = formatdate(localtime=True)
    email_message['Subject'] = get_subject()
    email_message.attach(MIMEText(body_message))

    transfer_receipt_os_path = get_path(user_input['transfer_receipt_filename'], DOWNLOAD_FOLDER_PATH)

    if not transfer_receipt_os_path:
        print(user_input['transfer_receipt_filename'] + ' does not seem to exist in: ' + DOWNLOAD_FOLDER_PATH)
        sys.exit()

    part = MIMEBase('application', "octet-stream")
    try:
        part.set_payload(open(transfer_receipt_os_path, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=' + user_input['transfer_receipt_filename'])
        email_message.attach(part)
    except Exception as e:
        print('error while sending the email: ' + str(e))
        print(traceback.format_exc())

    return email_message

def get_path(name, path):
    # TODO: add regex to check if name ends with .pdf else add .pdf
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def get_body_message(user_input):
    bill_type_full_name = get_full_bill_type_name().capitalize()
    message = BODY_MESSAGE_TEMPLATE.replace('$BILL_TYPE', bill_type_full_name)
    if bill_type != 'r':
        message = message.replace('$INVOICE_NR', 'Invoice nr: ' + user_input['invoice_number'])
    else:
        message = message.replace('$INVOICE_NR', '')
    return message

def get_subject():
    subject = get_full_bill_type_name() + ' ' + SUBJECT
    return subject

def get_full_bill_type_name():
    if bill_type == 'e':
        return ELECTRICITY
    if bill_type == 'r':
        return RENT
    if bill_type == 'w':
        return WATER

def verify_message(email_message):
    user_verified = False
    is_ok = None

    while not user_verified:
        print(email_message['Subject'] + '  --- to: ' + email_message['To'])
        is_ok = input('Looks ok? y/n: ').lower()
        if is_ok == 'y' or is_ok == 'n': user_verified = True 
    if is_ok == 'n':
        print('Ok, terminating program... :(')
        sys.exit()
        return False
    return True

def send_email(email):
    print('preparing to sending email...')
    send_from = email_setup.getFromAddress()
    send_to = email_setup.getSendToAddress(bill_type),
    try: 
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.login(email_setup.getFromAddress(), email_setup.getEmailCode())
        conn.sendmail(send_from, send_to, email.as_string())
        conn.close()
    except Exception as e:
        print('error while sending the email: ' + str(e))
        print(traceback.format_exc())
        sys.exit()
    finally:
        print('Done!')