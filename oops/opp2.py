class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print("Deposit:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdraw:", amount)
        else:
            print("Insufficient balance")

    def checkBalance(self):
        print("Balance:", self.balance)


b = BankAccount(1000)
b.deposit(500)
b.withdraw(250)
b.checkBalance()
