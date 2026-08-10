
class AccountRepository:

    def __init__(self, session):
        self.session = session

    def find_by_id(self, account_id):
        statement = select(Account).where(Account.id == account_id)
        account = self.session.scalars(statement).first()

        return account
