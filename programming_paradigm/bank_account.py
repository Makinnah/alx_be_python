class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional starting balance.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount from the account balance if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current account balance.
        """
        print(f"Current Balance: ${self.account_balance}")
