from database import Session
from models import User
from banking_service import BankingService


session = Session()

service = BankingService(session)

user = service.create_user("Alice")

account = service.create_account(
    user,
    "Savings",
    1000
)

print(user.id)
print(account.name)
print(account.balance)
