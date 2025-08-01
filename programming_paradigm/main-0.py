from bank_account import BankAccount

def main():
    # Create a new bank account with an initial balance of $100
    account = BankAccount(100)

    # Display initial balance
    account.display_balance()

    # Deposit $50
    account.deposit(50)
    print("Deposited $50.")
    account.display_balance()

    # Attempt to withdraw $30
    if account.withdraw(30):
        print("Withdrew $30.")
    else:
        print("Insufficient funds to withdraw $30.")
    account.display_balance()

    # Attempt to withdraw $150
    if account.withdraw(150):
        print("Withdrew $150.")
    else:
        print("Insufficient funds to withdraw $150.")
    account.display_balance()

if __name__ == "__main__":
    main()
