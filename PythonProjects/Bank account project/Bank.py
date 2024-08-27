import BankAccount
class Bank:
    def __init__(self):
        self.accounts = {}

    # Need to create a password first.
    def open_account(self, account_number, account_holder,password):
        account = BankAccount(account_number,account_holder,password)
        self.accounts[account_number] = account
        print(f"Account created. Account Number: {account_number}")

    def close_account(self, account_number):
        if account_number in self.accounts:
            self.accounts.pop(account_number).close_account()
        else:
            print("Account could not be found.")

    def view_account_details(self,account_number):
        if account_number in self.accounts:
            self.accounts[account_number].display_balance()

        else:
            print("Account could not be found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account could not be found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account could not be found.")

    def view_all_accounts(self):
        for account in self.accounts.items():
            account.display_balance()


