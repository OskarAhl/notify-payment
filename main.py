# Input: 
# mandatory - invoice number, type (water (w) or electricity(e), pdf) 

# Procedure:
# 1. find pdf
# 2. Make email text (with invoice number)
# 3. Add pdf as attachment
# 4. confirmation 
# 5. Send email
import user_input, email_handler

user_inputs = {}
user_input.get_user_inputs(user_inputs)

email_message = email_handler.make_email_message(user_inputs)

email_handler.verify_message(email_message)

email_handler.send_email(email_message)
