# Input: 
# mandatory - invoice number, type (water (w) or electricity(e), pdf) 
# optional - email address

# Procedure:
# 1. find pdf
# 2. Make email text (with invoice number)
# 3. Add pdf as attachment
# 4. confirmation 
# 5. Send email
import os, sys
import emailsetup

def add_input(start_input):
    user_inputs = {}
    user_inputs['invoice_number'] = add_required_input('Invoice number: ')
    user_inputs['type_bill'] = add_type_bill('Type - water (w) or electricity (e): ')
    user_inputs['transfer_receipt_filename'] = add_required_input('Transfer receipt filename: ')
    print(user_inputs)

def add_required_input(input_help_text):
    user_input = ''
    while(not user_input):
        user_input = input(input_help_text)
    return user_input

def add_type_bill(input_help_text):
    type_bill = ''
    input_is_e_or_w = True
    while input_is_e_or_w:
        type_bill = input(input_help_text).lower()
        if type_bill == 'e' or type_bill == 'w': input_is_e_or_w = False
    return type_bill

print('starting...')
start_input = sys.argv
if(len(start_input) < 3):
    add_input(start_input)
