class BankAccount:
    def __init__(self,account_holder,initial_balance=0.0):
        self.account_holder=account_holder
        self.balance=initial_balance
    def deposit(self,amount):
        if amount<=0:
            print("the amount cannot be negative")
        else:
            self.balance=amount+self.balance
            print(f"${amount:.2f} deposited. New_balance:${self.balance:.2f}")
    def withdraw(self,amount):
        if amount<=0:
            print("the amount for withdraw cannot be negative")
        elif amount>self.balance:
            print("insufficient funds")
        else:
            self.balance=self.balance-amount
            print(f"${amount:.2f} withdrawn. New_balance:${self.balance:.2f}")
    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance
account=BankAccount("Abhishek",10000)
account.deposit(5000)
account.withdraw(12000)
account.check_balance()