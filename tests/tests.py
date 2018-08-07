import unittest
import sys
sys.path.insert(0, '/Users/oskarahlroth/Documents/Portfolio/workspace/udemy/python/pdf-reading/notify-payment/')
import email_handler, user_input

user_inputs = {}
class NotifyPaymentTests(unittest.TestCase):
    def setUp(self):
        global user_inputs
        user_inputs['invoice_number'] = 'ABC123'
        user_inputs['bill_type'] = 'r'
        user_inputs['transfer_receipt_filename'] = 'bill.pdf'
        email_handler.set_bill_type(user_inputs['bill_type'])

    def test_get_full_bill_type_name(self):
        full_bill_type_name = email_handler.get_full_bill_type_name()
        self.assertEqual(full_bill_type_name, 'RENT')

    def test_make_subject(self):
        subject = email_handler.get_subject()
        self.assertEqual(subject, 'RENT DAMEN - A 16 13A')

    def test_message(self):
        message = email_handler.get_body_message(user_inputs)
        self.assertTrue(message)

unittest.main()
