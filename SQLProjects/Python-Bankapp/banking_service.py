from models import User, Account, Transaction


class BankingService:
    def __init__(self, session):
        self.session = session

    def create_user(self, name):
        user = User(name=name)

        self.session.add(user)
        self.session.commit()

        return user

    def create_account(self, user, name, balance):
        account = Account(
            name=name,
            balance=balance,
            user=user
        )

        self.session.add(account)
        self.session.commit()

        return account

    def deposit(self, account, amount):
        account.balance += amount

        transaction = Transaction(
            account=account,
            amount=amount,
            type="DEPOSIT"
        )

        self.session.add(transaction)
        self.session.commit()

        return transaction

    def withdraw(self, account, amount):
        if amount <= 0:
            return False

        if account.balance < amount:
            return False

        account.balance -= amount

        transaction = Transaction(
            account=account,
            amount=amount,
            type="WITHDRAW"
        )

        self.session.add(transaction)
        self.session.commit()

        return transaction

    def transfer(self, from_account, to_account, amount):
        if amount <= 0:
            return False
    
        if from_account.balance < amount:
            return False
    
        try:
            from_account.balance -= amount
            to_account.balance += amount
    
            transaction_from = Transaction(
                account=from_account,
                amount=amount,
                type="WITHDRAW"
            )
    
            transaction_to = Transaction(
                account=to_account,
                amount=amount,
                type="DEPOSIT"
            )
    
            self.session.add(transaction_from)
            self.session.add(transaction_to)
    
            self.session.commit()
    
        except:
            self.session.rollback()
            raise
    
        return True
