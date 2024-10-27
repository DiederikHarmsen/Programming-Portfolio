class BankAccount:
    def __init__(self,account_number, account_holder, balance=0, password, transactions):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.password = password
        self.transactions = []

    
    #Method for a deposit
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("DEPOSIT", amount))

    def withdraw(self, amount):
        if self.balance < amount:
            # Put it into label
            print("Not enough funds.")
        else:
            self.balance -= amount
            self.transactions.append(("WITHDRAWAL",amount))

    def display_balance(self):
        # Put it into labels.
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

    def close_account(self):
        self.balance = 0
        self.transactions = []
        # Put it into label/new window.
        print("Account closed.")


