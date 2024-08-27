import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
import Bank
import BankAccount

class BankApplication:

    def __init__(self,master):
        self.master = master
        master.title("Bank Application")

        self.login_screen()

    def login_screen(self):
        self.label_account_holder = tk.Label(self.master, text="Username:")
        self.label_account_holder.pack()
        self.entry_account_holder = tk.Entry(self.master)
        self.entry_account_holder.pack()

        self.label_password = tk.Label(self.master, text="Password")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self.master, text="Log In", command=self.login)
        self.button_login.pack()

        self.button_create_account = tk.Button(self.master, text="Create Account",command=self.create_account)
        self.button_create_account.pack()
        
    def login(self):
        print("Login")

    def create_account(self):
        account_holder = self.entry_account_holder.get()
        password = self.entry_password.get()
        
        if account_holder and password:
            self.open_account()


    def home_screen(self):
        self.label_account_number = tk.Label(self.master, text="Account Number:")
        self.label_account_number.pack()
        self.entry_account_number = tk.Entry(self.master)
        self.entry_account_number.pack()

        self.label_account_holder = tk.Label(self.master, text="Account Holder:")
        self.label_account_holder.pack()
        self.entry_account_holder = tk.Entry(self.master)
        self.entry_account_holder.pack()

        self.btn_open_account = tk.Button(self.master, text="Open Account", command=self.open_account)
        self.btn_open_account.pack()

        self.btn_deposit = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.btn_deposit.pack()

        self.btn_withdraw = tk.Button(self.master, text="Withdraw", command=self.withdraw)
        self.btn_withdraw.pack()

        self.btn_view_details = tk.Button(self.master, text="View Details", command=self.view_details)
        self.btn_view_details.pack()

    def open_account(self):
        account_number = int(self.entry_account_number.get())
        account_holder = self.entry_account_holder.get()
        self.bank.open_account(account_number, account_holder)
        print(f"Account created successfully. Account Number: {account_number}")


    def deposit(self):
        account_number = int(self.entry_account_number.get())
        amount = float(tk.simpledialog.askstring("Deposit", "Enter the deposit amount:"))
        self.bank.deposit(account_number, amount)

    def withdraw(self):
        account_number = int(self.entry_account_number.get())
        amount = float(tk.simpledialog.askstring("Withdraw", "Enter the withdrawal amount:"))
        self.bank.withdraw(account_number, amount)

    def view_details(self):
        account_number = int(self.entry_account_number.get())
        self.bank.view_account_details(account_number)
        #self.label = tk.Label(self.master, text="")
        #self.label.pack()

        #self.create_button = tk.Button(self.master, text="Create account", command=self.greet)
        #self.login_button = tk.Button(self.master, text="Log in", command=self.greet)
        #self.create_button.pack()
        #self.login_button.pack()



    def greet(self):
        print("Enter name:")


if __name__ == '__main__':

    TkWindow = tk.Tk()
    TkWindow.geometry('400x200')
    bank_gui = BankApplication(TkWindow)
    TkWindow.mainloop()