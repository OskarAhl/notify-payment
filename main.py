# Input: 
# mandatory - invoice number, type (water (w) or electricity(e), pdf) 
# Output: Email with corresponding attachment sent
# TODO: make classes

import user_input, email_handler

if __name__ == '__main__':
    user_inputs = {}
    user_input.get_user_inputs(user_inputs)

    email_message = email_handler.make_email_message(user_inputs)

    email_handler.verify_message(email_message)

    email_handler.send_email(email_message)
