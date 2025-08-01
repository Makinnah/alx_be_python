import unittest
from bank_account import BankAccount
from io import StringIO
import sys

class TestBankAccount(unittest.TestCase):
    def test_display_balance(self):
        account = BankAccount(200)

        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        account.display_balance()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check if output matches expected string
        self.assertEqual(captured_output.getvalue().strip(), "Current Balance: $200")

if __name__ == '__main__':
    unittest.main()
