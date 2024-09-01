'''
Написати систему, яка дозволить переказувати гроші між двома аккаунтами в банку
'''
import time
from threading import Thread, Lock

class BankAccount:
    def __init__(self, name: str, balance: int) -> None: # Decimal
        self.name = name
        self.balance = balance
        self.lock = Lock()

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount


account_one = BankAccount("Igor", 1000)
account_two = BankAccount("Vasya", 10000)

# Igor -> 1000, Vasya -> 10000 (10100)
# Igor -> 1000 (2000), Vasya -> 10000 (9000)

def transfer(account_from: BankAccount, account_to: BankAccount, amount: int):
    first_lock = min(id(account_from), id(account_to))
    second_lock = max(id(account_from), id(account_to))

    if (id(account_from) < id(account_to)):
        first_lock = account_from.lock
        second_lock = account_to.lock
    else:
        first_lock = account_to.lock
        second_lock = account_from.lock

    with first_lock: 
        time.sleep(1)
        with second_lock:
            account_from.withdraw(amount)
            account_to.deposit(amount)

def transfer_one():
    print("Transfering 100 UAH from Igor to Vasya")
    transfer(account_one, account_two, 100)

def transfer_two():
    print("Transfering 1000 UAH from Vasya to Igor")
    transfer(account_two, account_one, 1000)

thread1 = Thread(target=transfer_one)
thread2 = Thread(target=transfer_two)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
# transfer_one()
# transfer_two()

print(account_one.balance)
print(account_two.balance)

# print(id(account_one))
# print(id(account_two))
