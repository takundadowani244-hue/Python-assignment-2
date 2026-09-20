## Question 2: Encapsulation — BankAccount Class##
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute (name-mangled to _BankAccount__balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def display_balance(self):
        print(f"Current balance for {self.owner}: ${self.__balance:.2f}")


# Demonstration
account = BankAccount("Francois", 100)
account.display_balance()
account.deposit(50)
account.withdraw(30)
account.withdraw(1000)   # insufficient funds

# Direct access is blocked/hidden:
# print(account.__balance)        # AttributeError
print(account._BankAccount__balance)  # 120.0 — shows name mangling, but you shouldn't rely on this
