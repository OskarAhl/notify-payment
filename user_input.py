def get_user_inputs(user_inputs):
    user_inputs['type_bill'] = get_type_bill('Type - water (w), electricity (e), rent(r): ')
    if user_inputs['type_bill'] != 'r':
        user_inputs['invoice_number'] = get_required_input('Invoice number: ')
    user_inputs['transfer_receipt_filename'] = get_required_input('Transfer receipt filename: ')

def get_required_input(input_help_text):
    user_input = ''
    while(not user_input):
        user_input = input(input_help_text)
    return user_input

def get_type_bill(input_help_text):
    type_bill = ''
    input_is_e_w_r = True
    while input_is_e_w_r:
        type_bill = input(input_help_text).lower()
        if type_bill == 'e' or type_bill == 'w' or type_bill == 'r': input_is_e_w_r = False
    return type_bill
