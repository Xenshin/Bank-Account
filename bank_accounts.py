class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmmount, acctName):
        self.balance = initialAmmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \nBalance = ₹{self.balance:.2f}")

    def getBalance(self):
        print(f"\nFor Account '{self.name}' balance = ₹{self.balance:.2f}")

    def deposit(self, ammount):
        self.balance = self.balance + ammount
        print("\nDeposit Complete")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ₹{self.balance:.2f}")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: '{error}'")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete! ✅\n\n*********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, ammount):
        self.balance = self.balance + (ammount*1.05)
        print("\nDeposit Complete.")
        self.getBalance()