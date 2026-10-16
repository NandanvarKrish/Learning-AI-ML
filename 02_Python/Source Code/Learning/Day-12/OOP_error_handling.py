# Defining Errors

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Amount {amount} is less than 0! It should be positive.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Amount {amount} is less than 0! It should be positive.")

        if amount > self.balance:
            raise InsufficientBalanceError(f"{self.owner} has only {self.__balance}, tried to withdraw {amount}.")

        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, owner, balance = 0, rate = 0.02):
        super().__init__(owner, balance)
        self.rate = rate

    def apply_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)
        return self.balance




# account = Account('Krish', 2000)
# savingsAccount = SavingsAccount('Krish', 0)
#
# print(f"Total Balance after deposit : {account.deposit(1000)}")
# print(f"Total Balance after adding Interest : {savingsAccount.apply_interest()}")
# # print(f"Total Balance after Withdrawl : {account.withdraw(500)}")

# account = SavingsAccount('Krish', 2000)

# try:
#     account.withdraw(500)
#
# except InsufficientBalanceError as e:
#     print(f"Transition Blocked : {e}")
#
# except InvalidAmountError as e:
#     print(f"Invalid request : {e}")
#
# else:
#     print("Withdrawl Successful")
#
# finally:
#     print(f"Current balance: {account.get_balance()}")


account = SavingsAccount('Krish', 2000)

account.deposit(1000)
account.apply_interest()
print(account.get_balance())

try:
    account.withdraw(50)

except (InsufficientBalanceError, InvalidAmountError) as e:
    print(f"Error: {e}")

else:
    print("Withdrawal went through cleanly.")

finally:
    print("Cleanly finally.")

